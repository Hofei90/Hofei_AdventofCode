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


def check_passwords_part1(passwords):
    counter = 0
    for pw in passwords:
        frequency = pw.password.count(pw.character)
        if pw.frequency_min <= frequency <= pw.frequency_max:
            counter += 1
    return counter


def check_passwords_part2(passwords):
    counter = 0
    for pw in passwords:
        if pw.password[pw.frequency_min - 1] == pw.character and pw.password[pw.frequency_max - 1] != pw.character:
            counter += 1
        elif pw.password[pw.frequency_min - 1] != pw.character and pw.password[pw.frequency_max - 1] == pw.character:
            counter += 1
    return counter


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_2_1"))
    passwords = create_passwordlist(inhalt)

    # Day 2 Nr. 1
    right_passwords = check_passwords_part1(passwords)
    print(f"Solution auf Day 2 #1: {right_passwords}")

    # Day 2 Nr. 1
    right_passwords = check_passwords_part2(passwords)
    print(f"Solution auf Day 2 #2: {right_passwords}")


if __name__ == "__main__":
    main()
