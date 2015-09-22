import poems
import utils


def test_get_line():
    line = utils.get_line(3)
    assert isinstance(line, list)


def test_build_haiku():
    haiku = poems.Haiku()
    assert len(haiku.lines) == 3


def test_poem_string():
    haiku = poems.Haiku()
    haiku.lines = ['ABCDE', 'ABCDEFG', 'ABCDE']
    assert str(haiku) == '\n'.join([l.title() for l in haiku.lines])


def test_generate_text_files():
    syllables, gutenberg, brown = utils.generate_text_files()
assert all([
    isinstance(syllables, dict),
    isinstance(gutenberg, dict),
    isinstance(brown, dict)
])
