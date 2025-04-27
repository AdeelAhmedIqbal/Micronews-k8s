from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    # Call aggregator
    articles = requests.get('http://aggregator-service:8000/fetch').json()
    html = "<h1>Top Headlines</h1>"
    for article in articles[:5]:
        html += f"<h2>{article.get('title')}</h2><p>{article.get('description')}</p><hr>"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
