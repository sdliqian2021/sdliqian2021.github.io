---
layout: default
title: Home
description: Technical essays on Industrial AI, digital twins, engineering simulation, and tire-industry intelligence.
nav: home
---

<section class="hero">
  <p class="eyebrow">Qian Li's technical blog</p>
  <h1>Industrial AI, engineering, and the systems between them.</h1>
  <p class="hero-copy">
    Technical essays on digital twins, simulation, industrial workflows, and
    the tire ecosystems where technology meets manufacturing reality.
  </p>
  <div class="button-row">
    <a class="button" href="#technical-essays">Read technical essays</a>
    <a class="button button-secondary" href="{{ site.intelligence_url }}/">Explore tire intelligence</a>
  </div>
</section>

<section class="content-section" aria-labelledby="reading-modes-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">One publication, two reading modes</p>
      <h2 id="reading-modes-title">Ideas and intelligence</h2>
    </div>
    <p>
      The technical blog develops engineering ideas. Tire &amp; Rubber
      Intelligence follows industry evidence through recurring reports and
      deeper analysis.
    </p>
  </div>

  <div class="publication-grid">
    <article class="publication-card">
      <p class="eyebrow">Technical essays &amp; notes</p>
      <h3>Developing ideas in public</h3>
      <p>
        First-person technical thinking about Industrial AI, digital twins,
        simulation workflows, manufacturing systems, and tire-industry
        innovation.
      </p>
      <a class="text-link" href="#technical-essays">Browse the essay archive <span aria-hidden="true">→</span></a>
    </article>

    <article class="publication-card featured">
      <p class="eyebrow">Tire &amp; Rubber Intelligence</p>
      <h3>Evidence-led industry reporting</h3>
      <p>
        Human-reviewed weekly signals and deep analysis covering tire
        technology, manufacturing, materials, supply chains, markets, and
        policy.
      </p>
      <a class="text-link" href="{{ site.intelligence_url }}/">Open the intelligence publication <span aria-hidden="true">→</span></a>
    </article>
  </div>
</section>

<section id="technical-essays" class="content-section" aria-labelledby="technical-essays-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Archive</p>
      <h2 id="technical-essays-title">Technical essays</h2>
    </div>
    <p>
      Human-authored notes, refined with proofreading and evidence support
      before final editorial approval.
    </p>
  </div>

  {% assign essays = site.pages | where: "content_type", "essay" | sort: "updated" | reverse %}
  <div class="article-list">
    {% for essay in essays %}
      <article class="article-card">
        <div class="article-meta">
          <span>{{ essay.updated | default: essay.published | date: "%B %-d, %Y" }}</span>
          {% if essay.topics %}
            <span class="topic-list">
              {% for topic in essay.topics limit: 2 %}
                <span class="topic">{{ topic }}</span>
              {% endfor %}
            </span>
          {% endif %}
        </div>
        <div>
          <h3><a href="{{ essay.url | relative_url }}">{{ essay.title }}</a></h3>
          {% if essay.description %}<p>{{ essay.description }}</p>{% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>
