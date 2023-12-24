import os
from pprint import pprint

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

def main_one():
    hailstones = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            pos, vel = line.split("@")
            pos = [int(p) for p in pos.strip().split(", ")[:2]]
            vel = [int(v) for v in vel.strip().split(", ")[:2]]
            hailstones.append((pos, vel))

    total = 0

    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]: # Method of substitution to find intersection
            a1, b1, c1 = hs1[1][1], -hs1[1][0], hs1[1][1] * hs1[0][0] - hs1[1][0] * hs1[0][1]
            a2, b2, c2 = hs2[1][1], -hs2[1][0], hs2[1][1] * hs2[0][0] - hs2[1][0] * hs2[0][1]
            if a1 * b2 == b1 * a2:
                continue
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if all((x - hs[0][0]) * hs[1][0] >= 0 and (y - hs[0][1]) * hs[1][1] >= 0 for hs in (hs1, hs2)):
                    total += 1

    pprint(total)
    

if __name__ == "__main__":  
    main_one()
