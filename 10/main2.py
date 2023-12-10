import os
from collections import deque


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


EXPANDS = {
    "S": [",X,", "XXX", ",X,"],
    ".": [",,,", ",,,", ",,,"],
    "|": [",X,", ",X,", ",X,"],
    "-": [",,,", "XXX", ",,,"],
    "L": [",X,", ",XX", ",,,"],
    "J": [",X,", "XX,", ",,,"],
    "7": [",,,", "XX,", ",X,"],
    "F": [",,,", ",XX", ",X,"],
}


class Map:
    def __init__(self):
        self.map = deque()
        with open(filename) as f:
            for line in f.readlines():
                if "S" in line:
                    self.start = (line.index("S") + 1, len(self.map) + 1)
                row = deque([x for x in line.strip()])
                row.appendleft(".")
                row.append(".")
                self.map.append(row)
        self.map.append(deque(["." for x in range(len(self.map[0]))]))
        self.map.appendleft(deque(["." for x in range(len(self.map[0]))]))
        self.visited = []
        self.next = self.find_start()

    def find_start(self):
        pos = self.start
        out = []
        if self.map[pos[1] - 1][pos[0]] in ["7", "F", "|"]:
            out.append((pos[0], pos[1] - 1))
        if self.map[pos[1] + 1][pos[0]] in ["J", "L", "|"]:
            out.append((pos[0], pos[1] + 1))
        if self.map[pos[1]][pos[0] - 1] in ["L", "F", "-"]:
            out.append((pos[0] - 1, pos[1]))
        if self.map[pos[1]][pos[0] + 1] in ["J", "7", "-"]:
            out.append((pos[0] + 1, pos[1]))
        self.visited.append(pos)
        return out

    def find_next(self, pos):
        symbol = self.map[pos[1]][pos[0]]
        self.visited.append(pos)
        if symbol == "F":
            if (pos[0], pos[1] + 1) not in self.visited:
                return (pos[0], pos[1] + 1)
            elif (pos[0] + 1, pos[1]) not in self.visited:
                return (pos[0] + 1, pos[1])
        elif symbol == "7":
            if (pos[0], pos[1] + 1) not in self.visited:
                return (pos[0], pos[1] + 1)
            elif (pos[0] - 1, pos[1]) not in self.visited:
                return (pos[0] - 1, pos[1])
        elif symbol == "|":
            if (pos[0], pos[1] - 1) not in self.visited:
                return (pos[0], pos[1] - 1)
            elif (pos[0], pos[1] + 1) not in self.visited:
                return (pos[0], pos[1] + 1)
        elif symbol == "L":
            if (pos[0] + 1, pos[1]) not in self.visited:
                return (pos[0] + 1, pos[1])
            elif (pos[0], pos[1] - 1) not in self.visited:
                return (pos[0], pos[1] - 1)
        elif symbol == "J":
            if (pos[0] - 1, pos[1]) not in self.visited:
                return (pos[0] - 1, pos[1])
            elif (pos[0], pos[1] - 1) not in self.visited:
                return (pos[0], pos[1] - 1)
        elif symbol == "-":
            if (pos[0] + 1, pos[1]) not in self.visited:
                return (pos[0] + 1, pos[1])
            elif (pos[0] - 1, pos[1]) not in self.visited:
                return (pos[0] - 1, pos[1])
            
    def make_big_map(self):
        big_map = []
        for x in range(len(self.map)):
            row1 = []
            row2 = []
            row3 = []
            for y in range(len(self.map[x])):
                symbol = self.map[x][y]
                if (y, x) in self.visited:
                    row1 += [x for x in EXPANDS[symbol][0]]
                    row2 += [x for x in EXPANDS[symbol][1]]
                    row3 += [x for x in EXPANDS[symbol][2]]
                else:
                    row1 += [",", ",", ","]
                    row2 += [",", symbol, ","]
                    row3 += [",", ",", ","]
            big_map.append(row1)
            big_map.append(row2)
            big_map.append(row3)
        self.big_map = big_map

    def run(self):
        while self.next:
            out = []
            for next in self.next:
                out.append(self.find_next(next))
            if out[0] == out[1]:
                self.visited.append(out[0])
                break
            self.next = out

        self.make_big_map()

        queue = deque([(0, 0)])
        while len(queue) != 0:
            pos = queue.pop()
            if self.big_map[pos[1]][pos[0]] not in ["X", "O"]:
                self.big_map[pos[1]][pos[0]] = "O"
                if pos[0] < len(self.big_map[0]) - 1:
                    queue.append((pos[0] + 1, pos[1]))
                if pos[0] > 0:
                    queue.append((pos[0] - 1, pos[1]))
                if pos[1] < len(self.big_map) - 1:
                    queue.append((pos[0], pos[1] + 1))
                if pos[1] > 0:
                    queue.append((pos[0], pos[1] - 1))

        sum = 0
        for row in self.big_map:
            for char in row:
                if char not in ["X", "O", ","]:
                    sum += 1
        print(sum)


def main_two():
    map = Map()
    map.run()


if __name__ == "__main__":
    main_two()
