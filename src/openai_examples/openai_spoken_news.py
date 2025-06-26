"""
Read the xml feed from https://feed.infoq.com/news/, gather all the titles and say them with speaker.
"""

import argparse
import requests
import xml.etree.ElementTree as ET
from openai import OpenAI
from utilities import init
from openai_speak import speak


def get_news_titles(url: str):
    """Fetches news titles from the InfoQ RSS feed."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        titles = []
        for item in root.findall(".//item"):
            title_element = item.find("title")
            if title_element is not None:
                titles.append(title_element.text)
        return titles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the RSS feed URL")
    args = parser.parse_args()
    init()
    client = OpenAI()
    news_titles = get_news_titles(args.url)
    if news_titles:
        print("Fetched InfoQ News Titles:")
        all_titles = ".\n".join(news_titles)
        print(all_titles)
        speak(client, all_titles, "nova")
    else:
        print("No news titles found or an error occurred.")
