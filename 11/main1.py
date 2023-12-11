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
        count = 0
        for i in indexes:
            self.map.insert(i + count, deque(['.' for x in range(len(row))]))
            count += 1

        # Horizontal
        indexes = []
        for i in range(len(self.map[0])):
            column = [self.map[row][i] for row in range(len(self.map))]
            if '#' not in column:
                indexes.append(i)
        count = 0
        for i in indexes:
            for row in self.map:
                row.insert(i + count, '.')
            count += 1

    def run(self):
        self.expand()
        self.name_galaxies()
        pairs = combinations(range(1, self.galaxy_count + 1), 2)
        sum = 0
        for pair in pairs:
            start = self.coords_dict[pair[0]]
            end = self.coords_dict[pair[1]]
            sum += abs(start[0] - end[0]) + abs(start[1] - end[1])
        print(sum)


def main_one():
    map = Map()
    map.run()


if __name__ == "__main__":
    main_one()
