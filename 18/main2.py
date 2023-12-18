import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_two():
    DIRECTIONS = {
        0: (0, 1),
        2: (0, -1),
        1: (1, 0),
        3: (-1, 0),
    }

    map = [(0, 0)]
    border = 0
    with open(filename) as f:
        cur_point = (0, 0)
        for line in f:
            _, _, color = line.strip().split()
            color = color.strip('(').strip(')')
            direction, steps = color[-1], color[1:-1]
            direction = int(direction, 16)
            steps = int(steps, 16)
            print(direction, steps)

            steps = int(steps)
            border += steps
            cur_point = (
                cur_point[0] + DIRECTIONS[direction][0] * steps,
                cur_point[1] + DIRECTIONS[direction][1] * steps,
            )
            map.append(cur_point)

    # Shoelace formula
    area = abs(sum(map[i][0] * (map[i - 1][1] - map[(i + 1) % len(map)][1])
               for i in range(len(map)))) // 2
    inside = area - border // 2 + 1

    print(inside + border)


if __name__ == "__main__":
    main_two()
