import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
        inhalt.append("")
    return inhalt


def read_group_answers_1(inhalt):
    groups_answers = []
    answers = []
    for group_answer in inhalt:
        group_answer = group_answer.strip()
        if group_answer:
            for answer in group_answer:
                answers.append(answer)
        else:
            groups_answers.append(set(answers))
            answers = []
    return groups_answers


def read_group_answers_2(inhalt):
    counters = []
    antwort_set_1 = {chr(i) for i in range(ord("a"), ord("z") + 1)}
    for gruppen_antwort in inhalt:
        gruppen_antwort = gruppen_antwort.strip()
        if gruppen_antwort:
            antwort_set_2 = {antwort for antwort in gruppen_antwort}
            if len(antwort_set_2) > 0:
                antwort_set_1 = antwort_set_1 & antwort_set_2
        else:
            counters.append(len(antwort_set_1))
            antwort_set_1 = {chr(i) for i in range(ord("a"), ord("z") + 1)}
    return counters


def count_answers(groups_answers):
    counters = []
    for answers in groups_answers:
        counters.append(len(answers))
    return counters


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_6_1"))
    groups_answers = read_group_answers_1(inhalt)
    counters = count_answers(groups_answers)
    print(f"Solution of Day 6 #1: {sum(counters)}")

    counters = read_group_answers_2(inhalt)
    print(f"Solution of Day 6 #2: {sum(counters)}")


if __name__ == "__main__":
    main()
