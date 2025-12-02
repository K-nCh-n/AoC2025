from utils import read_input


ids = read_input(2)[0].split(",")
def part1():
    total = 0
    for id_range in ids:
        start, end = id_range.split('-')
        for i in range(int(start), int(end) + 1):
            id_string = str(i)
            half = len(id_string) // 2
            if id_string[:half] == id_string[half:]:
                total += i
    print(total)


def part2():
    total = 0
    for id_range in ids:
        start, end = id_range.split('-')
        for i in range(int(start), int(end) + 1):
            id_string = str(i)
            length = len(id_string)
            for len_interval in range(1, length//2 + 1):
                if id_string == id_string[:len_interval] * (length // len_interval):
                    print(id_string)
                    total += i
                    break
    print(total)

part1()
part2()