class Responder:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def response(data):
        return f'{data}ってなに？'


class Unmo:
    def __init__(self, name):
        self.name = name
        self.responder = Responder(name)

    def dialogue(self, data):
        return self.responder.response(data)

    def responder_name(self):
        return self.responder.name


def prompt(unmo):
    return unmo.name + ':' + unmo.responder_name() + '> '


if __name__ == '__main__':
    print('Unmo System prototype : proto')
    proto = Unmo('proto')

    while True:
        value = input('> ').rstrip()
        if value == '':
            break

        response = proto.dialogue(value)
        print(prompt(proto) + response)

