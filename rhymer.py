import random
from collections import defaultdict

import pandas as pd
import rijmwoord
import pyphen

# Rhyming words dicts from rijmwoord.py
rijmwoordenboek = rijmwoord.rijmwoordenboek
hulprijmwoordenboek = rijmwoord.hulprijmwoordenboek

df = pd.read_csv("new_wordswithrhyme.csv")
# Clean data by removing empty columns and making everything lowercase
df.dropna(inplace=True)
del df["phoneme"]
df['word'] = df['word'].str.lower()

# Group all rows from csv with the same rhyming column and put the words in a set
new_rijmwoordenboek = df.groupby('rhyming')['word'].apply(set).to_dict()

# Change datafram index to word column
df.set_index("word", inplace=True)
new_hulprijmwoordenboek = df.to_dict()["rhyming"]

# Merge hulprijmwoorden dict together with existing dict from rijmwoord.py
merged_hulpwoorden_dict = hulprijmwoordenboek | new_hulprijmwoordenboek

# Merge new rijmwoorden dict manually because of the sets
merged_rijmwoorden_dict = defaultdict(set)
for d in (rijmwoordenboek, new_rijmwoordenboek):
    for key, val_set in d.items():
        for val in val_set:
            merged_rijmwoorden_dict[key].add(val)


def get_all_rhyming_words(query):
    try:
        rhyming = merged_hulpwoorden_dict[query]
        rhyming_list = list(merged_rijmwoorden_dict[rhyming])

        # Prevents returning the query as rhyming word
        rhyming_list.remove(query)
        rhyming_list = [s for s in rhyming_list if query not in s]

        if rhyming_list:
            return rhyming_list
        else:
            return None
    except KeyError:
        # If word not found, try to hyphenate word and get last part
        pyphen_dict = pyphen.Pyphen(lang="nl_NL")
        for pair in pyphen_dict.iterate(query):
            last_part = pair[-1]
            try:
                rhyming = merged_hulpwoorden_dict[last_part]
                rhyming_list = list(merged_rijmwoorden_dict[rhyming])
                rhyming_list.remove(query)
                return rhyming_list

            except KeyError:
                return None

            except ValueError:
                return None
