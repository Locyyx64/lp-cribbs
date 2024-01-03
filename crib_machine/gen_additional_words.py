#!/usr/bin/env python3

from nltk import pos_tag
from nltk.corpus import brown
import sys
import os

file_dir = os.path.dirname(__file__)
lib_dir = os.path.join(file_dir, "..", "lib")
sys.path.append(lib_dir)

from libcrib import latin_alphabet, calc_rune_len

## NOTE: Why the fuck does this take an eternity to run?

additional_words = brown.words()
print("...words acquired")
tagged = pos_tag(additional_words)
print("...words tagged")
possessive_nouns = [i for i,j in tagged if j == "NNP"]
print("...possessive nouns found")
additional_words_upd = [word for word in additional_words if word not in possessive_nouns]
print("...wordlist updated")

improved_additional_words = set([word.upper().replace("K", "C").replace("Z", "S").replace("V", "U") for word in additional_words_upd if "q" not in word and "Q" not in word and set(word) <= set(latin_alphabet)])
print("...wordlist improved to fit the futhorc runeset")

print([word for word in improved_additional_words if calc_rune_len(word) == 11])

print("Exiting...")
