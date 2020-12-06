import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
        inhalt.append("")
    return inhalt


def read_group_answers(inhalt, part_1=False, part_2=False):
    groups_answers = []
    answers = []
    for group_answer in inhalt:
        group_answer = group_answer.strip()
        if group_answer:
            for answer in group_answer:
                answers.append(answer)
        else:
            if part_1:
                groups_answers.append(set(answers))
            elif part_2:
                pass
            else:
                raise ValueError
            answers = []
    return groups_answers


def count_answers(groups_answers):
    counters = []
    for answers in groups_answers:
        counters.append(len(answers))
    return counters


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_6_1"))
    groups_answers = read_group_answers(inhalt, part_1=True)
    counters = count_answers(groups_answers)
    print(f"Solution of Day 1 #1: {sum(counters)}")

    groups_answers = read_group_answers(inhalt, part_2=True)
    counters = count_answers(groups_answers)
    print(f"Solution of Day 1 #2: {sum(counters)}")


if __name__ == "__main__":
    main()