"""
Read the xml feed from an RSS feed, gather all the titles and say them with speaker.
"""

import argparse
import requests
import xml.etree.ElementTree as ET
from openai import OpenAI
from utilities import init
from openai_speak import speak

MAX_TTS_INPUT_SIZE = 4096


def get_news_titles(url: str) -> list[str]:
    """Fetches news titles from an RSS feed."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        titles = []
        for item in root.findall(".//item"):
            title_element = item.find("title")
            if title_element is not None and title_element.text:
                titles.append(title_element.text.strip())
        return titles
    except (requests.exceptions.RequestException, ET.ParseError) as e:
        print(f"Error fetching or parsing RSS feed: {e}")
        return []


def speak_news_titles(client: OpenAI, news_titles: list[str], voice: str):
    """Speaks news titles, chunking them to respect TTS API limits."""
    current_chunk = ""
    for title in news_titles:
        if len(title) > MAX_TTS_INPUT_SIZE:
            print(
                f"Warning: Skipping title longer than {MAX_TTS_INPUT_SIZE} characters: {title[:100]}..."
            )
            continue

        title_with_separator = title + ".\n"
        if (
            len(current_chunk) + len(title_with_separator) > MAX_TTS_INPUT_SIZE
            and current_chunk
        ):
            speak(client, current_chunk, voice)
            current_chunk = title_with_separator
        else:
            current_chunk += title_with_separator
    if current_chunk:
        speak(client, current_chunk, voice)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Reads news titles from an RSS feed aloud."
    )
    parser.add_argument(
        "url",
        nargs="?",
        default="https://feed.infoq.com/news/",
        help="the RSS feed URL (default: %(default)s)",
    )
    parser.add_argument(
        "--voice",
        default="nova",
        choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
        help="the voice to use for TTS (default: %(default)s)",
    )
    args = parser.parse_args()
    init()
    client = OpenAI()
    news_titles = get_news_titles(args.url)
    if news_titles:
        print("Fetched News Titles:")
        for title in news_titles:
            print(f"- {title}")
        speak_news_titles(client, news_titles, args.voice)
    else:
        print("No news titles found or an error occurred.")
