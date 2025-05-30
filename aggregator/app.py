import os
import requests
from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
from newspaper import Article
from newspaper.article import ArticleException

app = Flask(__name__)

# Load the NewsAPI key and MongoDB URI from environment variables
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
MONGO_URI = os.getenv('MONGO_URI')

# Connect to the MongoDB database
client = MongoClient(MONGO_URI)
db = client.get_default_database()

def get_full_text(url: str) -> str:
    """
    Try to scrape the full article text with newspaper3k.
    If it fails (for example, a paywall or network error), log a warning
    and return an empty string so we can fallback gracefully.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except ArticleException as e:
        app.logger.warning(f"Could not scrape full text ({e}) for URL: {url}")
        return ''

@app.route('/fetch', methods=['GET'])
def fetch_articles():
    """
    Fetch the latest headlines from NewsAPI, attempt to scrape each
    article’s full text, and store everything in MongoDB. If scraping
    doesn’t work, fall back to the short snippet provided by NewsAPI.
    """
    response = requests.get(
        f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    )
    items = response.json().get('articles', [])

    results = []
    for item in items:
        url = item.get('url')
        # get the full article text or use the snippet if scraping failed
        full_text = get_full_text(url) if url else ''
        snippet = item.get('content', '') or ''
        content = full_text or snippet

        record = {
            'url':         url,
            'title':       item.get('title', ''),
            'content':     content,
            'publishedAt': item.get('publishedAt'),
            'fetchedAt':   datetime.utcnow()
        }

        # store the article without creating duplicates
        db.articles.update_one(
            {'url': url},
            {'$setOnInsert': record},
            upsert=True
        )

        results.append(record)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
