import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def get_next():
    with open(filename) as f:
        for line in f.readlines():
            for sequence in line.strip().split(","):
                yield sequence if sequence else None


def get_hash(sequence):
    hash = 0
    for char in sequence:
        hash += ord(char)
        hash *= 17
        hash = hash % 256
    return hash


def main_one():
    sum = 0
    for sequence in get_next():
        sum += get_hash(sequence)
    print(sum)


def main_two():
    boxes = deque([
        {"label_queue": deque(), "val_queue": deque()} for _ in range(256)
    ])
    for sequence in get_next():
        if "-" in sequence:
            label = sequence.strip("-")
            box_id = get_hash(label)
            if label in boxes[box_id]["label_queue"]:
                idx = boxes[box_id]["label_queue"].index(label)
                del boxes[box_id]["label_queue"][idx]
                del boxes[box_id]["val_queue"][idx]
        elif "=" in sequence:
            label, value = sequence.split("=")
            box_id = get_hash(label)
            if label in boxes[box_id]["label_queue"]:
                idx = boxes[box_id]["label_queue"].index(label)
                boxes[box_id]["val_queue"][idx] = value
            else:
                boxes[box_id]["label_queue"].append(label)
                boxes[box_id]["val_queue"].append(value)

    sum = 0
    for i, box in enumerate(boxes):
        for j, value in enumerate(box["val_queue"]):
            sum += (i + 1) * (j + 1) * int(value)
    print(sum)


if __name__ == "__main__":
    main_one()
    main_two()
