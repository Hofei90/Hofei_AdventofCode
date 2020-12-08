import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


class InfinityGuard:
    def __init__(self, anweisungen):
        self.position = [False] * len(anweisungen)

    def set_position(self, index):
        self.position[index] = True

    def get_position(self, index):
        return self.position[index]


class Bootloader:
    def __init__(self, befehle, infinity_guard):
        self.befehle = befehle
        self.index = 0
        self.accumulator = 0
        self.infinity_guard = infinity_guard

    def excecute_befehl(self):
        index = self.index
        if not self.infinity_guard.get_position(index):
            if self.befehle[index][0] == "acc":
                self.accumulator += int(self.befehle[index][1])
                self.index += 1
            elif self.befehle[index][0] == "jmp":
                self.index += int(self.befehle[index][1])
            elif self.befehle[index][0] == "nop":
                self.index += 1
            else:
                raise ValueError
            self.infinity_guard.set_position(index)
            return True
        else:
            return False


def read_input(datei):
    """Gibt eine Liste mit den Anweisungsbefehlen zurück
    Die Anweisungsbefehle sind ebenfalls in Listen enthalten
    Index 0 enthält den Befehl
    Index 1 enthält den Wert"""
    with open(datei) as file:
        inhalt = file.readlines()
    return [line.strip().split() for line in inhalt]


def main():
    anweisungen = read_input(os.path.join(SKRIPTPFAD, "input_8_1"))
    infinity_guard = InfinityGuard(anweisungen)
    bootloader = Bootloader(anweisungen, infinity_guard)
    running_bootloader = True
    while running_bootloader:
        running_bootloader = bootloader.excecute_befehl()
    print(f"Lösung Teil 1, Accumulator: {bootloader.accumulator}")


if __name__ == "__main__":
    main()
