"""
Read the news and classify each article.
"""

import feedparser
import yaml
from pydantic import BaseModel, Field
from openai import OpenAI
from utilities import init
import logging

class NewsArticle(BaseModel):
    title: str = Field(description="The title of the news article.")
    description: str = Field(description="The description in the RSS feed of this article.")


class Classification(BaseModel):
    stars: int = Field(description="The star rating of the article, from 1 to 5.", ge=1, le=5)
    reason: str = Field(description="The reason for the rating.")


def read_news_feeds(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data.get('news-feeds', [])


def fetch_and_parse_feed(feed_url: str):
    return feedparser.parse(feed_url)


def classify_article(article: NewsArticle, interests: list[str]) -> Classification:
    client = OpenAI()
    prompt = f"""
    As an expert software engineer, please classify the following news article based on my interests: {', '.join(interests)}.
    Give a star rating from 1 to 5, where 5 is highly relevant and 1 is not relevant at all.
    Provide a short reason for your rating. The reason should be short 1-2 sentences. The reason should not include the interests.

    Article Title: {article.title}
    Article Description: {article.description}

    Return a JSON object that conforms to this schema:
    {{ "stars": 1-5, "reason": "string" }}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that returns structured JSON in the expected format."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    classification = Classification.model_validate_json(response.choices[0].message.content)
    logging.info(f"classification {classification}")
    return classification


def main():
    interests = ["Kotlin", "Rust", "AWS"]
    news_feeds = read_news_feeds("examples/newsfeeds.yaml")
    for feed_url in news_feeds:
        feed = fetch_and_parse_feed(feed_url)
        for entry in feed.entries:
            article = NewsArticle(title=entry.title, description=entry.get("descriptionDetail") or entry.description )
            logging.debug(f"article {article}")
            classification = classify_article(article, interests)
            print(f"Article: {article.title}")
            print(f"         {article.description}")
            print(f"Rating: {classification.stars} stars")
            print(f"Reason: {classification.reason}")
            print("-" * 20)


if __name__ == "__main__":
    init(logging.WARN)
    main()
