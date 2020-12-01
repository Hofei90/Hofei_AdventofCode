import os
import itertools

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


def convert_to_int(inhalt):
    new_list = [int(zahl.strip()) for zahl in inhalt]
    return new_list


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def generate_combinations(zahlen_liste):
    combinations = itertools.combinations(zahlen_liste, 2)
    return combinations


def check_sum(combinations, summe):
    for a, b in combinations:
        if a + b == summe:
            return a, b


def produkt_of_right_combinations(a, b):
    return a * b


def main():
    inhalt = convert_to_int(read_input(os.path.join(SKRIPTPFAD, "input_1_1")))
    combinations = generate_combinations(inhalt)
    int_a, int_b = check_sum(combinations, 2020)
    solution = produkt_of_right_combinations(int_a, int_b)
    print(solution)


if __name__ == "__main__":
    main()
