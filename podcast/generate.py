#!/usr/bin/env python3
"""Generate podcast audio from latest Horizon briefing using edge-tts."""

import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime

BRIEFING_DIR = Path.home() / "Horizon" / "data" / "summaries"
PODCAST_DIR = Path.home() / "horizon-daily-pages" / "podcast"
VOICE = "es-AR-ElenaNeural"
SITE_URL = "https://daily.jmlabs.app"

def clean_markdown(text: str) -> str:
    """Clean markdown for TTS narration."""
    text = re.sub(r'^#{1,4}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'^[-*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'---+\n', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def find_latest_briefing() -> Path | None:
    """Find most recent briefing markdown file."""
    files = sorted(BRIEFING_DIR.glob("horizon-*-es.md"), reverse=True)
    return files[0] if files else None

def generate_audio(text: str, output_path: Path) -> bool:
    """Generate MP3 audio using edge-tts."""
    tmp_txt = output_path.with_suffix('.txt')
    tmp_txt.write_text(text, encoding='utf-8')
    
    result = subprocess.run(
        ["edge-tts", "--voice", VOICE, "--file", str(tmp_txt), "--write-media", str(output_path)],
        capture_output=True, text=True, timeout=600
    )
    tmp_txt.unlink(missing_ok=True)
    
    if result.returncode != 0:
        print(f"edge-tts error: {result.stderr}", file=sys.stderr)
        return False
    
    return output_path.exists() and output_path.stat().st_size > 0

def update_podcast_feed(audio_file: str, title: str, date: str, duration_sec: int, size_bytes: int):
    """Generate podcast RSS feed with latest episode."""
    episodes = []
    feed_path = PODCAST_DIR / "feed.xml"
    
    # Gather existing episodes from feed
    if feed_path.exists():
        existing = feed_path.read_text(encoding='utf-8')
        # Extract existing <item> blocks
        items = re.findall(r'<item>.*?</item>', existing, re.DOTALL)
        episodes = items
    
    # Build new episode
    pub_date = datetime.now().strftime("%a, %d %b %Y 09:00:00 -0300")
    episode_xml = f"""    <item>
      <title>{title}</title>
      <description>Briefing diario de tech, AI y self-hosting — {date}</description>
      <enclosure url="{SITE_URL}/podcast/{audio_file}" length="{size_bytes}" type="audio/mpeg"/>
      <guid isPermaLink="false">{date}</guid>
      <pubDate>{pub_date}</pubDate>
      <duration>{duration_sec}</duration>
    </item>"""
    
    all_episodes = [episode_xml] + [e for e in episodes if date not in e][:29]  # keep last 30
    
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
{chr(10).join(all_episodes)}
  </channel>
</rss>"""
    
    feed_path.write_text(feed_xml, encoding='utf-8')

def main():
    briefing = find_latest_briefing()
    if not briefing:
        print("No briefing found", file=sys.stderr)
        sys.exit(1)
    
    # Extract date from filename
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', briefing.name)
    date_str = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")
    
    # Check if podcast already exists for this date
    audio_filename = f"daily-{date_str}.mp3"
    audio_path = PODCAST_DIR / audio_filename
    if audio_path.exists():
        print(f"Podcast already exists: {audio_filename}")
        sys.exit(0)
    
    print(f"Processing: {briefing.name}")
    text = briefing.read_text(encoding='utf-8')
    text = clean_markdown(text)
    
    # Add intro
    intro = f"Daily, el briefing diario de tecnología e inteligencia artificial. {date_str}.\n\n"
    text = intro + text
    
    word_count = len(text.split())
    print(f"Text: {word_count} words, {len(text)} chars")
    
    # Generate audio
    print("Generating audio with edge-tts (Elena, Argentine Spanish)...")
    if not generate_audio(text, audio_path):
        print("Failed to generate audio", file=sys.stderr)
        sys.exit(1)
    
    size_mb = audio_path.stat().st_size / (1024 * 1024)
    print(f"Audio: {size_mb:.1f} MB")
    
    # Estimate duration (edge-tts ~16KB/sec for this voice)
    # Better: use ffprobe if available
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)],
            capture_output=True, text=True, timeout=10
        )
        duration = int(float(result.stdout.strip()))
    except Exception:
        duration = word_count // 3  # rough estimate: ~3 words/sec
    
    mins = duration // 60
    secs = duration % 60
    print(f"Duration: {mins}:{secs:02d}")
    
    # Update podcast feed
    title = f"Daily — {date_str}"
    update_podcast_feed(audio_filename, title, date_str, duration, audio_path.stat().st_size)
    print(f"Feed updated: podcast/feed.xml")
    print("Done!")

if __name__ == "__main__":
    main()
