import os

SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))


class Memory:
    def __init__(self):
        self.mem = {}

    def create_new_bits(self, addr):
        self.mem[addr] = [[0] * 36]

    def write_value(self, addr, value, mask):
        if addr not in self.mem:
            self.create_new_bits(addr)
        bit_value = bin(int(value))
        bit_value = bit_value.replace("0b", "")
        bit_value = create_bit_muster(bit_value, mask)
        new_value = []
        for bit, marker in zip(bit_value, mask):
            if marker == "X":
                new_value.append(bit)
            else:
                new_value.append(marker)
        self.mem[addr] = new_value

    def get_all_values(self):
        values = []
        for key, value in self.mem.items():
            bit_value = ""
            for bit in value:
                bit_value = f"{bit_value}{bit}"
            values.append(int(f"0b{bit_value}", 2))
        return values


def read_input(datei):
    with open(datei) as file:
        inhalt = file.readlines()
    return inhalt


def create_bit_muster(bit_value, mask):
    diff = len(mask) - len(bit_value)
    bit_value = f"{'0' * diff}{bit_value}"
    return bit_value


def get_new_mask(mask):
    mask = mask.split("=")[1].strip()
    return mask


def get_new_addr(line):
    addr = line.split("=")[0].strip()
    addr = addr.replace("mem[", "").replace("]", "").strip()
    return addr


def get_new_value(line):
    value = line.split("=")[1].strip()
    return value


def main():
    inhalt = read_input(os.path.join(SKRIPTPFAD, "input_14"))
    memory = Memory()
    for zeile in inhalt:
        zeile = zeile.strip()
        if zeile.startswith("mask"):
            mask = get_new_mask(zeile)
        else:
            addr = get_new_addr(zeile)
            value = get_new_value(zeile)
            memory.write_value(addr, value, mask)
    values = memory.get_all_values()
    print(sum(values))


if __name__ == "__main__":
    main()
