from utils import get_line


class Poem:
    structure = ()

    def __init__(self):
        self.lines = []

        for line in self.structure:
            output = []
            random_line = get_line(line)
            for bit in random_line:
                output.append(' '.join(bit) if isinstance(bit, list) else bit)
            self.lines.append(' '.join(output))

    def __str__(self):
        return '\n'.join([line.title() for line in self.lines])


class Haiku(Poem):
    structure = [5, 7, 5]
