import random
import re


class Responder:
    def __init__(self, name, dictionary):
        self.name = name
        self.dictionary = dictionary

    def response(self, data):
        return ''


class WhatResponder(Responder):
    def response(self, data):
        return f'{data}ってなに？'


class RandomResponder(Responder):
    def response(self, data):
        return random.choice(self.dictionary.random)


class PatternResponder(Responder):
    def response(self, data):
        for pattern_item in self.dictionary.pattern:
            match = re.search(pattern_item['pattern'], data)
            if match is None:
                continue

            return random.choice(pattern_item['phrases']).replace('%match%', match.group())
        return random.choice(self.dictionary.random)