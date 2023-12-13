import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def count_difs(str1, str2):
    return sum([1 for i in range(len(str1)) if str1[i] != str2[i]])


def find_horizontal(my_map):
    buffer = deque([my_map[0]])
    for i, row in enumerate(my_map[1:]):
        is_mirrored = True
        found_smudge = False
        for mirror, real in zip(reversed(buffer), my_map[i + 1:]):
            if not found_smudge and count_difs(mirror, real) == 1:
                found_smudge = True
            elif mirror != real:
                is_mirrored = False
        if not is_mirrored:
            buffer.append(row)
            continue
        elif found_smudge:
            return (i + 1)
    return 0


def find_vertical(my_map):
    my_map = list(map(list, zip(*my_map)))  # Transpose
    my_map = [''.join(row) for row in my_map]  # Join
    return find_horizontal(my_map)


def main_two():
    maps = []
    with open(filename) as f:
        lines = f.read()
        flat_maps = lines.split("\n\n")
        for flat_map in flat_maps:
            maps.append(flat_map.split("\n"))

    sum = 0
    for map in maps:
        h = find_horizontal(map) * 100
        sum += h
        if h == 0:
            sum += find_vertical(map)
    print(sum)


if __name__ == "__main__":
    main_two()
