import poems
import utils


def test_has_words():
    assert utils.words


def test_get_line():
    line = utils.get_line(3)
    assert sum([word.syllables for word in line]) == 3


def test_assemble_line():
    line = utils.get_line(3)
    assert ' '.join(line)


def test_build_haiku():
    haiku = poems.Haiku()
    assert len(haiku.lines) == 3


def test_poem_string():
    haiku = poems.Haiku()
    haiku.lines = ['ABCDE', 'ABCDEFG', 'ABCDE']
    assert str(haiku) == '\n'.join([l.title() for l in haiku.lines])
