""""Quelle des Ausgangscodes: https://www.reddit.com/r/adventofcode/comments/r9824c/comment/hnullh0/?utm_source=share&utm_medium=web2x&context=3
"""

from pathlib import Path
from collections import Counter


SKRIPTPFAD = Path(__file__).parent
INPUT1 = SKRIPTPFAD / "input_5_1.txt"


def read_input(file):
    with open(file) as f:
        segments = [line.replace(' -> ', ',') for line in f.read().split('\n')]
    return segments


def erstelle_schnittkarte(segments, include_diagonal):
    straight, diagonal = [], []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2:
            straight += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        elif y1 < y2:
            diagonal += [(x, y1 + idx) for idx, x in enumerate(range(x1, x2 + 1))]
        else:
            diagonal += [(x, y1 - idx) for idx, x in enumerate(range(x1, x2 + 1))]
    position_counts = Counter(straight)
    if include_diagonal:
        position_counts += Counter(diagonal)
    return sum(v > 1 for v in position_counts.values())


def main():
    segments = read_input(INPUT1)
    print(erstelle_schnittkarte(segments, include_diagonal=False))
    print(erstelle_schnittkarte(segments, include_diagonal=True))


if __name__ == "__main__":
    main()
