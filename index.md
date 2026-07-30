---
layout: default
title: Home
description: Qian Li's technical thoughts and human-reviewed industry intelligence collected with AI assistance.
nav: home
---

<header class="blog-intro">
  <h1>Hi, I'm Qian.</h1>
  <p>
    I use this blog to document technical thoughts on Industrial AI,
    engineering simulation, digital twins, and the tire industry. I also
    publish intelligence notes collected with help from AI agents and reviewed
    by me before publication.
  </p>
</header>

<section id="technical-essays" class="post-section" aria-labelledby="technical-essays-title">
  <h2 id="technical-essays-title">Technical thoughts</h2>
  {% assign essays = site.pages | where: "content_type", "essay" | sort: "updated" | reverse %}
  <div class="post-list">
    {% for essay in essays %}
      <article class="post-preview">
        <h3><a href="{{ essay.url | relative_url }}">{{ essay.title }}</a></h3>
        {% if essay.description %}<p>{{ essay.description }}</p>{% endif %}
        <p class="post-meta">
          {{ essay.updated | default: essay.published | date: "%B %-d, %Y" }}
          {% if essay.topics %} · {{ essay.topics | join: ", " }}{% endif %}
        </p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="post-section" aria-labelledby="intelligence-notes-title">
  <h2 id="intelligence-notes-title">Intelligence notes</h2>
  <div class="post-list">
    <article class="post-preview">
      <h3><a href="{{ site.intelligence_url }}/reports/2026-07-06-to-2026-07-12/">Tire and Rubber Weekly Intelligence Report: July 6–12, 2026</a></h3>
      <p>Ten public-source signals covering tire technology, materials, manufacturing, trade, markets, and sales.</p>
      <p class="post-meta">Weekly intelligence · July 15, 2026</p>
    </article>
    <article class="post-preview">
      <h3><a href="{{ site.intelligence_url }}/deep-analysis/2026-07-15-5g-enabled-tire-factory-design-loop/">How a 5G-Enabled Tire Factory Can Improve Tire Design Decisions</a></h3>
      <p>A deeper look at when connected-factory evidence can improve tire design and what the public record still cannot establish.</p>
      <p class="post-meta">Deep analysis · July 22, 2026</p>
    </article>
  </div>
  <p class="archive-link"><a href="{{ site.intelligence_url }}/">View all intelligence notes →</a></p>
</section>
