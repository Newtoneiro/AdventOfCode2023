import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

workflows = {}


def count(ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product

    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)
    return total


def main_two():
    with open(filename) as f:
        block1, _ = f.read().split("\n\n")

    for line in block1.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    print(count({key: (1, 4000) for key in "xmas"}))


if __name__ == "__main__":
    main_two()
