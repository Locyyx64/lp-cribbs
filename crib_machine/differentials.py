#!/usr/bin/env python3

import sys
import os

file_dir = os.path.dirname(__file__)
lib_dir = os.path.join(file_dir, "..", "lib")
sys.path.append(lib_dir)

from libcrib import *
from crib_base import *


crib_candidates_text = get_crib_candidates_text(max_length)

print("PLAIN CRIB TARGETS -------------------|")
for target in crib_targets_limited:
    for word in crib_candidates_text[str(calc_rune_len(target, already_numified=True))]:
        calc_rune_diff(target, word, verbose=True, show_all=True, base_numified=True)

print("\n\nATBASHED CRIB TARGETS ---------------|\n")
for target in cribt_var1:
    for word in crib_candidates_text[str(calc_rune_len(target, already_numified=True))]:
        calc_rune_diff(target, word, verbose=True, show_all=True, base_numified=True)


