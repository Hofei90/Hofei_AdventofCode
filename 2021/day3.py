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


# ---- Teil 2 ---- '
def analyze_most_common_bit_oxygen(diagnostic_report, index):
    sum_numbers = len(diagnostic_report)
    high = 0
    for number in diagnostic_report:
        if int(number[index]):
            high += 1
    if high >= (sum_numbers / 2):
        keep = "1"
    else:
        keep = "0"
    new_report = []
    for number in diagnostic_report:
        if number[index] == keep:
            new_report.append(number)
    return new_report


def analyze_most_common_bit_cozwei(diagnostic_report, index):
    sum_numbers = len(diagnostic_report)
    high = 0
    for number in diagnostic_report:
        if int(number[index]):
            high += 1
    if high < (sum_numbers / 2):
        keep = "1"
    else:
        keep = "0"
    new_report = []
    for number in diagnostic_report:
        if number[index] == keep:
            new_report.append(number)
    return new_report


def main():
    diagnostic_report = INPUT1.read_text().splitlines()
    gamma_rate, epsilon_rate = analyze_most_common_bit(diagnostic_report)
    print(f"Power Consumption: {calc_power_consumption(gamma_rate, epsilon_rate)}")

    # Teil 2
    report = diagnostic_report

    index = 0
    while len(report) > 1:
        report = analyze_most_common_bit_oxygen(report, index)
        index += 1
    oxy = int(report[0], 2)

    report = diagnostic_report

    index = 0
    while len(report) > 1:
        report = analyze_most_common_bit_cozwei(report, index)
        index += 1
    co2 = int(report[0], 2)
    print(co2 * oxy)


if __name__ == "__main__":
    main()
