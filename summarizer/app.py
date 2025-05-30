import os
from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

app = Flask(__name__)

# POST /summarize
#   { "text": "<full article content>" }
# → { "summary": "<3-sentence summary>" }
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json(force=True)
    text = data.get('text', '')
    parser     = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    # get 1 sentence
    sentences = summarizer(parser.document, 1)
    result    = ' '.join(str(s) for s in sentences)
    return jsonify({'summary': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
