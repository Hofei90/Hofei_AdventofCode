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


def generate_combinations(zahlen_liste, r):
    combinations = itertools.combinations(zahlen_liste, r)
    return combinations


def check_sum(combinations, summe):
    for combination in combinations:
        if sum(combination) == summe:
            return combination


def produkt_of_right_combinations(combination):
    ergebnis = 1
    for zahl in combination:
        ergebnis = ergebnis * zahl
    return ergebnis


def main():
    inhalt = convert_to_int(read_input(os.path.join(SKRIPTPFAD, "input_1_1")))
    # Day 1 Nr. 1
    combinations = generate_combinations(inhalt, 2)
    right_combination = check_sum(combinations, 2020)
    solution = produkt_of_right_combinations(right_combination)
    print(f"Solution auf Day 1 #1: {solution}")

    # Day 1 Nr. 2
    combinations = generate_combinations(inhalt, 3)
    right_combination = check_sum(combinations, 2020)
    solution = produkt_of_right_combinations(right_combination)
    print(f"Solution auf Day 1 #2: {solution}")


if __name__ == "__main__":
    main()
