# Markov NLP Preprocessor
# Preprocesses NLTK corpora to enable Markov chain simulation
# by nlpgen.py

# Modify these two statements to change which corpus
# is used
from nltk.corpus import inaugural
corpus = inaugural

import json

allthewords = {}

def add(dict, key, word):
    if dict.get(key) is None:
        dict[key] = {}
    if dict[key].get(word) is None:
        dict[key][word] = 0
    dict[key][word] += 1

filename = input("Output filename> ")

for word, next in zip(corpus.words(), corpus.words()[1:]):
    # Add each word to the dictionary
    add(allthewords, word, next)


with open(filename, "w") as file:
    file.write(json.dumps(allthewords))

print(f"Successfully saved {i + 1} words to {filename}")