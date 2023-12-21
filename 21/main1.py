import os
from pprint import pprint
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

map = []


def get_neighbors(x, y):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(map) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(map[0]) - 1:
        neighbors.append((x, y + 1))
    return neighbors


def main_one():
    start = ()
    with open(filename) as f:
        for i, line in enumerate(f):
            row = []
            line = line.strip()
            for j, char in enumerate(line):
                if char == "S":
                    start = (i, j)
                row.append(char)
            map.append(row)
    out = set()
    visited = set(start)
    q = deque([(start, 64)])
    while len(q) > 0:
        pos, depth = q.popleft()
        if depth % 2 == 0:
            out.add(pos)
        if depth == 0:
            continue

        neighbors = get_neighbors(*pos)
        for neighbor in neighbors:
            if neighbor not in visited and \
                  map[neighbor[1]][neighbor[0]] in [".", "S"]:
                visited.add(neighbor)
                q.append((neighbor, depth - 1))
    pprint(len(out))


if __name__ == "__main__":
    main_one()
