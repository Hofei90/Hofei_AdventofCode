STARTNUMBERS = [8, 13, 1, 0, 18, 9]
TURNS_1 = 2020
TURNS_2 = 30000000


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


def play_game(startnumbers, max_turns):
    speeched_numbers = {}
    number = startnumbers[0]
    for turn in range(1, max_turns + 1):
        if turn <= len(startnumbers):
            number = startnumbers[turn - 1]
            speak_number(speeched_numbers, number, turn)
        else:
            last_rounds = get_last_turns(speeched_numbers, number)
            number = calc_next_number(last_rounds)
            speak_number(speeched_numbers, number, turn)
    return number


def main():
    print(f"The {TURNS_1}th number spoken is: {play_game(STARTNUMBERS, TURNS_1)}")
    print(f"The {TURNS_2}th number spoken is: {play_game(STARTNUMBERS, TURNS_2)}")


if __name__ == "__main__":
    main()
