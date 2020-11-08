from pathlib import Path

import noby


class Dictionary:
    def __init__(self):
        with open(Path(noby.__path__[0]) / 'dics' / 'random.txt') as f:
            self.random = [line.rstrip() for line in f if len(line) > 0]

        with open(Path(noby.__path__[0]) / 'dics' / 'pattern.txt') as f:
            self.pattern = [
                {'pattern': item[0], 'phrases': item[1].split('|')}
                for item in [line.rstrip().split('\t') for line in f]
                if len(item) == 2 and len(item[0]) > 0 and len(item[1]) > 0]
