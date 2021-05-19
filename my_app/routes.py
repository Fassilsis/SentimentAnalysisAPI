from my_app.app import app
from my_app.sentiment_analyzer import SentimentAnalyzer
from flask import jsonify, request, make_response


@app.route('/')
def home():
    return '''
    This sentiment analysis API extracts sentiment into a specific text string. 
    Based on Natural language processing algorithm, this API classifies each sentence 
    in the input as positive, neutral, or negative.
    '''


result = {}


@app.route('/query/', methods=['GET', 'POST'])
def sentimentQuery():
    if request.method == 'POST':
        text = request.form['q']
    else:
        text = request.args.get('q')
    senti = SentimentAnalyzer.sentiment(text)
    score = SentimentAnalyzer.score(text)
    result['sentiment'] = senti
    result['score'] = score
    return jsonify(result)
