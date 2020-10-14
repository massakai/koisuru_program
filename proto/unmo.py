from proto.responder import RandomResponder


class Unmo:
    def __init__(self, name):
        self.name = name
        self.responder = RandomResponder('Random')

    def dialogue(self, data):
        return self.responder.response(data)

    def responder_name(self):
        return self.responder.name
