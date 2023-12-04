import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            _, rest = line.strip().split(":")
            winning_numbers, play_numbers = rest.split("|")
            winning_numbers = [int(x) for x in winning_numbers.split()]
            play_numbers = [int(x) for x in play_numbers.split()]
            wins = 0
            for number in play_numbers:
                if number in winning_numbers:
                    wins += 1
            if wins > 0:
                sum += 2 ** (wins - 1)
    print(sum)


def main_two():
    with open(filename) as f:
        card_dict = {id: {"count": 1} for id in range(1, 205)}
        for line in f.readlines():
            game, rest = line.strip().split(":")
            _, game_id = game.split()
            game_id = int(game_id)
            winning_numbers, play_numbers = rest.split("|")
            winning_numbers = [int(x) for x in winning_numbers.split()]
            play_numbers = [int(x) for x in play_numbers.split()]
            wins = 0
            for number in play_numbers:
                if number in winning_numbers:
                    wins += 1
            won_card_ids = range(game_id + 1, game_id + wins + 1)
            for card_id in won_card_ids:
                card_dict[card_id]["count"] += card_dict[game_id]["count"]
        sum = 0
        for values in card_dict.values():
            sum += values["count"]
        print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
