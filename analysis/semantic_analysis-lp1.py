#!/usr/bin/env python3


from math import floor
import matplotlib.pyplot as plt
import os
import sys

script_dir = os.path.dirname(__file__)
lib_dir = os.path.join(script_dir, "..", "lib")
sys.path.append(lib_dir)

from libcrib import get_used_words

all_words = [word for word in get_used_words("lp_unsolved/1") if word[0] != "."]
upper_limit = max([len(word) for word in all_words])
len_distribution = {}

for i in range(upper_limit):
    num = 0
    for word in all_words:
        if len(word) == i+1:
            num += 1
    len_distribution[f"{i+1}"] = num

# --- SEMANTIC ANALYSIS OF THE FIRST SECTION OF THE UNSOLVED LIBER PRIMUS --- #
lexical_diversity_solved = 0.3562585969738652

words_num = len(all_words)

print(f"Number of sampled words: {words_num}")

approximate_new_words = floor(words_num*lexical_diversity_solved) 
print(f"\nGiven the lexical diversity of the solved section, we can approximately expect {approximate_new_words} total new words (not distinct) and {words_num-approximate_new_words} used words.")



# --- PLOTTING THE WORD LENGTH DISTRIBUTION IN MATPLOTLIB --- #
fig = plt.figure(figsize=(15,10))
plt.bar(list(len_distribution.keys()), list(len_distribution.values()), color="blue", width=0.4)
plt.xlabel("Word lengths")
plt.ylabel("Total number of occasions")
plt.title("Word Length Distribution")
plt.show()
