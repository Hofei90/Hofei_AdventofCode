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


def datenvalidation(passport_dict):
    try:
        if not validation_byr(passport_dict["byr"]):
            return False
        if not validation_iyr(passport_dict["iyr"]):
            return False
        if not validation_eyr(passport_dict["eyr"]):
            return False
        if not validation_hgt(passport_dict["hgt"]):
            return False
        if not validation_hcl(passport_dict["hcl"]):
            return False
        if not validation_ecl(passport_dict["ecl"]):
            return False
        if not validation_pid(passport_dict["pid"]):
            return False
    except KeyError:
        return False
    else:
        return True



def validation_byr(byr):
    byr = str(byr)
    if len(byr) == 4:
        byr = int(byr)
        if 1920 <= byr <= 2002:
            return True
    return False


def validation_iyr(iyr):
    iyr = str(iyr)
    if len(iyr) == 4:
        iyr = int(iyr)
        if 2010 <= iyr <= 2020:
            return True
    return False


def validation_eyr(eyr):
    eyr = str(eyr)
    if len(eyr) == 4:
        eyr = int(eyr)
        if 2020 <= eyr <= 2030:
            return True
    return False


def validation_hgt(hgt):
    counter = 0
    for counter, charactar in enumerate(hgt):
        if not charactar.isdigit():
            break
    value = int(hgt[:counter])
    unit = hgt[counter:]

    if unit == "cm":
        if 150 <= value <= 193:
            return True
        else:
            return False
    elif unit == "in":
        if 59 <= value <= 76:
            return True
        else:
            return False
    else:
        return False


def validation_hcl(hcl):
    valid = []
    if hcl.startswith("#"):
        if len(hcl[1:]) == 6:
            for char in hcl[1:]:
                try:
                    if int(char) in range(0, 10):
                        valid.append(True)
                    else:
                        valid.append(False)
                except ValueError:
                    if ord("a") <= ord(char) <= ord("f"):
                        valid.append(True)
                    else:
                        valid.append(False)
            return min(valid)

    return False



def validation_ecl(ecl):
    valid_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in valid_values:
        return True
    else:
        return False


def validation_pid(pid):
    pid = str(pid)
    if len(pid) == 9:
        for char in pid:
            if not char.isdigit():
                return False
        return True
    else:
        return False


def generate_passport_data(inhalt):
    passport_data = []
    passport_dict = {}
    for row in inhalt:
        row = row.strip()
        if row:
            passport_dict = analyze_passwort_data(passport_dict, row)
        else:
            if datenvalidation(passport_dict):
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
