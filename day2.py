import os
from dataclasses import dataclass

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


@dataclass
class PwPolicy:
    character: str
    frequency_min: int
    frequency_max: int
    password: str


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def analyze_frequency(frequency):
    min_max = frequency.split("-")
    return min_max


def analyze_character(character):
    char = character[0]
    return char


def create_passwordlist(data):
    passwordliste = []
    for datum in data:
        datum_liste = datum.split()
        min_max = analyze_frequency(datum_liste[0])
        character = analyze_character(datum_liste[1])
        passwordliste.append(PwPolicy(character, int(min_max[0]), int(min_max[1]), datum_liste[-1]))
    return passwordliste


def check_passwords(passwords):
    counter = 0
    for pw in passwords:
        frequency = pw.password.count(pw.character)
        if pw.frequency_min <= frequency <= pw.frequency_max:
            counter += 1
    return counter


def main():
    # Day 2 Nr. 1
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_2_1"))
    passwords = create_passwordlist(inhalt)
    right_passwords = check_passwords(passwords)
    print(f"Solution auf Day 2 #1: {right_passwords}")


if __name__ == "__main__":
    main()
