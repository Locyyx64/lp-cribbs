#!/usr/bin/env python3

import sys
import os
import re

file_dir = os.path.dirname(__file__)
lib_dir = os.path.join(file_dir, "..", "lib")
sys.path.append(lib_dir)

from libcrib import *


word_distribution = get_used_words_by_len("word_dump_lp1")
all_words_runes = get_used_words("lp_unsolved/1")

# --- CRIBBING --- # Next step: DIFFERENTIAL ANALYSIS  (INSPECTION OF DELTA DIFFERENTIALS, EVENTUAL PATTERN RECOGNITION)

def get_crib_candidates_text(max_len: int, additional_words=False) -> dict:
    crib_candidates_text = {}
    for i in range(max_len):
        word_list = []
        for key in word_distribution.keys():
            for crib in word_distribution[key]:
                crib = crib.replace('\n', '')
                if "'" not in crib and calc_rune_len(crib) == i+1:
                    word_list.append(crib)
        crib_candidates_text[f"{i+1}"] = word_list
    if additional_words:
        ## NOTE: add dynamic dictionary creation
        with open("./additional_words/11.txt", "r") as file:
            crib_candidates_text["11"] += [word.replace('\n', '') for word in file.read().split()]
    return crib_candidates_text

def get_all_crib_targets(words: list, limited=True, limit=10, already_numified=True):
    words_parsed = [word for word in words if word[0] != "." and word[0] != "\n"]
    if not limited:
        words_parsed_pref = words_parsed
    else:
        words_parsed_pref = words_parsed[:limit]
    if not already_numified:
        words_parsed_pref = [numify_runes(word) for word in words_parsed_pref]
    yield words_parsed_pref

    ## CIPHERED VERSIONS
    words_var1 = [rune_atbash(word, already_numified=already_numified) for word in words_parsed_pref]
    words_var2 = [crune_shift(word, already_numified=already_numified) for word in words_parsed_pref]
    words_var3 = [[rune_atbash(word, already_numified=already_numified) for word in offset_var] for offset_var in words_var2]
    words_var4 = [crune_shift(word, already_numified=already_numified) for word in words_var1]

    yield [words_var1, words_var2, words_var3, words_var4]

    # NOTE: Other variations to add: non-linear shift (Vigenere, Beaufort), Quagmire-like ciphers, Bifid, Playfair, Nihilist, Affine, etc.


if __name__ == '__main__':
    ## RESERVED FOR TESTING
    pass
