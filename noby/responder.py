import random


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
        self.responses = ['今日はさむいね', 'チョコたべたい', 'きのう10円ひろった']

    def response(self, data):
        return random.choice(self.responses)
