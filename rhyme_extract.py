import pandas as pd


def get_rhyme(word):
    substring_list = list()
    vowels = [':a', ':e', ':2', ':o', 'iE', 'y9', 'uA', 'i:a', 'i:o', 'iu',
              'ui', 'uy', 'u:e', ':E', ':9', ':O', 'I', 'E', 'A', 'O', 'Y', '@', 'i', 'y', 'u', 'e', 'a', 'o']

    for vowel in vowels:
        substring = word.partition(vowel)
        substring_list.append(substring)

    final_list = list(set(substring_list))
    rhyme_end_list = list()
    for item in final_list:
        if item[2] != '':
            rhyme_end_list.append(item[1] + item[2])

    try:
        return min(rhyme_end_list, key=len)
    except ValueError:
        return None


df = pd.read_csv('wordswithrhyme.csv')
df["rhyming"] = df["phoneme"].apply(get_rhyme)
df.to_csv('new_wordswithrhyme.csv', index=False)