import os
from collections import deque


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


class Map:
    def __init__(self):
        self.map = deque()
        self.steps = 0
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
        self.steps += 1
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

    def run(self):
        while self.next:
            out = []
            for next in self.next:
                out.append(self.find_next(next))
            self.steps += 1
            if out[0] == out[1]:
                break
            self.next = out
        print(self.steps)


def main_one():
    map = Map()
    map.run()


if __name__ == "__main__":
    main_one()
