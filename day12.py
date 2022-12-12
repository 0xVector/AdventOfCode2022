with open("inputs/day12.txt") as file:
    data = [line.strip() for line in file]


def height(x_, y_):
    if data[y_][x_] == "S":
        return ord("a")
    elif data[y_][x_] == "E":
        return ord("z")
    else:
        return ord(data[y_][x_])


# Part 1 & Part 2 ===
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

start, end = None, None
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (x, y)
        elif data[y][x] == "E":
            end = (x, y)

queue, visited, shortest = [end], set(), {end: 0}
part2 = float("inf")
while queue:
    x, y = queue.pop(0)
    if (x, y) in visited:
        continue
    visited.add((x, y))

    for dx, dy in D:
        if 0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data)\
                and height(x, y) <= height(x+dx, y+dy) + 1:
            queue.append((x+dx, y+dy))
            shortest[(x+dx, y+dy)] = min(shortest[(x, y)] + 1,
                                         shortest.get((x+dx, y+dy), float("inf")))

            if data[y+dy][x+dx] in ("a", "S"):
                part2 = min(shortest[(x+dx, y+dy)], part2)

part1 = shortest[start]

print("Part 1:", part1)
print("Part 2:", part2)
