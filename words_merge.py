#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:43:47 2022

@author: giulianaorizzonte

Code is ugly, inefficient and needs debugging. It works for now.
"""

# import existing words
from rijmwoord import rijmwoordenboek

# import additional words
import pandas as pd

extra_words = pd.read_csv("extra_words.csv")
extra_words

extra_words["rhyming"] = ""

extra_words = extra_words.rename(columns={' phoneme': 'phoneme'})

# get all the rhyming patterns
rhymes = list(rijmwoordenboek.keys())
print(rhymes)

# add rhyming patterns to the extra words
length = len(extra_words.index)
i = 0

for i in range(length):
    for k in rhymes:
        if extra_words.phoneme[i].endswith(k):
            extra_words.rhyming[i] = k

# make list of rhymes

rhyme_list = []

test_words = extra_words[0:1900]

for k in test_words.groupby('rhyming'):
    rhyme_list.append(k)

# Output is a list of tuples and looks like
# ('i-j@r',
#                      word                   phoneme rhyming
#  72  A-parlementari&euml;r  'a-pAr-l@-mEn-'ta-ri-j@r   i-j@r)

# Alternative output:
    
rhyme_list2 = []

for j in range(len(rhyme_list)):
    rhyme_list2.append([rhyme_list[j][0], rhyme_list[j][1].word.values.tolist()])
    
rhyme_dict = {item[0]: item[1] for item in rhyme_list2}
    
# Output is a list of lists and looks like:  ['ok-t@', ['aangestookte', 'aanstookte', 'aanstookten']]

# reformat original list
rijm_list = list(rijmwoordenboek.items())

for i in range(len(rijm_list)):
   rijm_list[i] = list(rijm_list[i]) 
   rijm_list[i][1] = list(rijm_list[i][1])
    
# =============================================================================
# ignore this
# from collections import defaultdict
# 
# d1 = {1: [2], 3: [4]}
# d2 = {1: [6, 1], 3: [7, 4]}
# 
# dd = defaultdict(list)
# 
# for d in (d1, d2): # you can list as many input dicts as you want here
#     for key, value in d.items():
#         dd[key].append(value)
#     
# print(dd) # result: defaultdict(<type 'list'>, {1: [2, 6], 3: [4, 7]})
# 
# import csv
# with open('testttt.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(dd)
# =============================================================================

# merged the two lists

#testing
test_rijm = rijm_list[0:10]
test_rhyme = rhyme_list2[258:265]

merged = test_rijm

for i in range(len(test_rijm)):
    for j in range(len(test_rhyme)):
        if test_rijm[i][0] == test_rhyme[j][0]:
            merged[i][1] = test_rijm[i][1] + test_rhyme[j][1]
            
for i in range(len(merged)):
    merged[i][1] = tuple(merged[i][1])

# =============================================================================
# need to eliminate duplicates
# =============================================================================

# export to csv -> the structure is: ['sound', ('word', 'word')] ; ['sound', ('word', 'word')]

#testing
import csv
with open('mergedtest.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(merged)
    
# =============================================================================
# why is the first element in the csv in quotes?
# =============================================================================

