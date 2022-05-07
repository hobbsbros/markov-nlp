Extremely Basic Natural Language Generation, Powered By Markov Chains
=====================================================================

This is a *very simple* Python package that enables generation of passable but meaningless English-like sentences.

The package constructs Markov chains from downloaded NLTK corpora and generates English sentences based on the Markov models.

# Dependencies

This project has the following Python package dependencies:
- `json`
- `nltk`
- `os`
- `random`

# How To Use

Using this package is very simple.

## Clone the Repository

First, clone this repository into your working directory.

```
$ git clone https://github.com/hobbsbros/markov-nlp.git
$ cd markov-nlp
```

## Install Dependencies

Next, ensure that you have all four dependencies (as listed above) installed.

## Preprocess Data

In `preprocess.py`, change lines 7 and 8 to reflect the NLTK corpus that you desire to create a Markov model from.  By default, the `inaugural` corpus of U.S. Presidential Inauguration speeches is used.

Currently, only NLTK corpora are supported.

Run `py preprocess.py` in your terminal and follow the instructions on-screen.  The preprocessor will request a filename to save preprocessed data to; it is recommended that this file has `.json` extension.

## Generate Natural Language

Run `py nlpgen.py` in your terminal and follow the instructions on-screen.  Note that it will require the filename for the preprocessed data.  Ensure that the filename and extension match what you put into the preprocessor (see above).

# How Does It Work?

This package constructs a simple statistical model (a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)) from the provided NLTK corpus.  The Markov chain represents transitional probabilities from one word to the next word.  It does this by iterating over the entire corpus of words and recording the transitional frequencies of each successive word.

For example, for the word "of", it counts the number of times it sees "my" after "of", "representative" after "of", etc.  It then uses this information to construct a list of probabilities representing how likely each word is to come after "of".  It then uses this process to generate visibly passable but completely ungrammatical English sentences (on execution of `nlpgen.py`).

# Disclaimer

This package is no longer being actively maintained.

# License

This package is licensed under the MIT license and is provided *as-is* with no warranty.  See `LICENSE` for more information.