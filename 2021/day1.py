from pathlib import Path
import utils

SKRIPTPFAD = Path(__file__).parent
INPUT1 = SKRIPTPFAD / "input_1_1.txt"


def count_increasement(measurements):
    increased = 0
    previos_value = None
    for datum in measurements:
        datum = int(datum)
        if previos_value is None:
            previos_value = datum
            continue
        if datum > previos_value:
            increased += 1
        previos_value = datum
    return increased


def count_group_increasement(measurements):
    increased = 0
    end = 3
    previos_value = None
    for start, _ in enumerate(measurements):
        value = sum(measurements[start:end])
        if previos_value is None:
            pass
        elif value > previos_value:
            increased += 1
        previos_value = value
        end += 1
    return increased


def main():
    measurements = utils.read_input(INPUT1)
    print(f"Rätsel 1_1: Ergebnis: {count_increasement(measurements)}")
    print(f"Rätsel 1_2: Ergebnis: {count_group_increasement(measurements)}")


if __name__ == "__main__":
    main()
