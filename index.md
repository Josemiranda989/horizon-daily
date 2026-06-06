---
layout: default
title: Horizon Daily
---

# 🌅 Horizon Daily

AI-curated daily digest of tech, AI, and self-hosting news — fetched from Hacker News, Reddit, and RSS feeds.

## Latest Briefings

<ul>
{% for post in site.posts limit:7 %}
  <li>
    <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small>{{ post.date | date: "%B %d, %Y" }}</small>
  </li>
{% endfor %}
</ul>

[Subscribe via RSS]({{ '/feed-en.xml' | relative_url }})

---

<small>Powered by [Horizon](https://github.com/Thysrael/Horizon) · Automated daily at 9 AM (UTC-3)</small>
