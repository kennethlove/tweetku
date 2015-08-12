import utils

def test_has_words():
    assert utils.words


def test_get_line():
    line = utils.get_line(3)
    assert sum([word.syllables for word in line]) == 3