with open("inputs/day01.txt") as file:
    data = [[]]
    for line in file:
        if len(line.strip()) == 0:
            data.append([])
        else:
            data[-1].append(int(line.strip()))

# Part 1 ===
part1 = max(sum(x) for x in data)

# Part 2 ===
part2 = sum(sorted((sum(x) for x in data), reverse=True)[:3])

print("Part 1:", part1)
print("Part 2:", part2)
