from utils import get_line


class Poem:
    structure = ()

    def __init__(self):
        self.lines = []

        for line in self.structure:
            self.lines.append(' '.join(get_line(line)))

    def __str__(self):
        return '\n'.join([line.title() for line in self.lines])


class Haiku(Poem):
    structure = [5, 7, 5]
