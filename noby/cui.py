from noby.unmo import Unmo


def prompt(unmo):
    return unmo.name + ':' + unmo.responder_name() + '> '


def main():
    print('Unmo System prototype : noby')
    proto = Unmo('noby')

    while True:
        value = input('> ').rstrip()
        if value == '':
            break

        response = proto.dialogue(value)
        print(prompt(proto) + response)


if __name__ == '__main__':
    main()
