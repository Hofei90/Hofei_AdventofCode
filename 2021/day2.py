import utils
from pathlib import Path

SKRIPTPFAD = Path(__file__).parent
INPUT1 = SKRIPTPFAD / "input_2_1.txt"


class Navigator:
    def __init__(self, horizontal, tiefe):
        self.horizontal = horizontal
        self.tiefe = tiefe

    def move(self, befehl):
        cmd = befehl.split()
        direction = cmd[0]
        value = int(cmd[1])
        if direction == "forward":
            self.move_forward(value)
        elif direction == "down":
            self.move_down(value)
        elif direction == "up":
            self.move_up(value)

    def move_forward(self, value):
        self.horizontal += value

    def move_down(self, value):
        self.tiefe += value

    def move_up(self, value):
        self.tiefe -= value


class Navigator2:
    def __init__(self, horizontal, tiefe, ziel):
        self.horizontal = horizontal
        self.tiefe = tiefe
        self.ziel = ziel

    def move(self, befehl):
        cmd = befehl.split()
        direction = cmd[0]
        value = int(cmd[1])
        if direction == "forward":
            self.move_forward(value)
        elif direction == "down":
            self.move_down(value)
        elif direction == "up":
            self.move_up(value)

    def move_forward(self, value):
        self.horizontal += value
        self.tiefe += value * self.ziel

    def move_down(self, value):
        self.ziel += value

    def move_up(self, value):
        self.ziel -= value


def calc_erg1(x, y):
    return x * y


def main():
    planned_course = INPUT1.read_text().split("\n")
    navigator = Navigator(0, 0)
    navigator2 = Navigator2(0, 0, 0)
    for cmd in planned_course:
        navigator.move(cmd)
        navigator2.move(cmd)
    print(f"Ergebnis: {calc_erg1(navigator.tiefe, navigator.horizontal)}")
    print(f"Ergebnis: {calc_erg1(navigator2.tiefe, navigator2.horizontal)}")


if __name__ == "__main__":
    main()