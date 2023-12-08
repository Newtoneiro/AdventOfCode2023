import os
import itertools
import math

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

path_to_index = {
    "L": 0,
    "R": 1,
}


def main_one():
    with open(filename) as f:
        direction_dir = {}
        path = [path_to_index[x] for x in f.readline().strip()]
        f.readline()
        for line in f.readlines():
            line = line.strip()
            key, rest = line.split(" = ")
            directions = rest.strip("(").strip(")").split(", ")
            direction_dir[key] = directions

    cur_node = "AAA"
    steps = 0
    for elem in itertools.cycle(path):
        if cur_node == "ZZZ":
            print(steps)
            break
        cur_node = direction_dir[cur_node][elem]
        steps += 1


def main_two():
    cur_nodes = []
    with open(filename) as f:
        direction_dir = {}
        path = [path_to_index[x] for x in f.readline().strip()]
        f.readline()
        for line in f.readlines():
            line = line.strip()
            key, rest = line.split(" = ")
            if key.endswith("A"):
                cur_nodes.append(key)
            directions = rest.strip("(").strip(")").split(", ")
            direction_dir[key] = directions

    steps = []
    for cur_node in cur_nodes:
        cur_steps = 0
        for elem in itertools.cycle(path):
            if cur_node.endswith("Z"):
                break

            cur_node = direction_dir[cur_node][elem]
            cur_steps += 1
        steps.append(cur_steps)
    print(math.lcm(*steps))  # Least common multiple


if __name__ == "__main__":
    # main_one()
    main_two()
