import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


class JoltManager:
    def __init__(self):
        self.number_jolts_one_different = 0
        self.number_jolts_three_different = 0

    def increase_one_different(self):
        self.number_jolts_one_different += 1

    def increase_three_different(self):
        self.number_jolts_three_different += 1


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return [int(value) for value in inhalt]


def check_adapters(manager, adapters):
    previous_adapter = 0
    for adapter in adapters:
        jolt_different = adapter - previous_adapter
        if jolt_different > 3:
            raise ValueError
        elif jolt_different == 1:
            manager.increase_one_different()
        elif jolt_different == 3:
            manager.increase_three_different()
        previous_adapter = adapter


def main():
    adapters = read_input(os.path.join(SKRIPTPFAD, "input_10"))
    adapters.sort()
    jolt_manager = JoltManager()
    check_adapters(jolt_manager, adapters)
    print((jolt_manager.number_jolts_three_different + 1) * jolt_manager.number_jolts_one_different)


if __name__ == "__main__":
    main()