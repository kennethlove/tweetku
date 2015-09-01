import collections
import pickle
import csv
import itertools
import os
import random
import re

import nltk.collocations
import nltk.corpus
from nltk.corpus import wordnet


word_syllables = re.compile(
    r'^(?P<word>[-\w]+)\s{2}(?P<syllables>(\w+\d?\s?)+)$',
)


class Word(str):
    syllables = 0


def build_syllable_pairs(corpus):
    for line in itertools.filterfalse(lambda x: x.startswith(';;;'),
                                      open(corpus, 'r', encoding='utf-8')):
        match = word_syllables.match(line)
        if match and all([
            len(match.group('syllables').split()) < 8,
            wordnet.synsets(match.group('word'))
        ]):
            yield (len(match.group('syllables').split()),
                   match.group('word').lower())


def find_bigrams(corpus):
    bgm = nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(corpus)
    finder.apply_freq_filter(3)  # must be found at least 3 times
    bigrams = finder.nbest(bgm.pmi, 10000)
    for first, second in bigrams:
        if first.isalpha() and second.isalpha():
            yield first, second


def bigrams_to_syllables(syllables, bigrams):
    output = collections.defaultdict(list)
    for first, second in bigrams:
        first = first.lower()
        second = second.lower()

        found_words = []
        total = 0
        for word in (first, second):
            count = [k for k, v in syllables.items() if word in v]
            if count:
                total += count[0]
                found_words.append(word)
        if len(found_words) == 2 and total <= 7:
            output[total].append(found_words)
    return output


def generate_text_files():
    if not os.path.exists('syllables.pickle'):
        syllables = collections.defaultdict(list)
        for length, word in build_syllable_pairs('cmudict.txt'):
            syllables[length].append(word)
        pickle.dump(syllables, open('syllables.pickle', 'wb'))
    else:
        syllables = pickle.load(open('syllables.pickle', 'rb'))
    if not os.path.exists('gutenberg.pickle'):
        gutenberg = bigrams_to_syllables(
            syllables,
            find_bigrams(nltk.corpus.gutenberg.words())
        )
        pickle.dump(gutenberg, open('gutenberg.pickle', 'wb'))
    else:
        gutenberg = pickle.load(open('gutenberg.pickle', 'rb'))
    if not os.path.exists('brown.pickle'):
        brown = bigrams_to_syllables(
            syllables,
            find_bigrams(nltk.corpus.brown.words())
        )
        pickle.dump(brown, open('brown.pickle', 'wb'))
    else:
        brown = pickle.load(open('brown.pickle', 'rb'))
    return syllables, gutenberg, brown


def get_line(syllables):
    texts = generate_text_files()
    total = 0
    syllable_counts = []
    while total < syllables:
        num = random.randint(1, syllables-total)
        syllable_counts.append(num)
        total += num
    chosen_words = []
    for syllable in syllable_counts:
        corpus = random.choice(texts)
        while syllable not in corpus:
            corpus = random.choice(texts)
        chosen_words.append(random.choice(corpus[syllable]))
    return chosen_words

