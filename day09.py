with open("inputs/day09.txt") as file:
    data = [(line.split()[0], int(line.split()[1])) for line in file]


def vector(move_, size):
    direction = 1 if move_ in ("R", "D") else -1
    x, y = 0, 0
    if move_ in ("R", "L"):
        x = size*direction
    else:
        y = size*direction
    return x, y


def touching(ax, ay, bx, by):
    return abs(ax-bx) <= 1 and abs(ay - by) <= 1


def solve(length):
    knots = [(0, 0) for _ in range(length)]
    visited = {(0, 0)}

    for direction, size in data:
        head = knots[0]
        head_move = vector(direction, size)

        while abs(head_move[0]) or abs(head_move[1]):

            if sum(head_move) > 0:
                sign = 1
            else:
                sign = -1

            # Move the head
            if abs(head_move[0]):
                head_move = (head_move[0]-1*sign, head_move[1])
                knots[0] = (knots[0][0]+1*sign, knots[0][1])
            else:
                head_move = (head_move[0], head_move[1]-1*sign)
                knots[0] = (knots[0][0], knots[0][1]+1*sign)

            # Move the rest
            while True:
                for i in range(1, len(knots)):
                    head_x, head_y = knots[i-1]
                    tail_x, tail_y = knots[i]
                    if touching(head_x, head_y, tail_x, tail_y):
                        break

                    # Same row
                    if head_y == tail_y:
                        while tail_x + 1 < head_x:
                            tail_x += 1
                        while head_x + 1 < tail_x:
                            tail_x -= 1

                    # Same col
                    elif head_x == tail_x:
                        while tail_y + 1 < head_y:
                            tail_y += 1
                        while head_y + 1 < tail_y:
                            tail_y -= 1

                    else:
                        sign_x = 1 if tail_x < head_x else -1
                        sign_y = 1 if tail_y < head_y else -1
                        tail_x += 1 * sign_x
                        tail_y += 1 * sign_y

                    knots[i] = (tail_x, tail_y)
                    if i == len(knots) - 1:
                        visited.add((tail_x, tail_y))

                if touching(knots[0][0], knots[0][1], knots[1][0], knots[1][1]):
                    break

    return len(visited)


# Part 1 ===
part1 = solve(2)

# Part 2 ===
part2 = solve(10)


print("Part 1:", part1)
print("Part 2:", part2)
