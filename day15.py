
STARTNUMBERS = [8, 13, 1, 0, 18, 9]
TURNS = 2020


def speak_number(speeched_numbers, number, turn):
    try:
        speeched_numbers[number].append(turn)
    except KeyError:
        speeched_numbers[number] = [turn]


def get_last_turns(speeched_numbers, last_number):
    return speeched_numbers[last_number]


def calc_next_number(last_rounds):
    if len(last_rounds) <= 1:
        return 0
    else:
        return last_rounds[-1] - last_rounds[-2]


def main():
    speeched_numbers = {}
    number = STARTNUMBERS[0]
    for turn in range(1, TURNS + 1):
        if turn <= len(STARTNUMBERS):
            number = STARTNUMBERS[turn - 1]
            speak_number(speeched_numbers, number, turn)
        else:
            last_rounds = get_last_turns(speeched_numbers, number)
            number = calc_next_number(last_rounds)
            speak_number(speeched_numbers, number, turn)
    print(f"The 2020th number spoken is: {number})


if __name__ == "__main__":
    main()
