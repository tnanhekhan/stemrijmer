import random
from collections import defaultdict

import pandas as pd
import rijmwoord
import pyphen

# Rhyming words dicts from rijmwoord.py
rijmwoordenboek = rijmwoord.rijmwoordenboek
hulprijmwoordenboek = rijmwoord.hulprijmwoordenboek

df = pd.read_csv("wordswithrhyme.csv")
# Clean data by removing empty columns and making everything lowercase
df.dropna(inplace=True)
del df["phoneme"]
df['word'] = df['word'].str.lower()

# Group all rows from csv with the same rhyming column and put the words in a set
new_rijmwoordenboek = df.groupby('rhyming')['word'].apply(set).to_dict()

df.set_index("word", inplace=True)
new_hulprijmwoordenboek = df.to_dict()["rhyming"]

merged_hulpwoorden_dict = hulprijmwoordenboek | new_hulprijmwoordenboek
merged_rijmwoorden_dict = defaultdict(set)

for d in (rijmwoordenboek, new_rijmwoordenboek):
    for key, val_set in d.items():
        for val in val_set:
            merged_rijmwoorden_dict[key].add(val)


def get_rhyming_word(query):
    try:
        rhyming = merged_hulpwoorden_dict[query]
        rhyming_results = list(merged_rijmwoorden_dict[rhyming])
        return random.choice(rhyming_results)
    except KeyError:
        # If word not found, try to hyphenate word and get last part
        pyphen_dict = pyphen.Pyphen(lang="nl_NL")
        for pair in pyphen_dict.iterate(query):
            last_part = pair[-1]
            try:
                rhyming = merged_hulpwoorden_dict[last_part]
                rhyming_results = list(merged_rijmwoorden_dict[rhyming])
                return random.choice(rhyming_results)

            except KeyError:
                return None


def get_all_rhyming_words(query):
    try:
        rhyming = merged_hulpwoorden_dict[query]
        return list(merged_rijmwoorden_dict[rhyming])
    except KeyError:
        # If word not found, try to hyphenate word and get last part
        pyphen_dict = pyphen.Pyphen(lang="nl_NL")
        for pair in pyphen_dict.iterate(query):
            last_part = pair[-1]
            try:
                rhyming = merged_hulpwoorden_dict[last_part]
                return list(merged_rijmwoorden_dict[rhyming])

            except KeyError:
                return None
