import random


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
