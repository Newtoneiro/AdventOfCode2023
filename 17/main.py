import os
from collections import deque
from pprint import pprint

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

map = []


def get_neighbors(pos):
    out = []
    if pos[0] - 1 >= 0:
        out.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(map[pos[1]]):
        out.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0:
        out.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(map):
        out.append((pos[0], pos[1] + 1))
    return out


def must_change_direction(buffer):
    if len(buffer) < 3:
        return False, None
    if buffer[0][0] == buffer[1][0] == buffer[2][0]:
        return True, "v"
    if buffer[0][1] == buffer[1][1] == buffer[2][1]:
        return True, "h"
    return False, None


def main_one():
    weights = [[0 for _ in range(len(map[row]))] for row in range(len(map))]
    start = (len(map[-1]) - 1, len(map) - 1)
    visited = set()
    queue = deque([start])
    while len(queue) > 0:
        pos = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        neighbors = get_neighbors(pos)
        for neighbor in neighbors:
            queue.append(neighbor)
            if neighbor not in visited:
                weights[neighbor[1]][neighbor[0]] = \
                    weights[pos[1]][pos[0]] + map[pos[1]][pos[0]]

    path = deque([(0, 0)])
    buffer = deque(maxlen=3)
    while (len(map[-1]) - 1, len(map) - 1) not in path:
        pos = path[-1]
        neighbors = get_neighbors(pos)
        must, direction = must_change_direction(buffer)
        neighbors = [x for x in neighbors if x not in path]
        if must:
            if direction == "h":
                neighbors = [x for x in neighbors if x[1] != pos[1]]
            if direction == "v":
                neighbors = [x for x in neighbors if x[0] != pos[0]]
        next = min(neighbors, key=lambda x: weights[x[1]][x[0]])
        path.append(next)
        buffer.append(next)
    sum = 0
    for pos in path:
        sum += map[pos[1]][pos[0]]
        map[pos[1]][pos[0]] = 0
    print(sum)
    pprint(weights)
    pprint(map)


def main_two():
    pass


if __name__ == "__main__":
    with open(filename) as f:
        for line in f:
            map.append([int(x) for x in line.strip()])

    main_one()
    main_two()
