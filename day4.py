import os
from dataclasses import dataclass

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


@dataclass
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def analyze_passwort_data(passport_dict, row):
    data = row.split()
    for datum in data:
        datum_list = datum.split(":")
        if datum_list[0] in passport_dict.keys():
            raise KeyError
        passport_dict[datum_list[0]] = datum_list[1]
    return passport_dict


def generate_passport_data(inhalt):
    passport_data = []
    passport_dict = {}
    for row in inhalt:
        row = row.strip()
        if row:
            passport_dict = analyze_passwort_data(passport_dict, row)
        else:
            passport_data.append(passport_dict)
            passport_dict = {}
    return passport_data


def generate_passports(passport_data):
    passports = []
    for datum in passport_data:
        try:
            passports.append(Passport(
                byr=datum["byr"],
                iyr=datum["iyr"],
                eyr=datum["eyr"],
                hgt=datum["hgt"],
                hcl=datum["hcl"],
                ecl=datum["ecl"],
                pid=datum["pid"],
                cid=datum.get("cid", None)
                )
            )
        except KeyError:
            continue
    return passports


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_4_1.txt"))
    passport_data = generate_passport_data(inhalt)
    passports = generate_passports(passport_data)
    print(len(passports))


if __name__ == "__main__":
    main()
