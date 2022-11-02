import json

import rijmwoord

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/rhyme', methods=['POST'])
def rhyme_word():
    data = request.form["query"].lower().strip().split()
    word = data[0]

    try:
        rijm_embed = rijmwoord.rijmwoorden(word)
        return json.dumps(list(rijm_embed))
    except KeyError as e:
        print(e)
        return "Geen rijmende woorden gevonden!"


if __name__ == '__main__':
    app.run()
