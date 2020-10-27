import unittest
from noby.responder import WhatResponder


class WhatResponderTest(unittest.TestCase):
    def test_response(self):
        responder = WhatResponder('What')

        self.assertEquals('Pythonってなに？', responder.response('Python'))
