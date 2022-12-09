from math import prod

with open("inputs/day08.txt") as file:
    data = [tuple(map(int, tuple(line.strip()))) for line in file]

# Part 1 ===
visible = [[False] * len(data[0]) for i in range(len(data))]
for y in range(len(data)):
    prev = -1
    for x in range(len(data[y])):
        if data[y][x] > prev:
            visible[y][x] = True
            prev = data[y][x]

    prev = -1
    for x in reversed(range(len(data[y]))):
        if data[y][x] > prev:
            visible[y][x] = True
            prev = data[y][x]

for x in range(len(data[0])):
    prev = -1
    for y in range(len(data)):
        if data[y][x] > prev:
            visible[y][x] = True
            prev = data[y][x]

    prev = -1
    for y in reversed(range(len(data))):
        if data[y][x] > prev:
            visible[y][x] = True
            prev = data[y][x]

part1 = sum(row.count(True) for row in visible)


# Part 2 ===
def score(x, y):
    scores = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        i = 0
        while True:
            i += 1
            if not (len(data) > y + dy * i >= 0 and len(data[0]) > x + dx * i >= 0):
                i -= 1
                break
            if not data[y][x] > data[y + dy * i][x + dx * i]:
                break
        scores.append(i)
    return prod(scores)


part2 = max(score(x, y) for y in range(len(data)) for x in range(len(data[0])))

print("Part 1:", part1)
print("Part 2:", part2)
