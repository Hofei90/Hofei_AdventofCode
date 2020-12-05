import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


class BinaryBoarding:
    def __init__(self, max_row, max_column, seat):
        self.rows = [value for value in range(0, max_row)]
        self.columns = [value for value in range(0, max_column)]
        self.seat = seat
        self.seat_id = None

    def analyze_seat_id(self):
        for spell in self.seat:
            if spell == "F":
                self.change_row(False)
            elif spell == "B":
                self.change_row(True)
            elif spell == "R":
                self.change_column(True)
            elif spell == "L":
                self.change_column(False)

        self.seat_id = self.rows[0] * 8 + self.columns[0]


    def change_row(self, lower_upper):
        if lower_upper:
            self.rows = get_upper_half(self.rows)
        else:
            self.rows = get_lower_half(self.rows)

    def change_column(self, lower_upper):
        if lower_upper:
            self.columns = get_upper_half(self.columns)
        else:
            self.columns = get_lower_half(self.columns)


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def get_upper_half(plaetze):
    half = get_half(plaetze)
    return plaetze[half:]


def get_lower_half(plaetze):
    half = get_half(plaetze)
    return plaetze[:half]


def get_half(plaetze):
    return int(len(plaetze) / 2)


def main():
    max_row = 128
    max_column = 8
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_5_1"))
    max_seat_id = 0
    seat_ids = []
    for seat in inhalt:
        boarding = BinaryBoarding(max_row, max_column, seat)
        boarding.analyze_seat_id()
        max_seat_id = max(boarding.seat_id, max_seat_id)
        seat_ids.append(boarding.seat_id)
    print(max_seat_id)

    # Tag 5 #2
    min_seat_id = min(seat_ids)
    max_seat_id = max(seat_ids)
    ids = [id_ for id_ in range(min_seat_id, max_seat_id + 1)]
    my_id = set(ids) - set(seat_ids)
    print(my_id)


if __name__ == "__main__":
    main()
