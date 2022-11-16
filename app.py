import random

import rijmwoord
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/random_word')
def random_word():
    # rijmwoorden_dict = rijmwoord.rijmwoordenboek
    # random_word = random.sample(random.choice(list(rijmwoorden_dict.values())), 1)[0]
    # return random_word

    with open("wordlist.txt", "r") as f:
        random_word = random.sample(f.readlines(), 1)[0]

    return random_word


@app.route('/rhyme', methods=['POST'])
def rhyme_word():
    data = request.form["query"].lower().strip().split()

    if not data:
        return "Geen rijmwoorden gevonden!"

    word = data[0]

    try:
        rijm_embed = list(rijmwoord.rijmwoorden(word))

        if not rijm_embed:
            return "Geen rijmwoorden gevonden!"
        else:
            return "<b>" + random.choice(rijm_embed) + "</b> rijmt op " + word + "!"

    except KeyError as e:
        return "Geen rijmende woorden gevonden!"
