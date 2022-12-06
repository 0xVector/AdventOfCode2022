with open("inputs/day06.txt") as file:
    data = file.readline()


def find(length):
    return next((i for i in range(length, len(data)+1) if len(set(data[i-length:i])) == length))


# Part 1 ===
part1 = find(4)

# Part 2 ===
part2 = find(14)

print("Part 1:", part1)
print("Part 2:", part2)
