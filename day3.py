import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


class Navigator:
    def __init__(self, down, right, matrix):
        self.down = down
        self.right = right
        self.x = 0
        self.y = 0
        self.matrix = matrix

    def drive(self):
        self.x += self.right
        self.y += self.down

    def check_crash(self):
        x_pointer = self.x % len(self.matrix[self.y])
        if self.matrix[self.y][x_pointer]:
            return True
        else:
            return False


def generate_matrix(inhalt):
    matrix = []
    for line in inhalt:
        row = []
        line = line.strip()
        for spell in line:
            if spell == ".":
                row.append(False)
            elif spell == "#":
                row.append(True)
            else:
                raise ValueError
        matrix.append(row)
    return matrix


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def main():
    matrix = generate_matrix(read_input(os.path.join(SKRIPTPFAD, "input_3_1")))
    navigator = Navigator(1, 3, matrix)
    counter = 0
    for _ in matrix:
        if navigator.check_crash():
            counter += 1
        navigator.drive()
    print(f"Solution auf Day 3 #1: {counter}")


if __name__ == "__main__":
    main()