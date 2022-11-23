import random

from flask import request, render_template, Flask

import rhymer
import rijmwoord

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app')
def app_index():
    return "HELLO WORLD"


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
        rijm_embed = rhymer.get_all_rhyming_words(word);

        if not rijm_embed:
            return "Ik weet niet wat rijmt op " + word + "."
        else:
            return random.choice(rijm_embed) + " rijmt op " + word + "! "

    except KeyError as e:
        return "Ik weet niet wat rijmt op " + word + "."
