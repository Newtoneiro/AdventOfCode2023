import os
from heapq import heappush, heappop

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

map = []


def main_one():
    visited = set()
    heap = [(0, 0, 0, 0, 0, 0)]
    while heap:
        score, row, col, dir_row, dir_col, moves_number = heappop(heap)

        if (row, col) == (len(map) - 1, len(map[0]) - 1):
            print(score)
            break

        if (row, col, dir_row, dir_col, moves_number) in visited:
            continue

        visited.add((row, col, dir_row, dir_col, moves_number))

        if moves_number < 3 and (dir_row, dir_col) != (0, 0):
            next_row = row + dir_row
            next_col = col + dir_col
            if 0 <= next_row < len(map) and 0 <= next_col < len(map[0]):
                heappush(
                    heap,
                    (
                        score + map[next_row][next_col],
                        next_row,
                        next_col,
                        dir_row,
                        dir_col,
                        moves_number + 1,
                    ),
                )

        for next_dir_row, next_dir_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (next_dir_row, next_dir_col) != (dir_row, dir_col) and (
                next_dir_row,
                next_dir_col,
            ) != (-dir_row, -dir_col):
                next_row = row + next_dir_row
                next_col = col + next_dir_col
                if 0 <= next_row < len(map) and 0 <= next_col < len(map[0]):
                    heappush(
                        heap,
                        (
                            score + map[next_row][next_col],
                            next_row,
                            next_col,
                            next_dir_row,
                            next_dir_col,
                            1,
                        ),
                    )


def main_two():
    visited = set()
    heap = [(0, 0, 0, 0, 0, 0)]

    while heap:
        score, row, col, dir_row, dir_col, moves_number = heappop(heap)

        if (row, col) == (len(map) - 1, len(map[0]) - 1):
            print(score)
            break

        if (row, col, dir_row, dir_col, moves_number) in visited:
            continue

        visited.add((row, col, dir_row, dir_col, moves_number))

        if moves_number < 10 and (dir_row, dir_col) != (0, 0):
            next_row = row + dir_row
            next_col = col + dir_col
            if 0 <= next_row < len(map) and 0 <= next_col < len(map[0]):
                heappush(
                    heap,
                    (
                        score + map[next_row][next_col],
                        next_row,
                        next_col,
                        dir_row,
                        dir_col,
                        moves_number + 1,
                    ),
                )

        if moves_number >= 4 or (dir_row, dir_col) == (0, 0):
            for next_dir_row, next_dir_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (next_dir_row, next_dir_col) != (dir_row, dir_col) and (
                    next_dir_row,
                    next_dir_col,
                ) != (-dir_row, -dir_col):
                    next_row = row + next_dir_row
                    next_col = col + next_dir_col
                    if 0 <= next_row < len(map) and 0 <= next_col < len(map[0]):
                        heappush(
                            heap,
                            (
                                score + map[next_row][next_col],
                                next_row,
                                next_col,
                                next_dir_row,
                                next_dir_col,
                                1,
                            ),
                        )


if __name__ == "__main__":
    with open(filename) as f:
        for line in f:
            map.append([int(x) for x in line.strip()])

    main_one()
    main_two()
