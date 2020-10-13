class Responder:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def response(data):
        return f'{data}ってなに？'