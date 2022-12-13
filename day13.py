from functools import cmp_to_key

with open("inputs/day13.txt") as file:
    pairs, pair = [], []
    for line in file:
        if len(line) > 1:
            pair.append(eval(line.strip()))
        if len(pair) == 2:
            pairs.append(tuple(pair))
            pair = []


def compare(l, r):
    if type(l) == int and type(r) == int:
        if l == r:
            return 0
        return 1 if l < r else -1

    elif type(l) == list and type(r) == list:
        for l_, r_ in zip(l, r):
            comp = compare(l_, r_)
            if comp != 0:
                return comp
        if len(l) == len(r):
            return 0
        return 1 if len(l) < len(r) else -1

    elif type(l) == list and type(r) == int:
        return compare(l, [r])
    elif type(l) == int and type(r) == list:
        return compare([l], r)


# Part 1 ===
part1 = 0
for i, (left, right) in enumerate(pairs, start=1):
    if compare(left, right) == 1:
        part1 += i


# Part 2 ===
part2 = 1
div_a, div_b = [[2]], [[6]]
packets = [packet for pair in pairs for packet in pair] + [div_a, div_b]
packets.sort(key=cmp_to_key(compare), reverse=True)
for i, packet in enumerate(packets, start=1):
    if packet == div_a or packet == div_b:
        part2 *= i


print("Part 1:", part1)
print("Part 2:", part2)
