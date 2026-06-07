---
layout: default
title: Horizon Daily
---

<div class="hero">
  <h1>🌅 Horizon Diario</h1>
  <p class="hero-sub">Briefings diarios de tech, AI y self-hosting — curados por IA desde HN, Reddit y RSS.</p>
  <div class="hero-stats">
    <span class="stat"><strong>{{ site.posts.size }}</strong> ediciones</span>
    {% assign latest = site.posts | first %}
    <span class="stat">Última: <strong>{{ latest.date | date: "%d/%m" }}</strong></span>
  </div>
</div>

<div class="briefings-grid">
{% for post in site.posts limit:14 %}
  <a href="{{ post.url | relative_url }}" class="briefing-card">
    <div class="card-date">
      <span class="date-day">{{ post.date | date: "%d" }}</span>
      <span class="date-month">{{ post.date | date: "%b" }}</span>
    </div>
    <div class="card-body">
      <h2 class="card-title">{{ post.title }}</h2>
      {% assign excerpt = post.excerpt | strip_html | truncate: 140 %}
      <p class="card-excerpt">{{ excerpt }}</p>
    </div>
    <div class="card-arrow">→</div>
  </a>
{% endfor %}
</div>

<div class="page-footer">
  <a href="{{ '/feed.xml' | relative_url }}" class="rss-link">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M6.18 15.64a2.18 2.18 0 0 1 2.18 2.18C8.36 19 7.38 20 6.18 20C5 20 4 19 4 17.82a2.18 2.18 0 0 1 2.18-2.18M4 4.44A15.56 15.56 0 0 1 19.56 20h-2.83A12.73 12.73 0 0 0 4 7.27V4.44m0 5.66a9.9 9.9 0 0 1 9.9 9.9h-2.83A7.07 7.07 0 0 0 4 12.93V10.1Z"/></svg>
    RSS
  </a>
  <span class="footer-note">Generado con <a href="https://github.com/Thysrael/Horizon">Horizon</a> · Diario 9 AM (UTC-3)</span>
</div>
