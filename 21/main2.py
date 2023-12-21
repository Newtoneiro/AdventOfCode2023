import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

map = []


def dfs(start, ss):
    out = set()
    visited = set(start)
    q = deque([(start, ss)])

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
    return len(out)


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


def main_two():
    with open(filename) as f:
        for i, line in enumerate(f):
            row = []
            line = line.strip()
            for j, char in enumerate(line):
                if char == "S":
                    start = (i, j)
                row.append(char)
            map.append(row)

    size = len(map)
    steps = 26501365

    sr, sc = start

    map_width = steps // size - 1

    odd = (map_width // 2 * 2 + 1) ** 2
    even = ((map_width + 1) // 2 * 2) ** 2

    odd_points = dfs((sr, sc), size * 2 + 1)
    even_points = dfs((sr, sc), size * 2)

    corner_t = dfs((size - 1, sc), size - 1)
    corner_r = dfs((sr, 0), size - 1)
    corner_b = dfs((0, sc), size - 1)
    corner_l = dfs((sr, size - 1), size - 1)

    small_tr = dfs((size - 1, 0), size // 2 - 1)
    small_tl = dfs((size - 1, size - 1), size // 2 - 1)
    small_br = dfs((0, 0), size // 2 - 1)
    small_bl = dfs((0, size - 1), size // 2 - 1)

    large_tr = dfs((size - 1, 0), size * 3 // 2 - 1)
    large_tl = dfs((size - 1, size - 1), size * 3 // 2 - 1)
    large_br = dfs((0, 0), size * 3 // 2 - 1)
    large_bl = dfs((0, size - 1), size * 3 // 2 - 1)

    print(
        odd * odd_points +
        even * even_points +
        corner_t + corner_r + corner_b + corner_l +
        (map_width + 1) * (small_tr + small_tl + small_br + small_bl) +
        map_width * (large_tr + large_tl + large_br + large_bl)
    )


if __name__ == "__main__":
    main_two()
