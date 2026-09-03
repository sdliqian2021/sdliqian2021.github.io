---
layout: default
title: Home
description: Qian Li's learning thoughts on Industrial AI, simulation, digital twins, and the tire industry.
nav: home
---

<header class="blog-intro">
  <h1>Welcome to Qian's blog.</h1>
  <p>
    Hi, I am Qian Li, I use this blog to document my thoughts on Tire Industry, Industrial AI, engineering simulations and digital twins.
  </p>
</header>

<section id="technical-essays" class="post-section" aria-labelledby="technical-essays-title">
  <h2 id="technical-essays-title">Technical thoughts</h2>
  {% assign essays = site.pages | where: "content_type", "essay" | sort: "display_order" %}
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
