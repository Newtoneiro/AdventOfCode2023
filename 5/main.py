import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    queue = ["seed"]
    global_map = {}
    with open(filename) as f:
        values = [int(x) for x in f.readline().strip().split()[1:]]
        f.readline()  # skip empty line
        next_line = f.readline()
        while next_line:
            title = next_line.strip().split()[0]
            ranges = f.readline().strip()
            src, dst = title.split("-")[0], title.split("-")[-1]
            queue.append(dst)
            global_map[f"{src}-{dst}"] = []
            while ranges:
                ranges = ranges.split()
                global_map[f"{src}-{dst}"].append([int(x) for x in ranges])
                ranges = f.readline().strip()
            next_line = f.readline()

        for src, dst in zip(queue, queue[1:]):
            key = f"{src}-{dst}"
            new_values = []
            for value in values:
                mapped = False
                for cur_range in global_map[key]:
                    if value in range(cur_range[1], cur_range[1] + cur_range[2]):
                        mapped = True
                        new_values.append(cur_range[0] + (value - cur_range[1]))
                if not mapped:
                    new_values.append(value)
            values = new_values
        print(min(values))


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def map_range(input_range, mapping_range):
    in_start, in_end = input_range[0], input_range[0] + input_range[1]
    map_start, map_end = mapping_range[1], mapping_range[1] + mapping_range[2]
    if in_end <= map_start:
        return [input_range]
    if in_start < map_start and in_end <= map_end:
        return [
            (in_start, map_start - in_start),
            (mapping_range[0], in_end - map_start),
        ]
    if in_start >= map_start and in_end <= map_end:
        return [(mapping_range[0] + (in_start - map_start), input_range[1])]
    if in_start < map_start and in_end > map_end:
        return [
            (in_start, map_start - in_start),
            (mapping_range[0], map_end - map_start),
            (map_end, in_end - map_end),
        ]
    if in_start < map_end and in_end > map_end:
        return [
            (mapping_range[0] + (in_start - map_start), map_end - in_start),
            (map_end, in_end - map_end),
            ]
    if in_start >= map_end:
        return [input_range]


def main_two():
    queue = ["seed"]
    global_map = {}
    with open(filename) as f:
        seed_ranges = [int(x) for x in f.readline().strip().split()[1:]]
        f.readline()  # skip empty line
        next_line = f.readline()
        while next_line:
            title = next_line.strip().split()[0]
            ranges = f.readline().strip()
            src, dst = title.split("-")[0], title.split("-")[-1]
            queue.append(dst)
            global_map[f"{src}-{dst}"] = []
            while ranges:
                ranges = ranges.split()
                global_map[f"{src}-{dst}"].append([int(x) for x in ranges])
                ranges = f.readline().strip()
            next_line = f.readline()

        ranges = [(s, e) for s, e in pairwise(seed_ranges)]
        for src, dst in zip(queue, queue[1:]):
            key = f"{src}-{dst}"
            new_ranges = []
            for cur_range in ranges:
                for mapping_range in global_map[key]:
                    dupa = map_range(cur_range, mapping_range)
                    new_ranges.extend(dupa)
            ranges = new_ranges
        print(min([x[0] for x in ranges]))


if __name__ == "__main__":
    main_one()
    main_two()
