#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:22:19 2022

@author: giulianaorizzonte
"""

# =============================================================================
# Big list of: word + phonetic spelling + rhyme
# Output: CSV file
# =============================================================================

# import rhyming dictionary
from rijmwoord import rijmwoordenboek

# import pandas
import pandas as pd

# import extra words as data frame, ~405,000 words + phonetic spelling
extra_words = pd.read_csv("extra_words.csv")

# add new column for rhyming
extra_words["rhyming"] = ""

# rename column
extra_words = extra_words.rename(columns={' phoneme': 'phoneme'})

# get all the rhyming patterns
rhymes = list(rijmwoordenboek.keys())

# add rhyming patterns to the extra words
length = len(extra_words.index)

for i in range(length):
    for k in rhymes:
        if extra_words.phoneme[i].endswith(k):
            extra_words.rhyming[i] = k

# export data frame to csv file
import csv

extra_words.to_csv('wordswithrhyme.csv', index = False)

# =============================================================================
# Debugging needed: the phonetic coding for some sounds is different
# between the rijmwoord.py file and the extra_words csv file
# Need to -> (i) find words with empty rhyme column, (ii) figure out
# what sound has different phonetic spelling, (iii) update the
# rijmwoordenboek with the phonetic spelling of the extra_words file,
# (iv) re-run for loop for rows with empty rhyme cell.
#
# Steps i to iii could potentially be done manually, it looks like
# there's not many sounds that are spelled differently but hard to tell when
# list is incomplete
# =============================================================================

# =============================================================================
# Big list of: rhymes + rhyming words
# Output: CSV file
# =============================================================================

# create list of rhymes
rhyme_list = []

# group all the words by rhyme
# add rhymes to the rhyme_list
for k in extra_words.groupby('rhyming'):
    rhyme_list.append(k)

# reformat to eliminate data frames inside list:
rhyme_list2 = []

for j in range(len(rhyme_list)):
    rhyme_list2.append([rhyme_list[j][0], rhyme_list[j][1].word.values.tolist()])    
# Output is a list of lists and looks like:  ['ok-t@', ['aangestookte', 'aanstookte', 'aanstookten']]

# reformat original list so it's compatible to merge
rijm_list = list(rijmwoordenboek.items())

for i in range(len(rijm_list)):
   rijm_list[i] = list(rijm_list[i]) 
   rijm_list[i][1] = list(rijm_list[i][1])
    
# merge the two lists
merged = rijm_list

for i in range(len(rijm_list)):
    for j in range(len(rhyme_list2)):
        if rijm_list[i][0] == rhyme_list2[j][0]:
            merged[i][1] = rijm_list[i][1] + rhyme_list2[j][1]
# BUT need to eliminate duplicates

# For each item in the list, reformat the second element to a tuple         
for i in range(len(merged)):
    merged[i][1] = tuple(merged[i][1])

# export to csv -> the structure is: ['sound', ('word', 'word')] ; ['sound', ('word', 'word')]

with open('rhymeswithwords.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(merged)
