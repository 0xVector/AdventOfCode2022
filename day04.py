with open("inputs/day04.txt") as file:
    data = []
    for line in file:
        line = line.split(",")
        data.append(tuple(map(lambda x: tuple(map(int, x.split("-"))), line)))

# Part 1 ===
part1 = sum(1 if a[0] <= b[0] <= b[1] <= a[1] or b[0] <= a[0] <= a[1] <= b[1] else 0
            for a, b in data)

# Part 2 ===
part2 = sum(1 if any((a[0] <= b[0] <= a[1],
            a[0] <= b[1] <= a[1],
            b[0] <= a[0] <= b[1],
            b[0] <= a[1] <= b[1])) else 0 for a, b in data)

print("Part 1:", part1)
print("Part 2:", part2)
