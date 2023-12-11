import os
from collections import deque
from itertools import combinations


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


class Map:
    def __init__(self):
        self.map = deque()
        self.steps = 0
        with open(filename) as f:
            for line in f.readlines():
                self.map.append(deque([char for char in line.strip()]))

    def name_galaxies(self):
        self.coords_dict = {}
        self.galaxy_count = 0
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == '#':
                    self.galaxy_count += 1
                    self.coords_dict[self.galaxy_count] = (x, y)
                    self.map[y][x] = f"{self.galaxy_count}"

    def expand(self):
        # Vertical
        indexes = []
        for i in range(len(self.map)):
            row = self.map[i]
            if '#' not in row:
                indexes.append(i)
        self.v_indexes = indexes

        # Horizontal
        indexes = []
        for i in range(len(self.map[0])):
            column = [self.map[row][i] for row in range(len(self.map))]
            if '#' not in column:
                indexes.append(i)
        self.h_indexes = indexes

    def run(self, expansion_rate):
        self.expand()
        self.name_galaxies()
        pairs = combinations(range(1, self.galaxy_count + 1), 2)
        sum = 0
        for pair in pairs:
            start = self.coords_dict[pair[0]]
            end = self.coords_dict[pair[1]]

            expansion_sum = 0
            for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                if x in self.h_indexes:
                    expansion_sum += expansion_rate - 1
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                if y in self.v_indexes:
                    expansion_sum += expansion_rate - 1

            sum += abs(start[0] - end[0]) + abs(start[1] - end[1]) + expansion_sum
        print(sum)


def main_two():
    map = Map()
    map.run(1_000_000)


if __name__ == "__main__":
    main_two()
