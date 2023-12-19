import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

operations_dict = {
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
}


def main_one():
    condition_dict = {}
    parts = deque()
    with open(filename) as f:
        line = f.readline().strip()
        while line != "":
            name, conditions = line.strip("}").split("{")
            q = deque()
            for condition in conditions.split(","):
                if any([op in condition for op in operations_dict.keys()]):
                    cond, goto = condition.strip().split(":")
                    part, operand, value = cond[:1], cond[1:2], cond[2:]
                    q.append({
                        "value": int(value),
                        "part": part,
                        "operation": operations_dict[operand],
                        "goto": goto
                    })
                else:
                    q.append({
                        "value": 0,
                        "part": "x",
                        "operation": lambda a, b: True,
                        "goto": condition
                    })

            condition_dict[name] = q
            line = f.readline().strip()

        for line in f.readlines():
            line = line.strip().strip("}").strip("{")
            cur_part = {}
            for value in line.split(","):
                part, value = value.strip().split("=")
                cur_part[part] = int(value)
            parts.append(cur_part)

    my_sum = 0
    for part in parts:
        current_operation = "in"
        operations = condition_dict[current_operation]
        while current_operation not in ["R", "A"]:
            for operation in operations:
                if operation["operation"](
                        part[operation["part"]], operation["value"]
                        ):
                    current_operation = operation["goto"]
                    if current_operation in ["R", "A"]:
                        if current_operation == "A":
                            my_sum += sum([part[x] for x in part.keys()])
                        break
                    operations = condition_dict[current_operation]
                    break
    print(my_sum)


condition_dict_shallow = {}
global_vals = deque()


def dfs(cur, vals):
    if cur in ["A", "R"]:
        if cur == "A":
            global_vals.append(vals)
        return
    conditions = condition_dict_shallow[cur]
    for cond in conditions:
        if cond["operation"] in [">", "<"]:
            vals.append(f"{cond['part']}{cond['operation']}{cond['value']}")
            dfs(cond["goto"], vals)
        elif cond["operation"] == "True":
            dfs(cond["goto"], vals)


if __name__ == "__main__":
    main_one()
