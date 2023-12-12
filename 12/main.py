import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

cache = {}


def count(symbols, numbers):
    if symbols == "":
        return 1 if len(numbers) == 0 else 0

    if len(numbers) == 0:
        return 0 if "#" in symbols else 1

    key = (symbols, numbers)

    if key in cache:
        return cache[key]

    result = 0

    if symbols[0] in ".?":
        result += count(symbols[1:], numbers)

    if symbols[0] in "#?":
        if numbers[0] <= len(symbols) \
            and "." not in symbols[:numbers[0]] \
                and (numbers[0] == len(symbols) or symbols[numbers[0]] != "#"):
            result += count(symbols[numbers[0] + 1:], numbers[1:])

    cache[key] = result
    return result


def main_one():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            symbols, numbers = line.strip().split()
            numbers = [int(num) for num in numbers.split(",")]
            sum += count(symbols, tuple(numbers))
    print(sum)


def main_two():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            symbols, numbers = line.strip().split()
            symbols = "?".join([symbols] * 5)
            numbers = ",".join([numbers] * 5)
            numbers = [int(num) for num in numbers.split(",")]
            sum += count(symbols, tuple(numbers))
    print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
