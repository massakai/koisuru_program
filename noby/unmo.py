import random

from noby.dictionary import Dictionary
from noby.responder import RandomResponder, WhatResponder


class Unmo:
    def __init__(self, name):
        self.name = name
        self.dictionary = Dictionary()
        self.responder_what = WhatResponder('What', self.dictionary)
        self.responder_random = RandomResponder('Random', self.dictionary)
        self.responder = self.responder_random

    def dialogue(self, data):
        self.responder = random.choice((
            self.responder_what, self.responder_random))
        return self.responder.response(data)

    def responder_name(self):
        return self.responder.name
