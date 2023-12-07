import os
from functools import total_ordering
from collections import defaultdict

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


@total_ordering
class Hand:
    def __init__(self, line):
        hand, value = line.strip().split()
        self._hand = hand
        self._value = int(value)

    def get_type(self):
        hand_dict = defaultdict(lambda: 0)
        for card in self._hand:
            hand_dict[card] += 1

        if 5 in hand_dict.values():
            return 6
        elif 4 in hand_dict.values():
            return 5
        elif all(val in hand_dict.values() for val in [2, 3]):
            return 4
        elif 3 in hand_dict.values():
            return 3
        elif list(hand_dict.values()).count(2) == 2:
            return 2
        elif 2 in hand_dict.values():
            return 1
        else:
            return 0

    def __gt__(self, other):
        if self.get_type() != other.get_type():
            return self.get_type() > other.get_type()
        for card1, card2 in zip(self._hand, other._hand):
            if ORDER.index(card1) != ORDER.index(card2):
                return ORDER.index(card1) < ORDER.index(card2)

    def __eq__(self, other):
        if self.get_type() != other.get_type():
            return False
        for card1, card2 in zip(self._hand, other._hand):
            if ORDER.index(card1) != ORDER.index(card2):
                return False


def main_one():
    with open(filename) as f:
        hands = []
        for line in f.readlines():
            hands.append(Hand(line))
        hands.sort()
        sum = 0
        count = 1
        for hand in hands:
            sum += hand._value * count
            count += 1
    print(sum)


if __name__ == "__main__":
    main_one()
