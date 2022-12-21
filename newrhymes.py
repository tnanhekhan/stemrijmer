#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:04:35 2022

@author: giulianaorizzonte
"""

# import pandas and numpy
import pandas as pd
import numpy as np

# import BAK list to obtain rhymes
bak_rhymes = pd.read_csv("BAKrhyme copy.csv")

# Select column that has rhymes
bak_rhymes = bak_rhymes[0:447]
# Change data type to list
rhymes = bak_rhymes['rhyme'].tolist()
# Keep only unique values
rhymes = list(set(rhymes))
# Eliminate the 1 nan value
rhymes = rhymes[1:]

# Import BAK list to add rhymes
bak_empty = pd.read_csv("BAKrhyme copy.csv")
# Make the rhyme column empty (because most are wrong)
bak_empty['rhyme'] = np.nan
# Remove rows with nan values in the phoneme column
bak_na = bak_empty.dropna(subset=['phoneme'])
# Eliminate duplicate words in the BAK list
bak_na.drop_duplicates(subset='Nederlands', keep='first', inplace=True)

# Loops to add rhymes from the rhymes list to the bak_na dataframe
for i, row in bak_na.iterrows():
       
    # Get the phoneme string for the current row
    phoneme = row['phoneme']
    
    # Initialize an empty list to store the matching rhymes
    matching_rhymes = []
    
    # Loop through each string in rhyme_list
    for rhyme in rhymes:
        # Check if the phoneme string ends with the rhyme string
        if phoneme.endswith(rhyme):
            # If it does, add the rhyme to the list of matching rhymes
            matching_rhymes.append(rhyme)
            
    # Add all the matching rhymes to the dataframe
    bak_na.at[i, 'rhyme'] = matching_rhymes

# Get random elements to add some of the missing rhymes
missing_rh = bak_na.sample(n=100)

# More rhymes to add to list
new_rhymes = ['ot-j@', 'ex', 'Elt', 'Op-t@r', 'Y+-t@', 'En', 'aj',
              'Ok', 'E-N@', 'ojt', 'ol', 'Y+s-t@-r@', 'An', 'A-s@',
              'A+-d@', 'Ant', 'ap', 'yrt', 'el', 'E+-f@r', 'e-r@',
              'Olf', 'Et', 'On', 'al', 'up', 'e-v@x', 'u-d@r', 
              'ar-d@', 'ats', 'Ast', 'o-p@', 'ot', 'Ip', 'e-z@']

rhymes = rhymes + new_rhymes

# repeat: keep only unique values
# repeat: loop
# repeat: get random elements

new_rhymes2 = ['a-z@', '2-r@', 'art', 'Ers-j@', 'A-N@', 'I-k@', 'i-z@'
               'Ot', 'Olkt', 'o-m@r', 'Ent', 'A-k@', 'a-m@', 'u-n@', 'Ots',
               'ur', 'e-k@', 'Ek', 'at', 'e-G@n-d@', 'IN-k@', 'st@x', 'ir'
               'Est', 'Er', 'Omp', 'ew', 'IN-k@r', 'ANs', 'u-m@', 'a-G@r',
               'a-G@', 'a-m@r', 'E+-p@', 'as', 'i-G@l', 'Ix-t@x', 'Y+-k@', 'o-l@k']

rhymes = rhymes + new_rhymes2

# repeat: keep only unique values
# repeat: loop
# repeat: get random elements

new_rhymes3 = ['e-G@', 'A~', 'I-t@', 'o-ni', 'on', 'I-n@', 'Elp', 'E-t@', 'O-p@',
               'Y+st', 'Ap', 'ENk', 'A-t@', 'O-m@', 'O-t@', 'An-d@r', 'E-t@r', 'A-p@x',
               'er-t@x', 'a-k@', 'a', 'o-Z@', 'yw', 'yr', 'In', 'e-z@x', 'on', 'i-d@',
               'Ol', 'El', 'ep', 'e-GIN', 'op', 'Ys-t@', 'O:-z@', 'alt', 'ens', 'El-p@',
               'uts', 'E+-d@', 'O-t@', 'o-v@', 'A-p@l', 'o-ni', 'i-wi']

rhymes = rhymes + new_rhymes3

# repeat: keep only unique values
# repeat: loop

new_rhymes4 = ['Ynt', 'Yx', 'E+st', 'Yrt', 'Ajnt', '2rt', 'Y+-v@', 'E+n-d@', 'Yx-t@',
              'w@', '2-z@', 'E+-z@', 'A+-z@', 'z@', 'Y+-x@', 'A+-w@', 'Y+-z@', 'E+-v@',
              'Y+-G@', 'Y-d@', 'Y+-v@', 'E+s-j@', 'E+st-j@', 'Ys-j@', 'Y-k@', 'E+-l@',
              'Y+-l@', 'lY-k@', 'Y+t-j@', 'E+t-j@', 'Yr-v@', 'A+w-tj@', 'Yr-k@', 'A+-w@',
              'E+-k@', 'A+t-j@', '2-k@', 'E+-m@', 'Y-l@', 'E+-n@', '@-l@', 'Ylp-j@',
              'E+-n@', 'Y-f@', 'Y-s@', 'E+-t@', 'j@', 'Yk-j@', '2-n@', 'A-J@', 'Y-d@']

rhymes = rhymes + new_rhymes4

# repeat: keep only unique values
# repeat: loop

new_rhymes5 = ['Y-p@l', 'E+-k@l', 'Y-f@l', '2-G@l', 'E+f-t@x', 'Yl-z@x', 'e-d@', 'Er-k@',
               'Al', 'Alf', 'Alk', 'Alm', 'Als', 'Er-t@', 'Er-v@', 'Yk', 'Er-d@r', 'Erk',
               'Erp', 'Ers', 'Erst', 'Ert', 'Erx', 'om', 'Es', 'Es-t@', 'Es-tIk', 'Esp',
               'Est', 'Et-j@s', 'Ark', 'ir', 'Ex-t@r', 'Ext', 'I-N@-r@', 'I-N@r', 'I-b@-r@',
               'I-b@-r@x', 'I-d@', 'I-d@-l@k', 'I-d@r', 'e-t@', 'Axs', 'I-k@r', 'I-k@-r@']

rhymes = rhymes + new_rhymes5

# repeat: keep only unique values
# repeat: loop

new_rhymes6 = ['E+-s@', 'Y+-m@', 'Y+-d@', 'Y+-p@', 'Y-n@', 'A:-s@', 'A+-t@-r@', 'Yl-d@-r@',
               'Y-t@-r@', 'e-v@n', '2-t@r', 'A+-t@r', 'E+-t@r', 'E+s-t@r', 'A+-d@r', 
               'E+-v@r', 'E+-z@r', 'A+-d@r', 'E+-p@r', 'Ys-t@r', 'Y+-k@r', 'E+-G@r',
               'Y+-j@r', 'Y-m@r', 'Y+-G@r', 'A+-d@rs', 'A', '@-nIs', 'A-N@r', 'A-d@-r@',
               'ul', 'A-d@r', 'A-f@', 'A-k@-l@k', 'A-k@r', 'A-l@s', 'A-l@x', 'A-m@',
               'A-m@-r@', 'A-m@r', 'A-p@-r@', 'us', 'A-p@r', 'A-sIN', 'A-so', 'A-t@x',
               'A-x@', 'A-x@l', 'AN', 'AN-k@', 'am', 'ANk', 'ANkt', 'ANst', 'I-p@',
               'On-d@', 'e-k@-n@', 'IN', 'Or-st@l', 'Aft', 'Aj', 'Ak-s@l', 'Ak-si',
               'Ak-tOr', 'Akt', 'Al-t@', 'Al-v@', 'Is', 'Am', 'Am-p@', 'Am-po', 'Am-st@r',
               'Amp', 'An-d@', 'An-d@-r@', 'An-d@rs', 'An-d@x', 'An-s@', 'An-si',
               'An-t@', 'Arts', 'Ans', 'Orm', 'or-d@', 'ort', 'Ants', 'Ap-st@r', 'Ar',
               'juw', 'Ar-k@', 'es', 'Ar-t@-l@k', 'Arkt', 'Arm', 'Arm-t@', 'Ars', 'Art',
               'As-k@r', 'i-n@', 'I-d@l', 'As-t@x', 'is', 'o-r@', 'Ax-t@', 'Ax-t@r',
               'Ixt', 'am', 'Ax-t@x', 'Axt', 'i', 'E-N@l', 'E-b@-r@x', 'E-d@', 'E-k@',
               'ef', '@l', 'Om', 'Oms', 'On-d@', 'On-d@r', 'Ons', 'Ont', 'Orm', 'Ork',
               'Orp', 'Orst', 'Ort', 'Os', 'Ost', 'Ot', 'Ox', 'Oxt', 'a-Z@', 'a-p@',
               'a-d@', 'a-d@r', 'a-d@l', 'a-d@m', 'a-r@', 'a-ri', 'a-t@', 'a-t@r', 'a-v@',
               'a-v@l', 'Ont', 'Onts', 'ak', 'am', 'ar-d@x', 'ars', 'ast', 'ax', 'e-G@l',
               'e-k@-n@', 'e-k@l', 'e-k@r', 'e-m@', 'e-t@l', 'e-t@r', 'e-v@', 'ef', 'eft'
               ]

rhymes = rhymes + new_rhymes6

# repeat: keep only unique values
# repeat: loop

new_rhymes7 = ['E-k@r', 'E-k@rs', 'E-l@x', 'E-m@', 'E-m@r', 'E-n@', 'E-n@s', 'E-p@',
               'E-t@-r@', 'o', 'EN', 'EN-k@', 'EN-k@r', 'EN-t@', 'Ef-t@x', 'Eks',
               'Ekt', 'El-d@', 'El-d@r', 'El-d@x', 'El-k@ns', 'El-t@', 'Elf', 'Elfs',
               'Elft', 'Elk', 'Elm', 'Elv-d@', 'Em', 'Em-b@r', 'Emt', 'En-d@', 'En-d@r',
               'En-t@', 'Ens', 'Ep', 'Er-G@ns', 'Er-d@', 'Er-m@', 'Erf', 'Erfst',
               'Et-s@', 'Ex-t@', 'Exts', 'I-k@t', 'I-m@', 'I-m@-r@', 'I-n@-k@',
               'I-n@x', 'Ift', 'I-p@r', 'I-s@', 'INk', 'INks', 'I-s@-l@k', 'Ik', 'Iks',
               'Ikt', 'Il', 'Il-d@r', 'Il-v@r', 'Ilm', 'Ilt', 'Im', 'Im-p@r', 'In-d@',
               'In-d@r', 'In-st@', 'Ins', 'In-t@r', 'Inst', 'Int', 'Ips', 'Is-t@-r@',
               'Ist', 'It', 'Its', 'Ix', 'Ix-t@r', 'Ixtst', 'u-k@', 'i-t@', 'In-d@',
               'Ors', 'Or-t@', '@rt', 'O-N@', 'O-N@r', 'O-d@r', 'O-f@', 'O-f@r',
               'O-m@r', 'O-n@x', 'O-r@', 'O-p@-r@', 'O-t@-r@', 'O-t@x', 'ON', 'Oj',
               'Ok-s@', 'Ok-t@r', 'Oks', 'Ol-G@ns', 'Ol-d@r', 'Or-d@', 'Om-p@',
               'On-d@-r@', 'On-d@rt', 'On-st@r', 'Or', 'Or-G@ns', 'Or-d@', 'Or-s@',
               'Or-t@', 'Ors', 'Orxt', 'its', 'Os-t@', 'Ot-s@', 'e-v@r', 'e-z@m',
               'ek', 'els', 'em-d@', 'emt', 'en', 'ent', 'er-l@k', 'es-t@r', 'et',
               'i-p@', 'i-r@', 'i-t@', 'i-t@r', 'i-p@r', 'i-v@r', 'i-v@rt', 'if',
               'ik', 'il', 'im', 'int', 'ip', 'it-j@s', 'its', 'iw', 'iws', 'iwt',
               'ix', 'o', 'o-b@r', 'o-d@m', 'o-k@', 'o-n@', 'o-t@', 'o-t@r', 'o-tOr',
               'o-to', 'of', 'oft', 'oj', 'ok', 'or', 'elt', 'orts', 'os', 'ox',
               'u-k@', 'u-p@', 'u-r@', 'u-t@', 'u-t@r', 'u-v@', 'u-v@r', 'uS', 'uf',
               'uft', 'uj', 'um', 'ust', 'ux', 'y', 'y-r@']

rhymes = rhymes + new_rhymes7

# repeat: keep only unique values
# repeat: loop

new_rhymes7 = ['E-k@r', 'E-k@rs', 'E-l@x', 'E-m@', 'E-m@r', 'E-n@', 'E-n@s', 'E-p@',
               'E-t@-r@', 'o', 'EN', 'EN-k@', 'EN-k@r', 'EN-t@', 'Ef-t@x', 'Eks',
               'Ekt', 'El-d@', 'El-d@r', 'El-d@x', 'El-k@ns', 'El-t@', 'Elf', 'Elfs',
               'Elft', 'Elk', 'Elm', 'Elv-d@', 'Em', 'Em-b@r', 'Emt', 'En-d@', 'En-d@r',
               'En-t@', 'Ens', 'Ep', 'Er-G@ns', 'Er-d@', 'Er-m@', 'Erf', 'Erfst',
               'Et-s@', 'Ex-t@', 'Exts', 'I-k@t', 'I-m@', 'I-m@-r@', 'I-n@-k@',
               'I-n@x', 'Ift', 'I-p@r', 'I-s@', 'INk', 'INks', 'I-s@-l@k', 'Ik', 'Iks',
               'Ikt', 'Il', 'Il-d@r', 'Il-v@r', 'Ilm', 'Ilt', 'Im', 'Im-p@r', 'In-d@',
               'In-d@r', 'In-st@', 'Ins', 'In-t@r', 'Inst', 'Int', 'Ips', 'Is-t@-r@',
               'Ist', 'It', 'Its', 'Ix', 'Ix-t@r', 'Ixtst', 'u-k@', 'i-t@', 'In-d@',
               'Ors', 'Or-t@', '@rt', 'O-N@', 'O-N@r', 'O-d@r', 'O-f@', 'O-f@r',
               'O-m@r', 'O-n@x', 'O-r@', 'O-p@-r@', 'O-t@-r@', 'O-t@x', 'ON', 'Oj',
               'Ok-s@', 'Ok-t@r', 'Oks', 'Ol-G@ns', 'Ol-d@r', 'Or-d@', 'Om-p@',
               'On-d@-r@', 'On-d@rt', 'On-st@r', 'Or', 'Or-G@ns', 'Or-d@', 'Or-s@',
               'Or-t@', 'Ors', 'Orxt', 'its', 'Os-t@', 'Ot-s@', 'e-v@r', 'e-z@m',
               'ek', 'els', 'em-d@', 'emt', 'en', 'ent', 'er-l@k', 'es-t@r', 'et',
               'i-p@', 'i-r@', 'i-t@', 'i-t@r', 'i-p@r', 'i-v@r', 'i-v@rt', 'if',
               'ik', 'il', 'im', 'int', 'ip', 'it-j@s', 'its', 'iw', 'iws', 'iwt',
               'ix', 'o', 'o-b@r', 'o-d@m', 'o-k@', 'o-n@', 'o-t@', 'o-t@r', 'o-tOr',
               'o-to', 'of', 'oft', 'oj', 'ok', 'or', 'elt', 'orts', 'os', 'ox',
               'u-k@', 'u-p@', 'u-r@', 'u-t@', 'u-t@r', 'u-v@', 'u-v@r', 'uS', 'uf',
               'uft', 'uj', 'um', 'ust', 'ux', 'y', 'y-r@']

rhymes = rhymes + new_rhymes7

# repeat: keep only unique values
# repeat: loop

new_rhymes8 = ['O-k@', 'E:-s@', 'Ik-s@m', 'In-t@x', 'Olk', 'On-d@r-l@k', 'O-s@',
               'Or-d@x', 'Ox-t@r', 'o-d@', 'a-d@-l@k', 'a-d@-m@', 'a-k@-l@k',
               'a-l@x', 'a-m@-l@k', 'a-r@x', 'a-t@-r@', 'O-k@', 'Omst', 'ant',
               'ar-l@k', 'at-s@', 'at-st@', 'atst', 'e-d@x', 'e-l@k', 'o-p@r',
               'e-n@', 'e-n@x', 'e-r@lt', 'orn', 'em', 'er-d@r', 'er-st@', 'erst',
               'es-t@', 'i-G@r', 'i-d@r', 'i-k@m', 'i-l@x', 'i-r@x', 'i-s@', 'i-t@x',
               'iN-k@', 'ifst', 'ift', 'E-n@r', 'ir-d@', 'it-s@', 'o-r@x', 'orn',
               'u-G@r', 'u-S@', 'u-l@ns', 'u-v@x', 'uj-l@k', 'uj-t@', 'umt',
               'un-t@', 'us-t@', 'ut-s@', 'y-p@r', 'yr-d@r', 'yr-l@k', 'yt',
               'os-t@', 'r@x', 'o-p@x', 'O-N@-r@x', 'ON-k@r-d@r', 'ON-k@rst',
               'e-s@-l@k', 'ert', 'i-z@-l@x', 'in-d@-l@k', 'o-G@-l@k', 'o-p@-n@',
              ' o-v@-r@', 'os-t@', 'u-f@-n@', 'o-v@-r@']

rhymes = rhymes + new_rhymes8

# repeat: keep only unique values
# repeat: loop

# The previous loop stores a list of rhymes in the column rhyme where more than
# one value can be appended. The true_rhyme column store the one correct rhyme,
# which is the longest one of the two.

# create a new column to find the one true rhyme
bak_na['true_rhyme'] = ""

# iterate through each row
for index, row in bak_na.iterrows():
  # if the length of the list in the 'rhymes' column is greater than 1
  if len(row['rhyme']) > 1:
    # find the longest element in the list
    longest_rhyme = max(row['rhyme'], key=len)
    # update the value in the 'longest_rhyme' column
    bak_na.at[index, 'true_rhyme'] = longest_rhyme
  # if the length of the list in the 'rhymes' column is 1 or 0
  else:
    # update the value in the 'longest_rhyme' column with the only element in the list
    bak_na.at[index, 'true_rhyme'] = row['rhyme'][0]







