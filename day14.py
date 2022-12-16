with open("inputs/day14.txt") as file:
    data = [[tuple(map(int, coord.split(",")))
             for coord in line.split(" -> ")] for line in file]

# Part 1 & Part 2 ===
cave = [["."] * 1000 for i in range(1000)]
lowest = max(max(line, key=lambda x: x[1])[1] for line in data)

for line in data:
    for (x1, y1), (x2, y2) in zip(line, line[1:]):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cave[y][x1] = "#"
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                cave[y1][x] = "#"

for x in range(1000):
    cave[lowest+2][x] = "#"

part1, part2 = None, None
count = 0
x, y = 500, 0
while True:
    if y >= lowest and part1 is None:
        part1 = count
    if cave[0][500] == "o":
        part2 = count
        break

    if cave[y+1][x] == ".":
        y += 1
    elif cave[y+1][x-1] == ".":
        x -= 1
        y += 1
    elif cave[y+1][x+1] == ".":
        x += 1
        y += 1
    else:
        cave[y][x] = "o"
        count += 1
        x, y = 500, 0

print("Part 1:", part1)
print("Part 2:", part2)
