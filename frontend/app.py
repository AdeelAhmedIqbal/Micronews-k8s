import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

AGG_URL  = os.getenv('AGG_SERVICE_URL',   'http://aggregator-service:8000')
SUMM_URL = os.getenv('SUMM_SERVICE_URL',   'http://summarizer-service:8001')

@app.route('/')
def homepage():
    # 1) pull all stored articles
    articles = requests.get(f'{AGG_URL}/fetch').json()
    return render_template('index.html', articles=articles)

@app.route('/summarize')
def summarize_article():
    # 2) find the one you clicked
    url = request.args.get('url')
    # pull content for that URL
    articles = requests.get(f'{AGG_URL}/fetch').json()
    art = next((a for a in articles if a['url']==url), None)

    summary = ''
    if art and art.get('content'):
        # 3) POST the full content to summarizer
        resp = requests.post(
            f'{SUMM_URL}/summarize',
            json={'text': art['content']}
        )
        summary = resp.json().get('summary','')

    return render_template('detail.html', article=art, summary=summary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
