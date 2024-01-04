#!/usr/bin/env python3

from nltk import pos_tag
from nltk.corpus import words
import os
from libaux import *

futhorc_runeset = ["F", "U", "1", "O", "R", "C", "G", "W", "H", "N", "I", "J", "2", "P", "X", "S", "T", "B", "E", "M", "L", "3", "4", "D", "A", "5", "Y", "6", "7"]
double_runes = ["TH", "EO", "NG", "OE", "AE", "IA|IO", "EA"]

latin_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def get_used_words(src: str) -> list:
    repo_dir, _ = os.path.split(os.getcwd())
    with open(f"{repo_dir}/data/{src}.txt", "r") as file:
        contents = file.read()
    all_words = contents.split(" ")
    return all_words

def get_used_words_by_len(src: str) -> dict:
    repo_dir, _ = os.path.split(os.getcwd())
    with open(f"{repo_dir}/data/{src}.txt", "r") as file:
        contents = file.read()
    all_words = contents.split(" ")
    word_distribution = {}
    upper_limit = max([len(word) for word in all_words])
    for i in range(upper_limit):
        word_list = []
        for word in all_words:
            if len(word) == i+1 and word not in word_list:
                word_list.append(word)
        word_distribution[f"{i+1}"] = word_list
    return word_distribution


def get_words(length: int, type_: str) -> list:
    pass

def numify_runes(word: str, exception=None, debug=False) -> str:
    ## NOTE: the exception argument has to be a list!
    assert set(word) <= set(futhorc_runeset), f"This word contains unknown runes! [[ {word} ]]"
    output = ""
    
    drune_idx = 0
    curr_idx = 0
    while curr_idx < len(word):
        if debug:
            print(f"func /numify_runes/ ;; while loop, before length validation  [[curr_idx == {curr_idx}, len(word) == {len(word)}]]")
        if curr_idx < len(word)-1:
            if word[curr_idx] == "I" and (word[curr_idx+1] == "A" or word[curr_idx+1] == "O"):
                if debug:
                    print(f"func /numify_runes/ ;; first drune switch (IA/IO check)  [[curr_idx == {curr_idx}, len(word) == {len(word)}]]")
                drune_idx += 1
                if not exception or drune_idx not in exception:
                    if debug:
                        print(f"--- [[if not exception or drune_idx not in exception]]  [[drune_idx == {drune_idx}]]")
                    output += "6"
                else:
                    output += word[curr_idx]+word[curr_idx+1]
                curr_idx += 2
                if debug:
                    print(f"func /numify_runes/ ;; Right before continuation  [[curr_idx == {curr_idx}]]")
                continue
            if word[curr_idx]+word[curr_idx+1] in double_runes:
                if debug:
                    print(f"func /numify_runes/ ;; Double-rune found! ({word[curr_idx]+word[curr_idx+1]}, at indexes {curr_idx} and {curr_idx+1})")
                drune_idx += 1
                if not exception or drune_idx not in exception:
                    if debug:
                        print(f"--- [[if not exception or drune_idx not in exception]]  [[drune_idx == {drune_idx}]]")
                    output += str(double_runes.index(word[curr_idx]+word[curr_idx+1])+1)
                else:
                    output += word[curr_idx]+word[curr_idx+1]
                curr_idx += 2
                if debug:
                    print("func /numify_runes/ ;; Right before continuation")
                continue
            output += word[curr_idx]
            curr_idx += 1
            continue
        if debug:
            print("func /numify_runes/ ;; Last character reached, final iteration of the while loop")
        output += word[curr_idx]
        curr_idx += 1
    return output


def calc_rune_len(word: str, exception=None, already_numified=False) -> int:
    improved_word = numify_runes(word, exception) if not already_numified else word
    return len(improved_word)

def calc_rune_diff(base: str, crib: str, base_exceptions=None, crib_exceptions=None, verbose=False, show_key=False, show_delta=False, show_all=False, base_numified=False, crib_numified=False, debug=False) -> list:
    improved_base, improved_crib = base, crib
    if not base_numified:
        improved_base = numify_runes(base, base_exceptions, debug)
    if not crib_numified:
        improved_crib = numify_runes(crib, crib_exceptions, debug)
    assert len(improved_base) == len(improved_crib), "The rune length of the base and the crib have to be equal!"
    
    differential = []

    if show_all:
        show_key = True
        show_delta = True

    if debug:
        print("func /calc_rune_diff/ ;; Right before differential calculation; numifications have been completed")

    for i in range(len(improved_base)):
        base_idx = futhorc_runeset.index(improved_base[i])
        crib_idx = futhorc_runeset.index(improved_crib[i])
        difference = base_idx-crib_idx
        if difference >= 0:
            differential.append(difference)
        else:
            differential.append(base_idx+len(futhorc_runeset)-crib_idx)
    if verbose:
        if not show_key and not show_delta:
            print(f"DIFF: {improved_base} ----> {improved_crib} {differential}")
        else:
            print(f"DIFF: {improved_base} ----> {improved_crib} {differential}", end=';   ')
            if show_key:
                keys = vkeygetf_diff_err(differential)
                shiftable_keys = [key for key in keys if "_" not in key]
                atbashed_keys = [rune_atbash(key) for key in shiftable_keys]
                print(f"KEY: {keys[0]} (ERRORS: {keys[1]}, {keys[2]}) ; ATBASHED KEYS: {atbashed_keys}")
                print("---SHIFTED KEYS - PLAIN")
                for i in range(len(shiftable_keys)):
                    print(f"----CURRENT KEY: {shiftable_keys[i]}")
                    for var in crune_shift(shiftable_keys[i]):
                        print(f"----- {var}")
                print("---SHIFTED KEYS - ATBASH")
                for i in range(len(atbashed_keys)):
                    print(f"----CURRENT KEY: {atbashed_keys[i]}")
                    for var in crune_shift(atbashed_keys[i]):
                        print(f"----- {var}")
            if show_delta:
                print(f"\n--DELTA: {get_ddiff(differential)}")

    return differential

