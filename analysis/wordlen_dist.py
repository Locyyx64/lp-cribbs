#!/usr/bin/env python3

from nltk import pos_tag
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import os
import sys

script_dir = os.path.dirname(__file__)
lib_dir = os.path.join(script_dir, "..", "lib")
sys.path.append(lib_dir)

from libcrib import get_used_words

all_words = get_used_words("word_dump_lp1")
all_words_runes = [word for word in get_used_words("word_dump_lp1_runes") if word[0] != "." and word[0] != ":" and word[0] != "\n" and word[0] != "("]
upper_limit = max([len(word) for word in all_words])
upper_limit_runes = max([len(word) for word in all_words_runes])
len_distribution = {}
len_distribution_runes = {}

for i in range(upper_limit):
    num = 0
    for word in all_words:
        if len(word) == i+1:
            num += 1
    len_distribution[f"{i+1}"] = num

for i in range(upper_limit_runes):
    num = 0
    for word in all_words_runes:
        if len(word) == i+1:
            num += 1
    len_distribution_runes[f"{i+1}"] = num

# --- SEMANTIC ANALYSIS OF THE SOLVED SECTION OF THE LIBER PRIMUS (INTUS + 55.jpg + 56.jpg)

tagged = pos_tag(all_words)
freqd_full = FreqDist(all_words)
freqd_len2 = FreqDist([word for word in all_words if len(word) == 2])
len2_num = freqd_len2.N()
freqd_len3 = FreqDist([word for word in all_words if len(word) == 3])
len3_num = freqd_len3.N()

print(f"Number of runic words sampled: {len(all_words_runes)}")

print("The most common 2-letter words:")
for word, num in freqd_len2.most_common(50):
    frequency = num/len2_num
    print(f"---- {word}  --> {num} ; {frequency} ; {frequency*100}%")

print("\nThe most common 3-letter words:")
for word, num in freqd_len3.most_common(150):
    frequency = num/len3_num
    print(f"---- {word}  --> {num} ; {frequency} ; {frequency*100}%")

lexical_diversity = len(set(all_words))/len(all_words)
lexical_diversity_percentage = 100*lexical_diversity
print(f"\nLEXICAL DIVERSITY: {lexical_diversity_percentage}%")



# --- MATPLOTLIB VISUALIZATION (WORD LENGTH DISTRIBUTION) --- #

fig = plt.figure(figsize=(10, 5))
plt.bar(list(len_distribution_runes.keys()), list(len_distribution_runes.values()), color="coral", width=0.4)
plt.xlabel("Word lengths")
plt.ylabel("Total number of occasions")
plt.title("Word Length Distribution")
plt.show()

