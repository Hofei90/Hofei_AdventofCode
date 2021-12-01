import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


class Navigator:
    def __init__(self, direction):
        self.direction = direction
        self.north_south = 0
        self.east_west = 0

    def turn_ship(self, value):
        erg = self.direction + value
        if erg >= 360:
            self.direction = erg - 360
        elif erg < 0:
            self.direction = 360 + erg
        else:
            self.direction = erg

    def go(self, action, value):
        if action == "N":
            self._go_north(value)
        elif action == "S":
            self._go_south(value)
        elif action == "E":
            self._go_east(value)
        elif action == "W":
            self._go_west(value)
        elif action == "L":
            self.turn_ship(value * -1)
        elif action == "R":
            self.turn_ship(value)
        elif action == "F":
            self.go(get_direction_as_char(self.direction), value)
        else:
            raise ValueError

    def _go_north(self, value):
        self.north_south += value

    def _go_south(self, value):
        self.north_south -= value

    def _go_east(self, value):
        self.east_west += value

    def _go_west(self, value):
        self.east_west -= value


def get_direction_as_char(direction):
    if direction == 0:
        return "N"
    elif direction == 90:
        return "E"
    elif direction == 180:
        return "S"
    elif direction == 270:
        return "W"
    else:
        raise ValueError


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def parse_instructions(inhalt):
    instructions = []
    for befehl in inhalt:
        befehl = befehl.strip()
        instructions.append((befehl[0], int(befehl[1:])))
    return instructions


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_12"))
    instractions = parse_instructions(inhalt)
    navigator = Navigator(90)
    for instraction in instractions:
        navigator.go(instraction[0], instraction[1])
    print(abs(navigator.north_south) + abs(navigator.east_west))


if __name__ == "__main__":
    main()
