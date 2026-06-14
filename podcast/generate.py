#!/usr/bin/env python3
"""Generate podcast audio from latest Horizon briefing using edge-tts.

Cleans markdown/HTML thoroughly and transforms into a conversational script
before passing to TTS. No URLs, no HTML tags, no hashtags, no metadata noise.
"""

import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime

BRIEFING_DIR = Path.home() / "Horizon" / "data" / "summaries"
PODCAST_DIR = Path.home() / "horizon-daily-pages" / "podcast"
VOICE = "es-AR-ElenaNeural"
SITE_URL = "https://daily.jmlabs.app"
RAW_URL = "https://raw.githubusercontent.com/Josemiranda989/horizon-daily/main"

# ── Cleaning ────────────────────────────────────────────────────────────────

def clean_markdown(text: str) -> str:
    """Aggressive cleaning: strip everything that sounds bad when read aloud.
    
    Order matters: strip HTML and section blocks BEFORE stripping bold markers,
    so we can match on **Contexto**: etc.
    """

    # 1. Strip HTML tags first
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&[a-zA-Z]+;', '', text)
    text = re.sub(r'&#?\d+;', '', text)

    # 2. Remove the TOC (numbered item list between first --- and second ---)
    #    Looks like: "1. [Title](url) ⭐️ 9.0/10\n2. ..."
    text = re.sub(
        r'(---\s*\n)((?:\d+\.\s+\[?.+?\n)+)(---)',
        r'\1\3', text, flags=re.DOTALL
    )

    # 3. Remove "Contexto:" blocks (before bold stripping so **Contexto** matches)
    text = re.sub(r'\*\*Contexto\*\*:.*?(?=\n\n|\n\*\*|$)', '', text, flags=re.DOTALL)

    # 4. Remove "Discusión:" blocks
    text = re.sub(r'\*\*Discusión\*\*:.*?(?=\n\n|\n\*\*|$)', '', text, flags=re.DOTALL)

    # 5. Remove "Etiquetas:" lines
    text = re.sub(r'\*\*Etiquetas\*\*:.*$', '', text, flags=re.MULTILINE)

    # 6. Remove <details> reference blocks (now just text after HTML strip)
    #    They look like: "Referencias\nClaude Mythos\nAnthropic launches..."
    text = re.sub(r'Referencias\s*\n(?:.+\n?)*?(?=\n\n|\n(?:---|\*\*)|$)', '', text)

    # 7. Convert markdown links: [text](url) → text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # 8. Strip bare URLs
    text = re.sub(r'https?://\S+', '', text)

    # 9. Strip markdown headers (# → plain text)
    #    But first, ensure each ## item is separated by \n\n to prevent merging
    text = re.sub(r'\n(## )', r'\n\n\1', text)
    text = re.sub(r'^#{1,4}\s+', '', text, flags=re.MULTILINE)

    # 10. Strip bold/italic markers (now safe — sections are already removed)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)

    # 11. Strip inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)

    # 12. Strip hashtags: #IA → IA
    text = re.sub(r'#(\w+)', r'\1', text)

    # 13. Strip list markers
    text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)

    # 14. Strip horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)

    # 15. Remove metadata lines (source · author · date)
    text = re.sub(r'^[a-z]+\s*·\s*.+$', '', text, flags=re.MULTILINE)

    # 16. Remove score/emoji from titles: "⭐️ 9.0/10" → nothing
    #     ⭐ can come with or without variation selector (U+FE0F)
    text = re.sub(r'⭐️?\s*[\d.]+/\d+', '', text)
    text = re.sub(r'🌟\s*[\d.]+/\d+', '', text)

    # 17. Remove "Horizon Diario - YYYY-MM-DD" title line
    text = re.sub(r'^Horizon Diario\s*[-–]\s*\d{4}-\d{2}-\d{2}\s*$', '', text, flags=re.MULTILINE)

    # 18. Remove the quote summary line: "> De X artículos..."
    text = re.sub(r'^>\s*.+$', '', text, flags=re.MULTILINE)

    # 19. Remove leftover reference artifacts — short lines that are just
    #     titles from references (single line, often English, 3-10 words)
    #     e.g. "Claude Mythos \\ Anthropic", "PeopleSoft", "Zero - day vulnerability"
    text = re.sub(r'^[A-Z].{5,80}\n(?=\n\n|\n(?:---|Pasamos|$))', '', text, flags=re.MULTILINE)

    # 20. Collapse whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)

    return text.strip()


# ── Conversational transformation ───────────────────────────────────────────

def to_conversational(text: str, date_str: str) -> str:
    """Transform cleaned text into a natural-sounding podcast script."""

    # Split into paragraphs (double newline separated)
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    # Filter noise: skip very short leftovers
    paragraphs = [p for p in paragraphs if len(p) > 40 or 
                  (len(p) > 15 and not p.startswith('Horizon'))]

    # Date in Spanish
    meses = {
        '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril',
        '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto',
        '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
    }
    y, m, d = date_str.split('-')
    fecha_es = f"{int(d)} de {meses[m]} de {y}"

    # Build script
    lines = []
    lines.append(f"Daily, el resumen diario de tecnología e inteligencia artificial.")
    lines.append(f"Edición del {fecha_es}.")
    lines.append("")
    lines.append("Comenzamos con las noticias más destacadas del día.")
    lines.append("")

    item_count = 0
    for para in paragraphs:
        # Detect new item: starts with a heading-like line (short, title case)
        first_line = para.split('\n')[0]
        is_title = (
            len(first_line) < 200 and
            len(first_line) > 10 and
            (first_line[0].isupper() or first_line[0].isdigit() 
             or first_line[0] in '¿¡"$')
        )
        
        if is_title:
            item_count += 1
            if item_count > 1:
                lines.append("")
                lines.append("Pasamos a la siguiente noticia.")
                lines.append("")

        lines.append(para)

    # Closing
    lines.append("")
    lines.append("Esto fue todo por hoy. Soy Elena, y esto fue Daily, tu resumen diario de tecnología.")
    lines.append("Nos escuchamos mañana.")

    return '\n'.join(lines)


