import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

map = []


def dfs(prev, pos):
    out = []
    direction = "h" if prev[1] == pos[1] else "v"
    symbol = map[pos[1]][pos[0]]
    if direction == "h":
        course = "r" if pos[0] > prev[0] else "l"
        if symbol in [".", "-"]:
            if course == "r" and pos[0] + 1 < len(map[pos[1]]):
                out.append((pos[0] + 1, pos[1]))
            elif course == "l" and pos[0] - 1 >= 0:
                out.append((pos[0] - 1, pos[1]))
        elif symbol == "/":
            if course == "r" and pos[1] - 1 >= 0:
                out.append((pos[0], pos[1] - 1))
            elif course == "l" and pos[1] + 1 < len(map):
                out.append((pos[0], pos[1] + 1))
        elif symbol == "\\":
            if course == "r" and pos[1] + 1 < len(map):
                out.append((pos[0], pos[1] + 1))
            elif course == "l" and pos[1] - 1 >= 0:
                out.append((pos[0], pos[1] - 1))
        elif symbol == "|":
            if pos[1] + 1 < len(map):
                out.append((pos[0], pos[1] + 1))
            if pos[1] - 1 >= 0:
                out.append((pos[0], pos[1] - 1))
    elif direction == "v":
        course = "d" if pos[1] > prev[1] else "u"
        if symbol in [".", "|"]:
            if course == "d" and pos[1] + 1 < len(map):
                out.append((pos[0], pos[1] + 1))
            elif course == "u" and pos[1] - 1 >= 0:
                out.append((pos[0], pos[1] - 1))
        elif symbol == "/":
            if course == "d" and pos[0] - 1 >= 0:
                out.append((pos[0] - 1, pos[1]))
            elif course == "u" and pos[0] + 1 < len(map[pos[1]]):
                out.append((pos[0] + 1, pos[1]))
        elif symbol == "\\":
            if course == "d" and pos[0] + 1 < len(map[pos[1]]):
                out.append((pos[0] + 1, pos[1]))
            elif course == "u" and pos[0] - 1 >= 0:
                out.append((pos[0] - 1, pos[1]))
        elif symbol == "-":
            if pos[0] + 1 < len(map[pos[1]]):
                out.append((pos[0] + 1, pos[1]))
            if pos[0] - 1 >= 0:
                out.append((pos[0] - 1, pos[1]))
    return out


def main_one():
    queue = deque([[(-1, 0), (0, 0)]])
    visited = set()
    while len(queue) > 0:
        prev, pos = queue.popleft()
        if (prev, pos) in visited:
            continue
        visited.add((prev, pos))
        for next_pos in dfs(prev, pos):
            queue.append((pos, next_pos))

    print(len(set(x[1] for x in visited)))


def main_two():
    start_upper = [
        [(x, -1), (x, 0)] for x in range(len(map[0]))
    ]
    start_bottom = [
        [(x, len(map)), (x, len(map) - 1)] for x in range(len(map[-1]))
    ]
    start_left = [
        [(-1, y), (0, y)] for y in range(len(map))
    ]
    start_right = [
        [(len(map[y]), y), (len(map[y]) - 1, y)] for y in range(len(map))
    ]

    best = 0
    for start in start_upper + start_bottom + start_left + start_right:
        queue = deque([start])
        visited = set()
        while len(queue) > 0:
            prev, pos = queue.popleft()
            if (prev, pos) in visited:
                continue
            visited.add((prev, pos))
            for next_pos in dfs(prev, pos):
                queue.append((pos, next_pos))
        score = len(set(x[1] for x in visited))
        if score > best:
            best = score
    print(best)


if __name__ == "__main__":
    with open(filename) as f:
        for line in f:
            map.append([x for x in line.strip()])

    main_one()
    main_two()
