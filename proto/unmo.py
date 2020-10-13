from proto.responder import Responder


class Unmo:
    def __init__(self, name):
        self.name = name
        self.responder = Responder(name)

    def dialogue(self, data):
        return self.responder.response(data)

    def responder_name(self):
        return self.responder.name
