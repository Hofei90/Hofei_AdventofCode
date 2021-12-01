import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def create_content(contents):
    bags = {}
    for content in contents:
        content = content.replace("bags", "").replace("bag", "").replace(".", "")
        content = content.strip()
        value = ""
        for count, char in enumerate(content):
            if char.isdigit():
                value = f"{value}{char}"
            else:
                break
        if value:
            value = int(value)
            bag = content[count:].replace("bags", "").replace("bag", "").strip().replace(" ", "_")
            bags.update({bag: value})
        else:
            bags = None
    return bags


def create_bags(rules_list):
    bags = {}
    for rule in rules_list:
        key = rule[0].replace("bags", "").replace("bag", "")
        key = key.strip()
        key = key.replace(" ", "_")
        contents = rule[1].split(",")
        bags[key] = create_content(contents)
    return bags


def create_rules(rules):
    rules_list = []
    for rule in rules:
        rules_list.append(rule.split("contain"))
    bags = create_bags(rules_list)
    return bags


def search_right_bag(search_bag, contain_bags, bags):
    # Durchsuche die Rücksäcke, ob ein Rucksack davon den goldenen Rucksack aufnehmen kann
    # wenn ja gib True zurück, ansonsten False
    for bag in contain_bags:
        if bags[bag] is None:
            continue
        # ja der Rucksack kann aufgenommen werden
        if search_bag in bags[bag].keys():
            return True
        else:
            # Wenn keiner den goldenen Rucksack aufnehmen kann, durchsuche, ob ein anderer Rucksack welcher enthalten ist
            # den goldenen Rucksack aufnehmen kann
            if search_right_bag(search_bag, bags[bag].keys(), bags):
                return True
    return False


def count_right_bag(search_bag, bags):
    """Zähle wie viele Rücksäcke meinen goldenen Rucksack aufnehmen können"""
    counter = 0
    for relevanter_bag in bags:
        # Nur Rucksäcke betrachten, die Rucksäcke aufnehmen können
        if not bags[relevanter_bag] is None:
            # Wenn der goldene Rucksack aufgenommen werden kann, erhöhe den Zähler auf 1, ansonsten durchsuche
            # ob die enthaltenen Rucksäcke den goldenen Rucksack aufnehmen können
            if search_bag in bags[relevanter_bag].keys():
                counter += 1
            else:
                if search_right_bag(search_bag, bags[relevanter_bag].keys(), bags):
                    counter += 1

    return counter


def calculate_individual_bags(contains_bags, bags, count_of_bags=1, sum_of_bags=None):
    if sum_of_bags is None:
        sum_of_bags = []
    for bag, value in contains_bags.items():
        sum_of_bags.append(count_of_bags * value)
        if bags[bag] is not None:
            sum_of_bags.extend(calculate_individual_bags(bags[bag], bags, count_of_bags * value))
    return sum_of_bags


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_7_1"))
    bags = create_rules(inhalt)
    counter = count_right_bag("shiny_gold", bags)
    print(f"Es können {counter} Beutel verwendet werden - Lösung Tag 7 Teil 1")

    my_bag_contains = bags["shiny_gold"]
    sum_idividual_bags = sum(calculate_individual_bags(my_bag_contains, bags))
    print(f"Es werden {sum_idividual_bags} Beutel benötigt - Lösung Tag 7 Teil 2")


if __name__ == "__main__":
    main()
