from pathlib import Path

import noby


class Dictionary:
    def __init__(self):
        with open(Path(noby.__path__[0]) / 'dics' / 'random.txt') as f:
            self.random = [line.rstrip() for line in f if len(line) > 0]
