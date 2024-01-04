#!/usr/bin/env python3

import sys
import os

file_dir = os.path.dirname(__file__)
lib_dir = os.path.join(file_dir, "..", "lib")
sys.path.append(lib_dir)

from libcrib import *
from crib_base import *

crib_targets = list(get_all_crib_targets(all_words_runes))
crib_targets_plain = crib_targets[0]
crib_targets_ciphered = crib_targets[1]

max_length = max([len(word) for word in crib_targets_plain])
crib_candidates_text = get_crib_candidates_text(max_length)

print("PLAIN CRIB TARGETS -------------------|")
for target in crib_targets_plain:
    for word in crib_candidates_text[str(calc_rune_len(target, already_numified=True))]:
        calc_rune_diff(target, word, verbose=True, show_all=True, base_numified=True)

print("\n\nATBASHED CRIB TARGETS ---------------|\n")
for target in crib_targets_ciphered[0]:
    for word in crib_candidates_text[str(calc_rune_len(target, already_numified=True))]:
        calc_rune_diff(target, word, verbose=True, show_all=True, base_numified=True)


