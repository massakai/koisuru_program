from proto.unmo import Unmo


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