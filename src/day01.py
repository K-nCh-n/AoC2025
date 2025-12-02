from utils import *

instructions = read_input(1)

def part1():
    dial = 50
    count = 0
    for inst in instructions:
        dir = inst[0]
        val = int(inst[1:])
        dial = (dial + (1 if dir == 'R' else -1) * (val)) % 100
        if dial == 0:
            count += 1
    print(count)


def part2():
    dial = 50
    count = 0
    for inst in instructions:
        dir = inst[0]
        val = int(inst[1:])
        for i in range(val):
            dial = (dial + (1 if dir == 'R' else -1)) % 100
            if dial == 0:
                count += 1
    print(count)

part1()
part2()