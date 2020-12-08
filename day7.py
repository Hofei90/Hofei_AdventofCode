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
    for bag in contain_bags:
        if bags[bag] is None:
            return False
        print(bags[bag].keys())
        if search_bag in bags[bag].keys():
            return True
        else:
            if search_right_bag(search_bag, bags[bag].keys(), bags):
                return True
    return False


def count_right_bag(search_bag, bags):
    counter = 0
    for relevanter_bag in bags:
        if bags[relevanter_bag] is None:
            if search_bag == relevanter_bag:
                counter += 1
            continue
        else:
            print(bags[relevanter_bag].keys())
            if search_bag == relevanter_bag:
                counter += 1
            elif search_bag in bags[relevanter_bag].keys():
                counter += 1
            else:
                if search_right_bag(search_bag, bags[relevanter_bag].keys(), bags):
                    counter += 1

    print(counter)


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_7_1"))
    bags = create_rules(inhalt)
    count_right_bag("shiny_gold", bags)


if __name__ == "__main__":
    main()
