with open("inputs/day10.txt") as file:
    data = []
    for line in file:
        line = line.split()
        if len(line) == 2:
            data.append((line[0], int(line[1])))
        else:
            data.append((line[0], None))

# Part 1 & 2 ===
part1 = 0
screen = [[" "]*40 for _ in range(6)]
cycle, register = 0, 1
i = 0
is_executing = False
while True:
    cycle += 1
    opcode, value = data[i]

    if (cycle - 20) % 40 == 0:
        part1 += cycle * register

    if (cycle-1) % 40 in range(register-1, register+2):
        screen[(cycle-1)//40][(cycle-1) % 40] = "#"

    if not is_executing:
        if opcode == "addx":
            is_executing = True
        else:  # noop
            i += 1
    else:
        is_executing = not is_executing
        register += data[i][1]
        i += 1

    if i + 1 >= len(data):
        break


print("Part 1:", part1)
print("Part 2:")
[print("".join(line)) for line in screen]
