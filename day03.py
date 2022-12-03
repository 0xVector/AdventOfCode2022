with open("inputs/day03.txt") as file:
    data = [line.strip() for line in file]


def priority(ch):
    if ch.islower():
        return ord(ch) - ord("a") + 1
    return ord(ch) - ord("A") + 27


# Part 1 ===
compartments = [(line[:len(line)//2], line[len(line)//2:]) for line in data]
part1 = sum(priority(set(line[0]).intersection(set(line[1])).pop()) for line in compartments)

# Part 2 ===
part2 = 0
for i in range(0, len(data), 3):
    part2 += priority(set(data[i]).intersection(set(data[i + 1])).intersection(set(data[i + 2])).pop())

print("Part 1:", part1)
print("Part 2:", part2)
