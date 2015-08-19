from utils import get_line


class Poem:
    structure = None
    def __init__(self):
        self.lines = []

        for line in self.structure:
            self.lines.append(' '.join(get_line(line)))


class Haiku(Poem):
    structure = [5, 7, 5]