def vkeygetf_diff(differential: list) -> str:
    ## Obtain a Vigenere key on the futhorc runeset with the given differential.
    key = ""
    for diff in differential:
        if diff == 0:
            key += "_"
            continue
        key += futhorc_runeset[diff-1]
    return key

def vkeygetf_diff_err(differential: list) -> list:
    ## Obtain a Vigenere key on the futhorc runeset with the given differential and an    ## absolute error of 1
    keys = ["", "", ""]
    for diff in differential:
        if diff == 0:
            keys[0] += "_"
            keys[1] += "_"
            keys[2] += "_"
            continue
        keys[0] += (futhorc_runeset[diff-1])
        keys[1] += (futhorc_runeset[diff])
        keys[2] += (futhorc_runeset[diff-2])
    return keys

def rune_atbash(chars: str, exception=None, already_numified=False) -> str:
    ## Do an atbash of the word on the futhorc runeset.
    improved_chars = numify_runes(chars, exception) if not already_numified else chars
    return ''.join([futhorc_runeset[len(futhorc_runeset)-futhorc_runeset.index(char)-1] for char in improved_chars])

def crune_shift(chars: str, exception=None, already_numified=False, n=None) -> list:
    ## Do a standard Caesar shifting of the word on the futhorc runeset. By default, this function
    ## returns all possible shifts.

    improved_chars = numify_runes(chars, exception) if not already_numified else chars
    variations = []

    if not n:
        n = len(futhorc_runeset)
    for i in range(n):
        variations.append(''.join([futhorc_runeset[(futhorc_runeset.index(char)+i)%len(futhorc_runeset)] for char in improved_chars]))
    return variations

def nlrune_shift(chars: str, differential: list, exception=None, already_numified=False) -> str:
    ## Do a non-linear shifting of the word on the futhorc runeset. The differential (the array of shifts) has to be
    ## provided.

    improved_chars = numify_runes(chars, exception) if not already_numified else chars

    variation = ""
    for i in range(len(improved_chars)):
        variation += futhorc_runeset[(futhorc_runeset.index(improved_chars[i])+differential[i%len(differential)])%len(futhorc_runeset)]
    return variation

def get_ddiff(differential: list) -> list:
    ## Calculate the delta differential of a differential (i.e. calculate the differences between the individual differential values)
    
    delta_differential = []
    for i in range(len(differential)-1):
        delta_differential.append(delta(differential[i:i+2]))
    return delta_differential



##  -- METHODS FOR DELTA-DIFFERENTIAL ANALYSIS --  ##

def ddvalidate_totient(ddifferential: list, upper_limit=20) -> tuple:
    ## Looks for the delta-differential in the delta totient sequence. This essentially determines whether some kind of progressive totient shift
    ## was used in the encryption (with any constant offset)

    if len(ddifferential) != 2:
        print("The list of delta differentials you've provided is either too long or too small. The list has to be exactly two values long.")
        return ("Error", "Error")
    lower_limit = min(ddifferential)
    delta_totient_sequence = delta_totient_range(200)
    validate_list = []
    for i in range(lower_limit):
        validate_list = [num-i for num in ddifferential]
        status, index = is_sublist(validate_list, delta_totient_sequence)
        if status:
            yield (-i, index)
    for i in range(upper_limit):
        validate_list = [num+i+1 for num in ddifferential]
        status, index = is_sublist(validate_list, delta_totient_sequence)
        if status:
            yield (i+1, index)

def ddvalidate_prime(ddifferential: list) -> tuple:
    ## Looks for the delta-differental in the delta prime sequence. It does the same kind of validation as the first method does, but on the prime sequence.
    ## On the other hand, since phi(p) = p - 1, this also checks the delta-differential on the prime totient sequence. Note that progressive shifting on the prime
    ## totient sequence HAS been used by 3301 before.

    delta_prime_sequence = delta_prime_range(10000)
    status, index = is_sublist(ddifferential, delta_prime_sequence)
    if status:
        return (0, index)


if __name__ == '__main__':
    ## RESERVED FOR TESTING :)
    pass

