import random
from pathlib import Path

import noby


class Responder:
    def __init__(self, name):
        self.name = name

    def response(self, data):
        return ''


class WhatResponder(Responder):
    def response(self, data):
        return f'{data}ってなに？'


class RandomResponder(Responder):
    def __init__(self, name):
        super().__init__(name)
        with open(Path(noby.__path__[0]) / 'dics' / 'random.txt') as f:
            self.responses = [line.rstrip() for line in f]

    def response(self, data):
        return random.choice(self.responses)
