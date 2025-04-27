import requests
from flask import Flask, jsonify
import os

app = Flask(__name__)
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

@app.route('/fetch', methods=['GET'])
def fetch_articles():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return jsonify(articles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
