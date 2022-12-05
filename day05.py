with open("inputs/day05.txt") as file:
    stacks, moves = [], []
    for line in file:
        if "[" in line:
            for stack_i, i in enumerate(range(1, len(line), 4)):
                if line[i].isalpha():
                    while len(stacks) <= stack_i:
                        stacks.append([])
                    stacks[stack_i].append(line[i])
        elif "move" in line:
            move = line.split()
            moves.append(tuple(map(int, (move[1], move[3], move[5]))))

# Part 1 ===
stacks1 = [stack.copy() for stack in stacks]
for count, from_, to in moves:
    stacks1[to-1] = list(reversed(stacks1[from_-1][:count])) + stacks1[to-1]
    stacks1[from_-1] = stacks1[from_-1][count:]
part1 = "".join(stack[0] for stack in stacks1)


# Part 2 ===
for count, from_, to in moves:
    stacks[to-1] = stacks[from_-1][:count] + stacks[to-1]
    stacks[from_-1] = stacks[from_-1][count:]
part2 = "".join(stack[0] for stack in stacks)

print("Part 1:", part1)
print("Part 2:", part2)
