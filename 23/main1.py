import os
from pprint import pprint
import sys
sys.setrecursionlimit(99999)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

slopes = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

map = []

def get_neighbors(pos):
    if map[pos[0]][pos[1]] in slopes.keys():
        next = slopes[map[pos[0]][pos[1]]]
        return [(pos[0] + next[0], pos[1] + next[1])]
    
    neighbors = []
    if pos[0] > 0:
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] < len(map) - 1:
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] < len(map[0]) - 1:
        neighbors.append((pos[0], pos[1] + 1))

    neighbors = [n for n in neighbors if map[n[0]][n[1]] != "#"]
    return neighbors


def dfs(next, end, visited=set()):
    all_paths = []
    for n in get_neighbors(next):
        n_visited = visited.copy()
        if n in visited:
            continue
        n_visited.add(n)
        if n == end:
            all_paths.append(tuple(sorted(n_visited)))
        else:
            all_paths.append([p for p in dfs(n, end, n_visited)])
    return max(all_paths, key=len) if all_paths else []


def main_one():
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            map.append([char for char in line])
    start = (0, map[0].index("."))
    end = (len(map) - 1, map[-1].index("."))
    path = dfs(start, end)
    pprint(len(path))
    

if __name__ == "__main__":  
    main_one()
