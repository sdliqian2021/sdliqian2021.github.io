from __future__ import annotations

import argparse
import html
import mimetypes
import re
import threading
import unicodedata
import webbrowser
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


MAIN_ROOT = Path(__file__).resolve().parent.parent
INTELLIGENCE_ROOT = MAIN_ROOT.parent / "tire-and-rubber-weekly-intelligence-report"
INTELLIGENCE_BASE = "/tire-and-rubber-weekly-intelligence-report"


def parse_simple_yaml(text: str) -> dict[str, object]:
    values: dict[str, object] = {}
    list_key: str | None = None
    for raw_line in text.splitlines():
        if list_key and re.match(r"^\s+-\s+", raw_line):
            item = re.sub(r"^\s+-\s+", "", raw_line).strip().strip('"\'')
            current = values[list_key]
            if isinstance(current, list):
                current.append(item)
            continue
        line = raw_line.strip()
        list_key = None
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            values[key] = []
            list_key = key
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if re.fullmatch(r"-?\d+", value):
            values[key] = int(value)
        else:
            values[key] = value
    return values


def split_front_matter(text: str) -> tuple[dict[str, object], str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, normalized
    marker = normalized.find("\n---\n", 4)
    if marker < 0:
        raise ValueError("Unclosed YAML front matter")
    return parse_simple_yaml(normalized[4:marker]), normalized[marker + 5 :]


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[^\w\s-]", "", value).replace("_", "-")
    return re.sub(r"[\s-]+", "-", value).strip("-")


def inline_markdown(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda match: f'<img src="{match.group(2)}" alt="{match.group(1)}">',
        escaped,
    )
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: f'<a href="{match.group(2)}">{match.group(1)}</a>',
        escaped,
    )
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"(?<!_)_([^_]+?)_(?!_)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def markdown_to_html(markdown: str, replacements: dict[str, str]) -> str:
    for source, target in replacements.items():
        markdown = markdown.replace(source, target)
    lines = markdown.replace("\r\n", "\n").split("\n")
    output: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    code_lines: list[str] | None = None
    code_language = ""

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            output.append(f"</{list_type}>")
            list_type = None

    index = 0
    while index < len(lines):
        raw_line = lines[index]
        line = raw_line.strip()

        if code_lines is not None:
            if line.startswith("```"):
                language = f' class="language-{html.escape(code_language)}"' if code_language else ""
                output.append(f"<pre><code{language}>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = None
                code_language = ""
            else:
                code_lines.append(raw_line)
            index += 1
            continue

        if line.startswith("```"):
            flush_paragraph()
            close_list()
            code_lines = []
            code_language = line[3:].strip()
            index += 1
            continue

        if (
            line.startswith("|")
            and index + 1 < len(lines)
            and re.fullmatch(r"\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*", lines[index + 1])
        ):
            flush_paragraph()
            close_list()
            headers = table_cells(line)
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(table_cells(lines[index]))
                index += 1
            output.append("<table><thead><tr>")
            output.extend(f"<th>{inline_markdown(cell)}</th>" for cell in headers)
            output.append("</tr></thead><tbody>")
            for row in rows:
                output.append("<tr>")
                output.extend(f"<td>{inline_markdown(cell)}</td>" for cell in row)
                output.append("</tr>")
            output.append("</tbody></table>")
            continue

        if not line:
            flush_paragraph()
            close_list()
            index += 1
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            title = heading.group(2)
            output.append(
                f'<h{level} id="{html.escape(slugify(title))}">{inline_markdown(title)}</h{level}>'
            )
            index += 1
            continue

        if re.fullmatch(r"-{3,}", line):
            flush_paragraph()
            close_list()
            output.append("<hr>")
            index += 1
            continue

        unordered = re.match(r"^-\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            wanted = "ul" if unordered else "ol"
            if list_type != wanted:
                close_list()
                output.append(f"<{wanted}>")
                list_type = wanted
            item = unordered.group(1) if unordered else ordered.group(1)
            output.append(f"<li>{inline_markdown(item)}</li>")
            index += 1
            continue

        if line.startswith(">"):
            flush_paragraph()
            close_list()
            quotes: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quotes.append(lines[index].strip().removeprefix(">").strip())
                index += 1
            output.append(f"<blockquote><p>{inline_markdown(' '.join(quotes))}</p></blockquote>")
            continue

        if line.startswith("<") and line.endswith(">"):
            flush_paragraph()
            close_list()
            output.append(raw_line)
            index += 1
            continue

        paragraph.append(line)
        index += 1

    if code_lines is not None:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    flush_paragraph()
    close_list()
    return "\n".join(output)


def load_config(root: Path) -> dict[str, object]:
    return parse_simple_yaml((root / "_config.yml").read_text(encoding="utf-8"))


def load_collection(root: Path, folder: str, content_type: str) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for path in (root / folder).glob("*.md"):
        metadata, body = split_front_matter(path.read_text(encoding="utf-8"))
        if metadata.get("content_type") != content_type:
            continue
        metadata["body"] = body
        metadata["path"] = path
        items.append(metadata)
    return items


def local_replacements(config: dict[str, object]) -> dict[str, str]:
    return {
        "{{ site.primary_site_url }}": "",
        "{{ site.intelligence_url }}": INTELLIGENCE_BASE,
        "{{ site.baseurl }}": str(config.get("baseurl", "")),
    }


def render_main_index(config: dict[str, object], essays: list[dict[str, object]]) -> tuple[dict[str, object], str]:
    metadata, body = split_front_matter((MAIN_ROOT / "index.md").read_text(encoding="utf-8"))
    essays = sorted(essays, key=lambda item: int(item.get("display_order", 9999)))
    cards: list[str] = []
    for essay in essays:
        title = html.escape(str(essay.get("title", "Technical thought")))
        permalink = html.escape(str(essay.get("permalink", "/")), quote=True)
        description = str(essay.get("description", ""))
        updated = date.fromisoformat(str(essay.get("updated", essay.get("published"))))
        date_text = f"{updated.strftime('%B')} {updated.day}, {updated.year}"
        topics = essay.get("topics", [])
        topic_text = ", ".join(str(topic) for topic in topics) if isinstance(topics, list) else str(topics)
        description_line = f"        <p>{html.escape(description)}</p>\n" if description else ""
        topic_suffix = f" · {html.escape(topic_text)}" if topic_text else ""
        cards.append(
            "      <article class=\"post-preview\">\n"
            f"        <h3><a href=\"{permalink}\">{title}</a></h3>\n"
            f"{description_line}"
            f"        <p class=\"post-meta\">{date_text}{topic_suffix}</p>\n"
            "      </article>"
        )
    body = re.sub(r"(?m)^\s*\{% assign essays = .*?%\}\s*", "", body)
    body = re.sub(
        r"(?s)\s*\{% for essay in essays %\}.*?\{% endfor %\}",
        "\n" + "\n".join(cards) + "\n",
        body,
        count=1,
    )
    return metadata, body


def format_period(start_text: str, end_text: str) -> str:
    start = date.fromisoformat(start_text)
    end = date.fromisoformat(end_text)
    if start.year != end.year:
        return f"{start.strftime('%B')} {start.day}, {start.year}–{end.strftime('%B')} {end.day}, {end.year}"
    if start.month == end.month:
        return f"{start.strftime('%B')} {start.day}–{end.day}, {end.year}"
    return f"{start.strftime('%B')} {start.day}–{end.strftime('%B')} {end.day}, {end.year}"


def render_intelligence_index(
    config: dict[str, object], reports: list[dict[str, object]]
) -> tuple[dict[str, object], str]:
    metadata, body = split_front_matter((INTELLIGENCE_ROOT / "index.md").read_text(encoding="utf-8"))
    reports = sorted(reports, key=lambda item: str(item.get("period_end", "")), reverse=True)
    cards: list[str] = []
    for report in reports:
        title = html.escape(str(report.get("title", "Weekly report")))
        permalink = f"{INTELLIGENCE_BASE}{str(report.get('permalink', '/'))}"
        period = format_period(str(report["period_start"]), str(report["period_end"]))
        count = html.escape(str(report.get("story_count", "")))
        cards.append(
            "      <article class=\"post-preview\">\n"
            f"        <h3><a href=\"{permalink}\">{title}</a></h3>\n"
            f"        <p class=\"post-meta\">{period} · {count} stories</p>\n"
            "      </article>"
        )
    body = re.sub(r"(?m)^\{% assign weekly_reports = .*?%\}\s*", "", body)
    body = re.sub(
        r"(?s)\s*\{% for report in weekly_reports %\}.*?\{% endfor %\}",
        "\n" + "\n".join(cards) + "\n",
        body,
        count=1,
    )
    return metadata, body


def render_layout(
    config: dict[str, object],
    metadata: dict[str, object],
    content: str,
    page_url: str,
    section: str,
) -> str:
    baseurl = str(config.get("baseurl", ""))
    site_title = str(config.get("title", "Qian Li"))
    page_title = str(metadata.get("title", ""))
    html_title = site_title if page_title == "Home" else f"{page_title} · {site_title}"
    description = str(metadata.get("description", config.get("description", "")))
    is_article = metadata.get("page_class") == "article-page" or "/posts/" in page_url or "/reports/" in page_url
    body_class = ' class="article-page"' if is_article else ""
    nav = str(metadata.get("nav", ""))
    technical_current = ' aria-current="page"' if section == "main" and nav in {"home", "essays"} else ""
    intelligence_current = ' aria-current="page"' if section == "intelligence" else ""
    about_current = ' aria-current="page"' if section == "main" and nav == "about" else ""
    year = date.today().year
    related = ""
    if metadata.get("related_url"):
        related_url = str(metadata["related_url"])
        related_title = html.escape(str(metadata.get("related_title", "Related reading")))
        related = f'<aside class="related-reading"><strong>Related:</strong> <a href="{related_url}">{related_title}</a></aside>'
    return f"""<!doctype html>
<html lang="{html.escape(str(config.get('lang', 'en')))}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light">
    <title>{html.escape(html_title)}</title>
    <meta name="description" content="{html.escape(description, quote=True)}">
    <link rel="stylesheet" href="{baseurl}/assets/css/site.css">
  </head>
  <body{body_class}>
    <a class="skip-link" href="#main-content">Skip to content</a>
    <header class="site-header">
      <div class="page-width header-inner">
        <a class="site-name" href="/">Qian Li's Notes</a>
        <nav class="site-nav" aria-label="Primary navigation">
          <a href="/#technical-essays"{technical_current}>Technical thoughts</a>
          <a href="{INTELLIGENCE_BASE}/"{intelligence_current}>Intelligence</a>
          <a href="/about.html"{about_current}>About</a>
        </nav>
      </div>
    </header>
    <main id="main-content" class="page-width main-content">
{content}
{related}
    </main>
    <footer class="site-footer">
      <div class="page-width">
        <p>© {year} Qian Li · Technical thoughts and public-source intelligence.</p>
      </div>
    </footer>
  </body>
</html>
"""


class PreviewHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        path = unquote(urlsplit(self.path).path)
        normalized = path.rstrip("/") or "/"

        if normalized == "/assets/css/site.css":
            self.send_file(MAIN_ROOT / "assets" / "css" / "site.css")
            return
        if normalized == f"{INTELLIGENCE_BASE}/assets/css/site.css":
            self.send_file(INTELLIGENCE_ROOT / "assets" / "css" / "site.css")
            return
        if normalized.startswith("/images/"):
            relative = normalized.removeprefix("/")
            candidate = (MAIN_ROOT / relative).resolve()
            if MAIN_ROOT.resolve() in candidate.parents and candidate.is_file():
                self.send_file(candidate)
                return

        main_config = load_config(MAIN_ROOT)
        intelligence_config = load_config(INTELLIGENCE_ROOT)
        essays = load_collection(MAIN_ROOT, "posts", "essay")
        reports = load_collection(INTELLIGENCE_ROOT, "reports", "weekly_report")

        if normalized == "/":
            metadata, content = render_main_index(main_config, essays)
            self.send_page(render_layout(main_config, metadata, content, "/", "main"))
            return
        if normalized == "/about.html":
            metadata, body = split_front_matter((MAIN_ROOT / "about.md").read_text(encoding="utf-8"))
            content = markdown_to_html(body, local_replacements(main_config))
            self.send_page(render_layout(main_config, metadata, content, path, "main"))
            return
        for essay in essays:
            if normalized == str(essay.get("permalink", "")).rstrip("/"):
                content = markdown_to_html(str(essay["body"]), local_replacements(main_config))
                self.send_page(render_layout(main_config, essay, content, path, "main"))
                return

        if normalized == INTELLIGENCE_BASE:
            metadata, content = render_intelligence_index(intelligence_config, reports)
            self.send_page(
                render_layout(intelligence_config, metadata, content, path, "intelligence")
            )
            return
        for report in reports:
            permalink = f"{INTELLIGENCE_BASE}{str(report.get('permalink', '/')).rstrip('/')}"
            if normalized == permalink:
                content = markdown_to_html(
                    str(report["body"]), local_replacements(intelligence_config)
                )
                self.send_page(
                    render_layout(intelligence_config, report, content, path, "intelligence")
                )
                return

        self.send_error(404, "Preview page not found")

    def send_page(self, page: str) -> None:
        self.send_bytes(page.encode("utf-8"), "text/html; charset=utf-8")

    def send_file(self, path: Path) -> None:
        if not path.is_file():
            self.send_error(404, "Preview asset not found")
            return
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        self.send_bytes(path.read_bytes(), content_type)

    def send_bytes(self, content: bytes, content_type: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview both Qian Li public websites locally")
    parser.add_argument("--port", type=int, default=4000)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    if not INTELLIGENCE_ROOT.is_dir():
        raise SystemExit(f"Sibling intelligence repository not found: {INTELLIGENCE_ROOT}")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), PreviewHandler)
    root_url = f"http://127.0.0.1:{args.port}/"
    print(f"Technical Thoughts: {root_url}")
    print(f"Intelligence: {root_url.rstrip('/')}{INTELLIGENCE_BASE}/")
    print("Save a website file and refresh the browser to see the change.")
    print("Press Ctrl+C to stop the preview server.")
    if not args.no_browser:
        threading.Timer(0.4, lambda: webbrowser.open(root_url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nPreview stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
