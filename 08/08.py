from collections import defaultdict
from itertools import cycle
import re
from rich import print

NODE_RE = re.compile("""([A-Z]{3}) = [(]([A-Z]{3}), ([A-Z]{3})[)]""")

def get_puzzle_input():
    instructions = ""
    with open("input.txt") as input_txt:
        instructions = input_txt.readline().strip()
        nodes = {}
        for line in input_txt:
            match = NODE_RE.search(line.strip())
            if match is None:
                continue
            #print(match.groups())
            nodes[match.group(1)] = (match.group(2), match.group(3))
    #print(nodes)
    return instructions, nodes

def solve_part_1(instructions, nodes):
    cursor = "AAA"
    distance = 0
    for instruction in cycle(instructions):
        choices = nodes[cursor]
        choice = 0 if instruction == "L" else 1
        cursor = choices[choice]
        distance += 1
        if cursor == "ZZZ":
            break
    return distance

def solve_part_2(instructions, nodes):
    cursors = [node for node in nodes.keys() if node.endswith("A")]
    print(cursors)
    distance = 0
    cycles = list([] for _ in cursors)
    for jj, instruction in enumerate(cycle(instructions)):
        if jj > 100000:
            # Should be able to predict cycles times now
            break

        j = jj % len(instructions)
        distance += 1
        choice = 0 if instruction == "L" else 1
        #print(cursors)
        for i, cursor in enumerate(cursors):
            choices = nodes[cursor]
            cursor = choices[choice]
            if cursor.endswith("Z"):
                cycles[i].append((distance, cursor, j))
                #print(cycles)
            cursors[i] = cursor

        cursors_at_end = [cursor.endswith("Z") for cursor in cursors]
        if all(cursors_at_end):
            break

    print(cycles)

    fast_cursors = []
    cycle_lengths = []

    for cycle_history in cycles:
        cycle_length = cycle_history[-1][0] - cycle_history[-2][0]
        cycle_lengths.append(cycle_length)
        fast_cursors.append(cycle_history[-1][0])

    print(cycle_lengths)
    least_common_multiple = 1
    for l in cycle_lengths:
        least_common_multiple *= l
    return least_common_multiple

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: Minimum Common Product of {answer_2}")
