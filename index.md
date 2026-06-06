---
layout: default
title: Horizon Daily
---

# 🌅 Horizon Diario

Resumen diario de noticias tech, AI y self-hosting — extraído de Hacker News, Reddit y RSS.

## Últimos Briefings

<ul>
{% for post in site.posts limit:7 %}
  <li>
    <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small>{{ post.date | date: "%B %d, %Y" }}</small>
  </li>
{% endfor %}
</ul>

[Suscribirse vía RSS]({{ '/feed-en.xml' | relative_url }})

---

<small>Generado con [Horizon](https://github.com/Thysrael/Horizon) · Automático todos los días a las 9 AM (UTC-3)</small>
