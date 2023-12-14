import ast
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def tilt_north(map):
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == "O":
                cur_row = i
                while cur_row > 0 and map[cur_row - 1][j] not in ['#', 'O']:
                    cur_row -= 1
                if cur_row != i:
                    map[cur_row][j], map[i][j] = "O", "."
    return map


def tilt_south(map):
    map = list(reversed(map))
    map = tilt_north(map)
    return list(reversed(map))


def tilt_west(map):
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == "O":
                cur_col = j
                while cur_col > 0 and map[i][cur_col - 1] not in ['#', 'O']:
                    cur_col -= 1
                if cur_col != j:
                    map[i][cur_col], map[i][j] = "O", "."
    return map


def tilt_east(map):
    map = [list(reversed(row)) for row in map]
    map = tilt_west(map)
    return [list(reversed(row)) for row in map]


def main_one():
    map = []
    with open(filename) as f:
        for line in f.readlines():
            map.append([*line.strip()])

    map = tilt_north(map)

    sum = 0
    score = len(map)
    for row in map:
        for element in row:
            if element == "O":
                sum += score
        score -= 1
    print(sum)


def main_two():
    positions = []
    map = []
    with open(filename) as f:
        for line in f.readlines():
            map.append([*line.strip()])

    loop_start = 0
    while True:
        map = tilt_north(map)
        map = tilt_west(map)
        map = tilt_south(map)
        map = tilt_east(map)
        key = str(map)
        if key not in positions:
            sum = 0
            score = len(map)
            for row in map:
                for element in row:
                    if element == "O":
                        sum += score
                score -= 1
            positions.append(key)
        else:
            loop_start = positions.index(key)
            break

    pos_nr = 1000000000 - len(positions) - 1
    positions = positions[loop_start:]
    pos_nr = pos_nr % len(positions)
    map = ast.literal_eval(positions[pos_nr])

    sum = 0
    score = len(map)
    for row in map:
        for element in row:
            if element == "O":
                sum += score
        score -= 1
    print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
