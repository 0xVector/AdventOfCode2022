from dataclasses import dataclass, field
from copy import deepcopy


@dataclass
class Monkey:
    op: str
    test: int
    true: int
    false: int
    items: list[int] = field(default_factory=list)
    inspected: int = 0


with open("inputs/day11.txt") as file:
    monkeys = []
    m = 1
    starting, op, test, true, false = None, None, None, None, None
    for line in file:
        line = line.strip().split(":")
        if "Monkey" in line[0]:
            continue
        elif "Starting" in line[0]:
            starting = list(map(int, line[1].strip().split(", ")))
        elif "Operation" in line[0]:
            op = line[1].split("=")[1].strip()
        elif "Test" in line[0]:
            test = int(line[1].split()[2])
            m *= int(line[1].split()[2])
        elif "true" in line[0]:
            true = int(line[1].split()[3])
        elif "false" in line[0]:
            false = int(line[1].split()[3])
        else:
            monkeys.append(Monkey(op, test, true, false, starting))
    monkeys.append(Monkey(op, test, true, false, starting))


def solve(rounds, divide_by_3):
    monkeys_ = deepcopy(monkeys)
    for _ in range(rounds):
        for monkey in monkeys_:
            while monkey.items:
                item = monkey.items.pop(0)
                item = eval(monkey.op.replace("old", str(item)))
                item = item//3 if divide_by_3 else item % m
                target = monkeys_[monkey.true] if item % monkey.test == 0 else monkeys_[monkey.false]
                target.items.append(item)
                monkey.inspected += 1
    monkeys_.sort(key=lambda x: x.inspected, reverse=True)
    return monkeys_[0].inspected * monkeys_[1].inspected


# Part 1 ===
part1 = solve(20, True)

# Part 2 ===
part2 = solve(10_000, False)


print("Part 1:", part1)
print("Part 2:", part2)
