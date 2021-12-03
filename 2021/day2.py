import utils
from pathlib import Path

SKRIPTPFAD = Path(__file__).parent
INPUT1 = SKRIPTPFAD / "input_2_1.txt"


class BaseNavigator:
    def __init__(self, horizontal=0, tiefe=0):
        self.horizontal = horizontal
        self.tiefe = tiefe

    def move(self, befehl):
        direction, value = befehl.split()
        getattr(self, f"move_{direction}")(int(value))


class Navigator(BaseNavigator):
    def move_forward(self, value):
        self.horizontal += value

    def move_down(self, value):
        self.tiefe += value

    def move_up(self, value):
        self.tiefe -= value


class AimingNavigator(BaseNavigator):
    def __init__(self, horizontal=0, tiefe=0, ziel=0):
        BaseNavigator.__init__(self, horizontal, tiefe)
        self.ziel = ziel

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
    navigator = Navigator()
    navigator2 = AimingNavigator()
    for cmd in planned_course:
        navigator.move(cmd)
        navigator2.move(cmd)
    print(f"Ergebnis: {calc_erg1(navigator.tiefe, navigator.horizontal)}")
    print(f"Ergebnis: {calc_erg1(navigator2.tiefe, navigator2.horizontal)}")


if __name__ == "__main__":
    main()