with open("inputs/day07.txt") as file:
    data = {}
    current_dir = data
    parent = current_dir
    for line in file:
        line = line.split()

        if line[0] == "$":
            if line[1] == "cd":
                if line[2] not in current_dir:
                    current_dir[line[2]] = {}
                    current_dir[line[2]][".."] = current_dir

                if line[2] == "/":
                    current_dir = data["/"]
                else:
                    current_dir = current_dir[line[2]]

            else:  # ls
                continue

        else:  # dir / file
            if line[0] == "dir":
                if line[1] not in current_dir:
                    current_dir[line[1]] = {}
                    current_dir[line[1]][".."] = current_dir
            else:
                current_dir[line[1]] = {"size": int(line[0])}


def solve1(d):
    total = 0
    this = 0
    if "size" in d:
        return d["size"], 0
    for k, v in d.items():
        if k == "..":
            continue
        s, st = solve1(v)
        this += s
        total += st
    if this <= 100000:
        total += this
    return this, total


def size(d):
    if "size" in d:
        return d["size"]
    return sum(size(d[i]) for i in d if i != "..")


def solve2(d):
    this, best = 0, float("inf")
    if "size" in d:
        return d["size"], float("inf")

    for k, v in d.items():
        if k == "..":
            continue
        s, b = solve2(d[k])
        best = min(best, b)
        this += s
    if this >= need:
        best = min(best, this)
    return this, best


# Part 1 ===
part1 = solve1(data)[1]

# Part 2 ===
TOTAL = 70000000
REQUIRED = 30000000
need = REQUIRED - (TOTAL - size(data))
part2 = solve2(data)[1]

print("Part 1:", part1)
print("Part 2:", part2)
