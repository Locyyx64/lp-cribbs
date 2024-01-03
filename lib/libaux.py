#!/usr/bin/env python3

from sympy.ntheory.factor_ import totient
from sympy import primerange

def is_sublist(list1: list, list2: list) -> tuple:
    assert len(list1) <= len(list2), "The second list cannot be smaller than the first!"
    for i in range(len(list2)+1-len(list1)):
        if list2[i:i+len(list1)] == list1:
            return (True, i)
    return (False, None)

def delta(differential: list) -> int:
    assert len(differential) == 2, "The differential list has to be exactly two values!"
    if (differential[0] < 0 and differential[1] < 0) or (differential[0] > 0 and differential[1] > 0):
        return max([abs(differential[0]), abs(differential[1])])-min([abs(differential[0]), abs(differential[1])])
    else:
        return abs(differential[0])+abs(differential[1])

def totient_range(n: int) -> list:
    values = []
    for i in range(n):
        values.append(totient(i+1))
    return values

def prime_totient_range(n: int) -> list:
    ## Get the first n elements of the prime totient sequence
    return [num-1 for num in list(primerange(0, 15*n))[:n]]

def delta_totient_range(n: int) -> list:
    orig_values = totient_range(n)
    delta_values = []
    for i in range(n-2):
        delta_values.append(abs(orig_values[i+2]-orig_values[i+1]))
    return delta_values

def delta_prime_range(n: int) -> list:
    orig_values = list(primerange(0, n))
    delta_values = []
    for i in range(len(orig_values)-2):
        delta_values.append(orig_values[i+2]-orig_values[i+1])
    return delta_values

