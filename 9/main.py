import os
from collections import deque


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            values = deque([int(x) for x in line.split()])
            extrapolations = deque([values])
            while not all([x == 0 for x in extrapolations[-1]]):
                new_row = deque()
                for i in range(1, len(extrapolations[-1])):
                    new_row.append(
                        extrapolations[-1][i] - extrapolations[-1][i - 1]
                    )
                extrapolations.append(new_row)
            extrapolations[-1].append(0)
            for i in reversed(range(len(extrapolations) - 1)):
                extrapolations[i].append(
                    extrapolations[i][-1] + extrapolations[i + 1][-1])
            sum += extrapolations[0][-1]
    print(sum)


def main_two():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            values = deque([int(x) for x in line.split()])
            extrapolations = deque([values])
            while not all([x == 0 for x in extrapolations[-1]]):
                new_row = deque()
                for i in range(1, len(extrapolations[-1])):
                    new_row.append(
                        extrapolations[-1][i] - extrapolations[-1][i - 1]
                    )
                extrapolations.append(new_row)
            extrapolations[-1].appendleft(0)

            for i in reversed(range(len(extrapolations) - 1)):
                extrapolations[i].appendleft(
                    extrapolations[i][0] - extrapolations[i + 1][0])
            sum += extrapolations[0][0]
    print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
