import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            include = True
            game, rest = line.strip().split(":")
            _, game_id = game.split(" ")
            games = rest.replace(" ", "").split(";")
            for game in games:
                blocks_dict = {
                    "red": 0,
                    "green": 0,
                    "blue": 0
                }
                blocks = game.split(",")
                for color_blocks in blocks:
                    for key in blocks_dict.keys():
                        if color_blocks.endswith(key):
                            blocks_dict[key] = int(color_blocks.strip(key))

                if not all([blocks_dict[key] <= max_cubes[key] for key in max_cubes.keys()]):
                    include = False
            if include:
                sum += int(game_id)
    print(sum)


def main_two():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            game, rest = line.strip().split(":")
            games = rest.replace(" ", "").split(";")
            blocks_dict = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for game in games:
                blocks = game.split(",")
                for color_blocks in blocks:
                    for key in blocks_dict.keys():
                        if color_blocks.endswith(key):
                            if int(color_blocks.strip(key)) > blocks_dict[key]:
                                blocks_dict[key] = int(color_blocks.strip(key))
            part_sum = 1
            for val in blocks_dict.values():
                part_sum *= val
            sum += part_sum
    print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
