import itertools
import os
from functools import total_ordering
from collections import defaultdict

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

ORDER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


@total_ordering
class Hand:
    def __init__(self, line):
        hand, value = line.strip().split()
        self._hand = hand
        self._value = int(value)

    @staticmethod
    def get_type_from_dict(hand_dict):
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

    def get_type(self):
        hand_dict = defaultdict(lambda: 0)

        for card in self._hand:
            if card != "J":
                hand_dict[card] += 1

        no_j = self._hand.count("J")
        if no_j == 0:
            return self.get_type_from_dict(hand_dict)

        posibilities = []
        for perm in itertools.product("".join(ORDER), repeat=no_j):
            copy_dict = hand_dict.copy()
            for char in perm:
                copy_dict[char] += 1
            possible_type = self.get_type_from_dict(copy_dict)
            if possible_type not in posibilities:
                posibilities.append(possible_type)
        return max(posibilities)

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


def main_two():
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
    main_two()
