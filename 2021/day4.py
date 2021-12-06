from pathlib import Path

SKRIPTPFAD = Path(__file__).parent
INPUT_EXAMPLE = SKRIPTPFAD / "input_4_1_test.txt"
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
    return bingo_felder


def create_gewinner_vertikal(index, bingo):
    gewinner = []
    for zeile in bingo:
        gewinner.append(zeile[index][0])
    return gewinner


def check_bingo_felder(bingo_felder):
    for bingo_feld in bingo_felder:
        spalten = [True] * len(bingo_felder[0][0])
        for zeile in bingo_feld:
            if all(position[1] for position in zeile):
                gewinner = [zahl[0] for zahl in zeile]
                return bingo_feld, gewinner
            for spalte, position in enumerate(zeile):
                if not spalten[spalte] or not position[1]:
                    spalten[spalte] = False
        try:
            gewinner_spalte = spalten.index(True)
        except ValueError:
            pass
        else:
            gewinner = create_gewinner_vertikal(gewinner_spalte, bingo_feld)
            return bingo_feld, gewinner
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
        bingo_felder = setze_zahl(int(zahl), bingo_felder)
        bingo, gewinner = check_bingo_felder(bingo_felder)
        if bingo is not None:
            print(calc_solution(bingo, [int(zahl)]))
            break


if __name__ == "__main__":
    main()