# ── Audio generation ────────────────────────────────────────────────────────

def generate_audio(text: str, output_path: Path) -> bool:
    """Generate MP3 audio using edge-tts."""
    tmp_txt = output_path.with_suffix('.txt')
    tmp_txt.write_text(text, encoding='utf-8')

    result = subprocess.run(
        ["edge-tts", "--voice", VOICE, "--file", str(tmp_txt),
         "--write-media", str(output_path)],
        capture_output=True, text=True, timeout=600
    )
    tmp_txt.unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"edge-tts error: {result.stderr}", file=sys.stderr)
        return False

    return output_path.exists() and output_path.stat().st_size > 0


# ── RSS Feed ────────────────────────────────────────────────────────────────

def update_podcast_feed(audio_file: str, title: str, date: str,
                        duration_sec: int, size_bytes: int):
    """Generate podcast RSS feed with latest episode."""
    episodes = []
    feed_path = PODCAST_DIR / "feed.xml"

    if feed_path.exists():
        existing = feed_path.read_text(encoding='utf-8')
        items = re.findall(r'<item>.*?</item>', existing, re.DOTALL)
        episodes = items

    pub_date = datetime.now().strftime("%a, %d %b %Y 09:00:00 -0300")
    episode_xml = f"""    <item>
      <title>{title}</title>
      <description>Briefing diario de tech, AI y self-hosting — {date}</description>
      <enclosure url="{RAW_URL}/podcast/{audio_file}" length="{size_bytes}" type="audio/mpeg"/>
      <guid isPermaLink="false">{date}</guid>
      <pubDate>{pub_date}</pubDate>
      <duration>{duration_sec}</duration>
    </item>"""

    all_episodes = [episode_xml] + [e for e in episodes if date not in e][:29]

    feed_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>Daily — Briefing Tech &amp; AI</title>
    <link>{SITE_URL}</link>
    <description>Resumen diario de noticias de tecnología, inteligencia artificial y self-hosting. Curado por IA desde HN, Reddit y RSS. Narrado por Elena.</description>
    <language>es</language>
    <itunes:author>Horizon AI</itunes:author>
    <itunes:summary>Briefing diario de tech, AI y self-hosting</itunes:summary>
    <itunes:category text="Technology"/>
    <itunes:image href="{SITE_URL}/podcast/cover.jpg"/>
    <itunes:explicit>no</itunes:explicit>
    <itunes:owner>
      <itunes:name>José Miranda</itunes:name>
      <itunes:email>josemiranda989@gmail.com</itunes:email>
    </itunes:owner>
{chr(10).join(all_episodes)}
  </channel>
</rss>"""

    feed_path.write_text(feed_xml, encoding='utf-8')


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    briefing = find_latest_briefing()
    if not briefing:
        print("No briefing found", file=sys.stderr)
        sys.exit(1)

    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', briefing.name)
    date_str = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")

    audio_filename = f"daily-{date_str}.mp3"
    audio_path = PODCAST_DIR / audio_filename
    if audio_path.exists():
        audio_path.unlink()  # overwrite for re-generation
        print(f"Removed old: {audio_filename}")

    print(f"Processing: {briefing.name}")
    raw = briefing.read_text(encoding='utf-8')

    # Clean
    cleaned = clean_markdown(raw)
    # Transform to conversational
    script = to_conversational(cleaned, date_str)

    word_count = len(script.split())
    print(f"Script: {word_count} words, {len(script)} chars")

    # Save script for debugging
    script_path = PODCAST_DIR / f"script-{date_str}.txt"
    script_path.write_text(script, encoding='utf-8')
    print(f"Script saved: {script_path}")

    # Generate audio
    print("Generating audio with edge-tts (Elena, Argentine Spanish)...")
    if not generate_audio(script, audio_path):
        print("Failed to generate audio", file=sys.stderr)
        sys.exit(1)

    size_mb = audio_path.stat().st_size / (1024 * 1024)
    print(f"Audio: {size_mb:.1f} MB")

    # Duration via ffprobe
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)],
            capture_output=True, text=True, timeout=10
        )
        duration = int(float(result.stdout.strip()))
    except Exception:
        duration = word_count // 3

    mins = duration // 60
    secs = duration % 60
    print(f"Duration: {mins}:{secs:02d}")

    # Update podcast feed
    title = f"Daily — {date_str}"
    update_podcast_feed(audio_filename, title, date_str, duration, audio_path.stat().st_size)
    print(f"Feed updated: podcast/feed.xml")
    print("Done!")


def find_latest_briefing() -> Path | None:
    files = sorted(BRIEFING_DIR.glob("horizon-*-es.md"), reverse=True)
    return files[0] if files else None


if __name__ == "__main__":
    main()
