# An extremely simple Markov chain model of the English language
# for generating English-like sentences

import json
import os
from random import choices

filename = input("Input preprocessed corpus filename> ")

PUNCTUATION = {";", ",", ".", ":", "?", "!"}
NOSPACE = {"'", "-", "--"}

def clear():
    """
    Cross-platform terminal clearing
    """
    os.system("cls" if os.name == "nt" else "clear")

def caps(string):
    """
    Capitalize the first letter in the given string and return the result
    """
    return string[0].upper() + string[1:]

def join(list):
    """
    Join together tokens (from a Markov chain) according to a rough
    model of English punctuation and capitalization
    """
    output = ""
    i = 0
    while i < len(list):
        # We only want complete sentences in our output
        if "." not in list[i:]:
            break

        # We also want to enforce capitalization at the beginning
        # of sentences
        if i > 0 and list[i - 1] == ".":
            output += caps(list[i])
        else:
            output += list[i]
        
        # And we want to enforce spaces between words, but not between
        # words and punctuation
        if list[i + 1] not in PUNCTUATION | NOSPACE and ((i > 0 and list[i - 1] not in NOSPACE) or i == 0):
            output += " "
        
        i += 1
    return output

allthewords = {}

with open(filename, "r") as file:
    allthewords = json.loads(file.read())

clear()

while True:
    begin = input("Provide a starting word or phrase (optional)> ")
    # Get the last word in `begin` to use as a starting word
    current = begin.split(" ")[-1]
    sofar = []
    for _ in range(150):
        if allthewords.get(current) is not None:
            # If the current word exists in the corpus, get the next word based on
            # state transitional probabilities
            next = choices(list(allthewords[current].keys()), list(allthewords[current].values()))
        else:
            # If the current word does not exist in the corpus, just get a random
            # word from the corpus
            next = choices(list(allthewords.keys()))
        next = next[0]
        sofar.append(next)
        current = next
    # Right now this just prints output to the terminal
    # But this can easily be modified to output into a file
    # or really anything else
    space = " " if sofar[0] not in PUNCTUATION else ""
    output = begin + space + join(sofar)
    print()
    print(f"NLP output:\n{output}")
    print()
    print()