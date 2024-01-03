#!/usr/bin/env python3

from subprocess import call
from math import ceil
from colorama import init, Fore, Style
import re
#from sys import stdout

init(autoreset=True) #Apparently the autoreset mechanism doesn't work with stdout.write :(

ascii_art = " \
////////////////////////////////////////////////////// \n\
//                                                  // \n\
//                                                  // \n\
//    _                       _ _     _             // \n\
//   | |_ __         ___ _ __(_) |__ | |__  ___     // \n\
//   | | '_ \ _____ / __| '__| | '_ \| '_ \/ __|    // \n\
//   | | |_) |_____| (__| |  | | |_) | |_) \__ \    // \n\
//   |_| .__/       \___|_|  |_|_.__/|_.__/|___/    // \n\
//     |_|                                          // \n\
//                                                  // \n\
//                                                  // \n\
////////////////////////////////////////////////////// \n"

print(ascii_art)
print(Style.BRIGHT + Fore.GREEN + "Welcome to cribbs! Have fun bruteforcing ciphers!\n")

## NOTE: develop the commands + add more
commands = [
        ("break_standard", "Break the cipher, if it's a simple monoalphabetic substitution cipher (like ROT13, Caesar, Atbash etc.)"),
        ("find_key_standard", "Run a key derivation algorithm on the text using 3 standard ciphers: Caesar, Atbash and Vigenere (+ Beaufort)."),
        ("break_progressive_shift", "Attempt to decipher the text, if it utilizes a progressive shift."),
        ("break_progressive_shift_mobius", "Attempt to decipher the text, if it utilizes a progressive shift that incorporates the Möbius function."),
        ("break_progressive_shift_affine", "Attempt to decipher the text if it utilizes a progressive shift alongside an Affine-like cipher."),
        ("break_quagmire3", "Attempt to decipher the text, if it utilizes the Quagmire III cipher."),
        ("break_polybius", "Attempt to break the cipher through famous polybius-based cryptographic functions (Bifid, Playfair etc.)"),
        ("quit", "Exit the program")]
delimiter = "~~~"
is_running = True

while is_running:
    print("What would you like to perform? // Command syntax: {command} [path/to/ciphered/text] // \n")
    print("Options:")
    for command, desc in commands:
        pre_delimiter_whitespaces = 40-len(command)-len(delimiter)
        post_delimiter_whitespaces = 10
        print(Style.BRIGHT + f"     {command}", end=f"{pre_delimiter_whitespaces*' '}{delimiter}{post_delimiter_whitespaces*' '}")
        print(f"{desc}")
    command = input(">")


    if command == "quit":
        is_running = False
