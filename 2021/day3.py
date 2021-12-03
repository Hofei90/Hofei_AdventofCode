from pathlib import Path

SKRIPTPFAD = Path(__file__).parent
INPUT1 = SKRIPTPFAD / "input_3_1.txt"


def generate_int(rate):
    str_ = "".join(str(bit) for bit in rate)
    return int(str_, 2)



def calc_power_consumption(gamma_rate, epsilon_rate):
    gamma_rate = generate_int(gamma_rate)
    epsilon_rate = generate_int(epsilon_rate)
    return gamma_rate * epsilon_rate


def generate_rates(sum_numbers, high_counter):
    gamma_rate = []
    epsilon_rate = []

    for common_bit in high_counter:
        if common_bit > sum_numbers / 2:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)
    return gamma_rate, epsilon_rate


def analyze_most_common_bit(diagnostic_report):
    sum_numbers = len(diagnostic_report)
    high_counter = [0] * len(diagnostic_report[0])
    for number in diagnostic_report:
        for position, bit in enumerate(number):
            high_counter[position] = high_counter[position] + int(bit)
    return generate_rates(sum_numbers, high_counter)


def main():
    diagnostic_report = INPUT1.read_text().splitlines()
    gamma_rate, epsilon_rate = analyze_most_common_bit(diagnostic_report)
    print(f"Power Consumption: {calc_power_consumption(gamma_rate, epsilon_rate)}")



if __name__ == "__main__":
    main()