import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            cur_num = [0, 0]
            for char in line:
                if char.isnumeric():
                    cur_num[0] = int(char)
                    break
            for char in reversed(line):
                if char.isnumeric():
                    cur_num[1] = int(char)
                    break
            sum += int(f"{cur_num[0]}{cur_num[1]}")
    print(sum)


def main_two():
    number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            cur_num = [0, 0]

            buffer = deque(maxlen=5)
            for char in line:
                cur_buffer = "".join(buffer)
                if any([cur_buffer.endswith(key) for key in number_dict.keys()]):
                    for key in number_dict.keys():
                        if cur_buffer.endswith(key):
                            found_key = key
                            break
                    cur_num[0] = number_dict[found_key]
                    break
                if char.isnumeric():
                    cur_num[0] = int(char)
                    break
                buffer.append(char)

            rev_buffer = deque(maxlen=5)
            for char in reversed(line):
                cur_buffer = "".join(rev_buffer)
                if any([cur_buffer.startswith(key) for key in number_dict.keys()]):
                    for key in number_dict.keys():
                        if cur_buffer.startswith(key):
                            found_key = key
                            break
                    cur_num[1] = number_dict[found_key]
                    break
                if char.isnumeric():
                    cur_num[1] = int(char)
                    break
                rev_buffer.appendleft(char)
            sum += int(f"{cur_num[0]}{cur_num[1]}")
    print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
