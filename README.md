# lp-cribbs
## Purpose

lp-cribbs is a Python-based cryptanalysis & cryptography tool designed to make attempts at deciphering the remaining parts of the Liber Primus, the latest mystery of the famous Cicada 3301 puzzle. On the cryptanalytical side, it is (not quite yet, but we'll get there) capable of running dozens of tests on both the solved and the unsolved sectionsof the book, in order to try narrowing down on the cryptographic functions that might have been used on the text. On the other hand, it can run many types of brute-force attacks on the given encrypted text, by means of cribbing and key derivation. It's still in its very early stages, and there are tons of things I still have to add.

## Installation

First and foremost, make sure that you have the Python3 interpreter installed and a virtual environment set up. Next, install the packages contained within the *requirements.txt* file using pip.

## Usage

If you want to get into decryption right away, you can do that through **main.py**. As for the cryptanalysis, everything can be found within the scripts of the analysis folder.
