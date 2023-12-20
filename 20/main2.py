import abc
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

STEPS = 0


class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    @abc.abstractmethod
    def broadcast(self, pulse, parent):
        pass


class Output(Node):
    def __init__(self, name, children):
        super().__init__(name, children)

    def broadcast(self, pulse, parent):
        print(STEPS)
        if pulse == "low":
            print(STEPS)
            exit()


class Broadcaster(Node):
    def __init__(self, name, children):
        super().__init__(name, children)

    def broadcast(self, pulse, parent):
        for child in self.children:
            if isinstance(child, Conjunction):
                child.remembered[self.name] = pulse
        for child in self.children:
            PULSES_COUNT[pulse] += 1
            child.broadcast(pulse, self)


class FlipFlop(Node):
    def __init__(self, name, children):
        super().__init__(name, children)
        self.is_on = False

    def broadcast(self, pulse, parent):
        if pulse == "high":
            pass
        elif pulse == "low":
            self.is_on = not self.is_on
            for child in self.children:
                if isinstance(child, Conjunction):
                    child.remembered[self.name] = "high" if self.is_on else "low"
            for child in self.children:
                PULSES_COUNT["high" if self.is_on else "low"] += 1
                child.broadcast("high" if self.is_on else "low", self)


class Conjunction(Node):
    def __init__(self, name, children):
        super().__init__(name, children)
        self.remembered = {}

    def broadcast(self, pulse, parent):
        for child in self.children:
            if isinstance(child, Conjunction):
                if all([value == "high" for value in self.remembered.values()]):
                    pulse = "low"
                else:
                    pulse = "high"
                child.remembered[self.name] = pulse
        for child in self.children:
            if all([value == "high" for value in self.remembered.values()]):
                PULSES_COUNT["low"] += 1
                child.broadcast("low", self)
            else:
                PULSES_COUNT["high"] += 1
                child.broadcast("high", self)


PULSES_COUNT = {"high": 0, "low": 0}


def main_two():
    nodes = {}
    with open(filename) as f:
        for line in f.readlines():
            module, children = line.strip().split(" -> ")
            children = children.split(", ")
            if module == "broadcaster":
                nodes["broadcaster"] = Broadcaster(module, children)
            elif module.startswith("%"):
                name = module[1:]
                nodes[name] = FlipFlop(name, children)
            elif module.startswith("&"):
                name = module[1:]
                nodes[name] = Conjunction(name, children)

    for value in nodes.values():
        new_children = []
        for child in value.children:
            if child in nodes.keys():
                new_children.append(nodes[child])
            else:
                new_children.append(Output(child, []))
        value.children = new_children
        # add parents to conjunctions
        for child in value.children:
            if isinstance(child, Conjunction):
                child.remembered[value.name] = "low"

    while True:
        global STEPS
        PULSES_COUNT["low"] += 1
        nodes["broadcaster"].broadcast("low", None)
        STEPS += 1


if __name__ == "__main__":
    main_two()
