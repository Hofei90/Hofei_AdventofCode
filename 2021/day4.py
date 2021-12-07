from pathlib import Path
from sys import exit

SKRIPTPFAD = Path(__file__).parent
INPUT1 = SKRIPTPFAD / "input_4_1.txt"


def create_bingo_felder(daten):
    bingo_felder = []
    bingo_feld = []
    for zahlenreihe in daten:
        if zahlenreihe:
            zahlen = zahlenreihe.split()
            zeile = [[int(zahl), False] for zahl in zahlen]
            bingo_feld.append(zeile)
        else:
            bingo_felder.append(bingo_feld)
            bingo_feld = []
    else:
        bingo_felder.append(bingo_feld)
    return bingo_felder


def setze_zahl(zahl, bingo_felder):
    for bingo_feld in bingo_felder:
        for zeile in bingo_feld:
            for position in zeile:
                if position[0] == zahl:
                    position[1] = True


def create_gewinner_vertikal(index, bingo):
    gewinner = []
    for zeile in bingo:
        gewinner.append(zeile[index][0])
    return gewinner


def check_bingo_felder(bingo_felder):
    for feld_nummer, bingo_feld in enumerate(bingo_felder):
        spalten = [True] * len(bingo_felder[0][0])
        for zeile in bingo_feld:
            if all(position[1] for position in zeile):
                return bingo_feld, feld_nummer
            for spalte, position in enumerate(zeile):
                spalten[spalte] = spalten[spalte] and position[1]
        try:
            _ = spalten.index(True)
        except ValueError:
            pass
        else:
            return bingo_feld, feld_nummer
    return None, None


def calc_solution(bingo, gewinner):
    unmarkiert = 0
    for zeile in bingo:
        for position in zeile:
            if not position[1]:
                unmarkiert += position[0]
    return sum(gewinner) * unmarkiert


def main():
    #daten = INPUT_EXAMPLE.read_text().splitlines()
    daten = INPUT1.read_text().splitlines()
    zahlen = daten[0].split(",")
    daten = daten[2:]
    bingo_felder = create_bingo_felder(daten)
    for zahl in zahlen:
        setze_zahl(int(zahl), bingo_felder)
        bingo, _ = check_bingo_felder(bingo_felder)
        if bingo is not None:
            print(calc_solution(bingo, [int(zahl)]))
            break

    # Teil 2
    bingo_felder = create_bingo_felder(daten)
    for zahl in zahlen:
        setze_zahl(int(zahl), bingo_felder)
        bingo = False
        while bingo is not None:
            bingo, position_gewinner_feld = check_bingo_felder(bingo_felder)
            if bingo is not None:
                if len(bingo_felder) == 1:
                    print(calc_solution(bingo, [int(zahl)]))
                    exit(0)
                else:
                    bingo_felder.pop(position_gewinner_feld)


if __name__ == "__main__":
    main()
