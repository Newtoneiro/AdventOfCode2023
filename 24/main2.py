import os
from pprint import pprint
import sympy

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

def main_two():
    hailstones = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            pos, vel = line.split("@")
            pos = [int(p) for p in pos.strip().split(", ")]
            vel = [int(v) for v in vel.strip().split(", ")]
            hailstones.append((pos, vel))

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
    equations = []

    for i, ((sx, sy, sz), (vx, vy, vz)) in enumerate(hailstones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            break
        
    answer = answers[0]

    print(answer[xr] + answer[yr] + answer[zr])
    

if __name__ == "__main__":  
    main_two()
