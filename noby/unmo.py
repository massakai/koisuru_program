import random

from noby.dictionary import Dictionary
from noby.responder import RandomResponder, WhatResponder, PatternResponder


class Unmo:
    def __init__(self, name):
        self.name = name
        self.dictionary = Dictionary()
        self.responder_what = WhatResponder('What', self.dictionary)
        self.responder_random = RandomResponder('Random', self.dictionary)
        self.responder_pattern = PatternResponder('Pattern', self.dictionary)
        self.responder = self.responder_random

    def dialogue(self, data):
        n = random.randint(0, 100)
        if n < 60:
            self.responder = self.responder_pattern
        elif n < 90:
            self.responder = self.responder_random
        else:
            self.responder = self.responder_what
        return self.responder.response(data)

    def responder_name(self):
        return self.responder.name
