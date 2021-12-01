def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return [int(value) for value in inhalt]