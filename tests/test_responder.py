import unittest
from noby.dictionary import Dictionary
from noby.responder import WhatResponder


class WhatResponderTest(unittest.TestCase):
    def test_response(self):
        dictionary = Dictionary()
        responder = WhatResponder('What', dictionary)

        self.assertEquals('Pythonってなに？', responder.response('Python'))
