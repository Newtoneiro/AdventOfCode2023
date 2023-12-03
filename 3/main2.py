from collections import deque
import functools
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


class Map:
    def __init__(self):
        self._map = []

    @staticmethod
    def is_gear(c):
        if c != "*":
            return False
        return True

    def init_map(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                row = []
                for c in line.strip():
                    row.append(c)
                self._map.append(row)

    def get_left(self, i, j, accumulation):
        if j <= 0:
            return accumulation
        char = self._map[i][j-1]
        if char.isnumeric():
            accumulation.appendleft(char)
            self.get_left(i, j-1, accumulation)
        return accumulation

    def get_right(self, i, j, accumulation):
        if j >= len(self._map[i]) - 1:
            return accumulation
        char = self._map[i][j+1]
        if char.isnumeric():
            accumulation.append(char)
            self.get_right(i, j+1, accumulation)
        return accumulation

    def get_up(self, i, j):
        if i <= 0:
            return []
        try:
            up_left = functools.reduce(lambda a, b: a + b, self.get_left(i-1, j, deque()))
        except TypeError:
            up_left = "."
        try:
            up_right = functools.reduce(lambda a, b: a + b, self.get_right(i-1, j, deque()))
        except TypeError:
            up_right = "."
        try:
            up_middle = self._map[i-1][j]
        except IndexError:
            up_middle = "."
        top = "" + up_left + up_middle + up_right
        up = []
        for possible_number in top.split("."):
            if possible_number.isnumeric():
                up.append(int(possible_number))
        return up

    def get_down(self, i, j):
        if i >= len(self._map) - 1:
            return []
        try:
            down_left = functools.reduce(lambda a, b: a + b, self.get_left(i+1, j, deque()))
        except TypeError:
            down_left = "."
        try:
            down_right = functools.reduce(lambda a, b: a + b, self.get_right(i+1, j, deque()))
        except TypeError:
            down_right = "."
        try:
            down_middle = self._map[i+1][j]
        except IndexError:
            down_middle = "."
        bottom = "" + str(down_left) + str(down_middle) + str(down_right)
        down = []
        for possible_number in bottom.split("."):
            if possible_number.isnumeric():
                down.append(int(possible_number))
        return down

    def get_horizontal(self, i, j):
        horizontal = []
        try:
            left = int(functools.reduce(lambda a, b: a + b, self.get_left(i, j, deque())))
            horizontal.append(left)
        except TypeError:
            pass
        try:
            right = int(functools.reduce(lambda a, b: a + b, self.get_right(i, j, deque())))
            horizontal.append(right)
        except TypeError:
            pass
        return horizontal

    def get_vertical(self, i, j):
        up = self.get_up(i, j)
        down = self.get_down(i, j)
        return up + down

    def parse(self):
        my_sum = 0
        for i, row in enumerate(self._map):
            for j, c in enumerate(row):
                if self.is_gear(c):
                    h_values = self.get_horizontal(i, j)
                    v_values = self.get_vertical(i, j)
                    all_values = h_values + v_values
                    if len(all_values) == 2:
                        my_sum += functools.reduce(lambda a, b: a * b, all_values)
        print(my_sum)


def main_two():
    map = Map()
    map.init_map(filename)
    map.parse()


if __name__ == "__main__":
    main_two()
