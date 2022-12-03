with open("inputs/day02.txt") as file:
    data = [line.split() for line in file if line.strip()]

# Part 1 ===
MY_SCORE = {"X": 1, "Y": 2, "Z": 3}
MY_WINS = {"X": "C", "Y": "A", "Z": "B"}
PAIRINGS = {"X": "A", "Y": "B", "Z": "C"}
part1 = 0
for round_ in data:
    part1 += MY_SCORE[round_[1]]
    if MY_WINS[round_[1]] == round_[0]:
        part1 += 6
    elif PAIRINGS[round_[1]] == round_[0]:
        part1 += 3

# Part 2 ===
MY_WINS.update({v: k for k, v in MY_WINS.items()})
PAIRINGS.update({v: k for k, v in PAIRINGS.items()})
part2 = 0
for round_ in data:
    my_play = None
    if round_[1] == "Z":
        my_play = MY_WINS[round_[0]]
        part2 += 6
    elif round_[1] == "X":
        x = {"X", "Y", "Z"}
        x.remove(MY_WINS[round_[0]])
        x.remove(PAIRINGS[round_[0]])
        my_play = x.pop()
    else:
        my_play = PAIRINGS[round_[0]]
        part2 += 3

    part2 += MY_SCORE[my_play]

print("Part 1:", part1)
print("Part 2:", part2)
