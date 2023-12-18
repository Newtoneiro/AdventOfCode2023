import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    DIRECTIONS = {
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0),
        "U": (-1, 0),
    }

    map = [(0, 0)]
    with open(filename) as f:
        cur_point = (0, 0)
        for line in f:
            direction, steps, color = line.strip().split()
            for i in range(int(steps)):
                cur_point = (
                    cur_point[0] + DIRECTIONS[direction][0],
                    cur_point[1] + DIRECTIONS[direction][1],
                )
                if cur_point not in map:
                    map.append(cur_point)
    x0, y0 = min(map, key=lambda x: x[0])[0], min(map, key=lambda x: x[1])[1]
    for i in range(len(map)):
        map[i] = (map[i][0] - x0, map[i][1] - y0)
    width, height = (
        max(map, key=lambda x: x[1])[1] + 1,
        max(map, key=lambda x: x[0])[0] + 1
    )

    full_map = [["." for _ in range(width)] for _ in range(height)]
    for pos in map:
        full_map[pos[0]][pos[1]] = "#"

    start = min(map, key=lambda x: x[0] + x[1])
    start = (start[0] + 1, start[1] + 1)

    def get_neighbors(point):
        neighbors = []
        for direction in DIRECTIONS.values():
            neighbor = (point[0] + direction[0], point[1] + direction[1])
            if 0 <= neighbor[0] < height and 0 <= neighbor[1] < width:
                neighbors.append(neighbor)
        return neighbors

    visited = set()
    q = deque([start])
    while len(q) > 0:
        cur_point = q.popleft()
        if cur_point in visited:
            continue
        visited.add(cur_point)
        for neighbor in get_neighbors(cur_point):
            if full_map[neighbor[0]][neighbor[1]] != "#":
                q.append(neighbor)
                full_map[neighbor[0]][neighbor[1]] = "#"

    sum = 0
    for row in full_map:
        sum += row.count("#")
    print(sum)


if __name__ == "__main__":
    main_one()
