import itertools
import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))
PREAMBLE_ANZAHL = 25

class Preamble:
    def __init__(self, values):
        self.preamble = values
        self.preamble_summen = generature_preamble_summen(self.preamble)


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return [int(value) for value in inhalt]


def generature_preamble_summen(values):
    combinations = itertools.combinations(values, 2)
    return [sum(combination) for combination in combinations]


def check_values(values):
    for index, _ in enumerate(values):
        preamble = Preamble(values[index:PREAMBLE_ANZAHL + index])
        number = values[PREAMBLE_ANZAHL + index]
        if number not in preamble.preamble_summen:
            return number


def find_list_contiguous_set(searched_sum, values):
    for index_number in range(0, len(values)):
        for position, _ in enumerate(values):
            contiguous_set = values[position:index_number+position+2]
            if sum(contiguous_set) == searched_sum:
                return contiguous_set


def get_encryption_weakness(contiguous_set):
    return min(contiguous_set) + max(contiguous_set)


def main():
    values = read_input(os.path.join(SKRIPTPFAD, "input_9"))
    incorrect_value = check_values(values)
    print(f"Die inkorrekte Zahl lautet: {incorrect_value} (Lösung Tag 9 Teil 1)")

    contiguous_set = find_list_contiguous_set(incorrect_value, values)
    print(f"Lösung Tag 9 Teil 2: {get_encryption_weakness(contiguous_set)}")


if __name__ == "__main__":
    main()