from collections import defaultdict
import csv
from itertools import filterfalse
import re

word_syllables = re.compile(
    r'^(?P<word>[-\w]+)\s{2}(?P<syllables>(\w+\d?\s?)+)$',
)


def build_csv(corpus):
    for line in filterfalse(lambda x: x.startswith(';;;'),
                            open(corpus, 'r', encoding='utf-8')):
        match = word_syllables.match(line)
        if match and len(match.group('syllables').split()) < 8:
            yield match.group('word'), len(match.group('syllables').split())


with open('words.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(build_csv('dict.txt'))


def build_dict(csvfile):
    reader = csv.reader(open(csvfile, 'r', encoding='utf-8'))
    word_dict = defaultdict(list)
    for word, syl in reader:
        word_dict[int(syl)].append(word)
    return word_dict

words = build_dict('words.csv')

