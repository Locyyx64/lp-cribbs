#!/usr/bin/env python3

import sys
import os

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


crib_targets = [word for word in all_words_runes if word[0] != "." and word[0] != "\n"]
crib_targets_limited = crib_targets[:10]
crib_targets_indexed = enumerate(crib_targets)

max_length = max([len(word) for word in crib_targets])

 ## - CIPHERED VARIATIONS OF THE CRIB TARGETS - ##

cribt_var1 = [rune_atbash(word) for word in crib_targets_limited]
cribt_var2 = [crune_shift(word) for word in crib_targets_limited]
cribt_var3 = [[rune_atbash(word) for word in offset_var] for offset_var in cribt_var2]
cribt_var4 = [crune_shift(word) for word in cribt_var1]

# NOTE: Other variations to add: non-linear shift (Vigenere, Beaufort), Quagmire-like ciphers, Bifid, Playfair, Nihilist, Affine, etc.
