from collections import defaultdict, namedtuple
import csv
import itertools
import random
import re

word_syllables = re.compile(
    r'^(?P<word>[-\w]+)\s{2}(?P<syllables>(\w+\d?\s?)+)$',
)

class Word(str):
    syllables = 0


def build_csv(corpus):
    for line in itertools.filterfalse(lambda x: x.startswith(';;;'),
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
        word = Word(word)
        word.syllables = int(syl)
        word_dict[int(syl)].append(word)
    return word_dict

words = build_dict('words.csv')


def get_line(syllables):
    total = 0
    order = []
    while total < syllables:
        num = random.randint(1, syllables-total)
        order.append(num)
        total += num
    line = map(lambda l: random.choice(words[l]), order)
    return list(line)
