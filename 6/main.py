import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    sum = 1
    with open(filename) as f:
        times = [int(x) for x in f.readline().strip().split()[1:]]
        distances = [int(x) for x in f.readline().strip().split()[1:]]
        for time, distance in zip(times, distances):
            number_of_ways = 0
            for v in range(0, time):
                time_to_travel = time - v
                actual_distance = v * time_to_travel
                if actual_distance > distance:
                    number_of_ways += 1
            if number_of_ways > 0:
                sum *= number_of_ways
    print(sum)


def main_two():
    with open(filename) as f:
        times = f.readline().strip().split()[1:]
        time = int("".join(times))
        distances = f.readline().strip().split()[1:]
        distance = int("".join(distances))
        number_of_ways = 0
        for v in range(0, time):
            time_to_travel = time - v
            actual_distance = v * time_to_travel
            if actual_distance > distance:
                number_of_ways += 1
        print(number_of_ways)


if __name__ == "__main__":
    main_one()
    main_two()
