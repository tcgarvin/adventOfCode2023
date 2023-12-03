from rich import print
from collections import defaultdict

def get_puzzle_input(filename="input.txt"):
    puzzle_input = defaultdict(lambda: ".")
    max_j = 0
    max_i = 0
    with open(filename) as input_txt:
        for j,line in enumerate(input_txt):
            max_j = max(j, max_j)
            for i, char in enumerate(line):
                max_i = max(i, max_i)
                puzzle_input[(i,j)] = char
    return puzzle_input, (max_i, max_j)

def is_digit(char):
    return char in "0123456789"

def is_symbol(char):
    return char != "." and not is_digit(char)

def get_adjacent_coords(coord):
    i,j = coord
    return [
        (i+1, j),
        (i+1, j-1),
        (i+1, j+1),
        (i, j-1),
        (i, j+1),
        (i-1, j),
        (i-1, j+1),
        (i-1, j-1)
    ]


def get_number_value(grid, coord):
    number_finished = False
    adjacent_symbol = False
    number = ""
    cursor = coord
    while not number_finished:
        number += grid[cursor]
        for adjacent_coord in get_adjacent_coords(cursor):
            if is_symbol(grid[adjacent_coord]):
                adjacent_symbol = True

        cursor = (cursor[0]+1, cursor[1])
        next_character = grid[cursor]
        if not is_digit(next_character):
            number_finished = True

    #print(coord, number, adjacent_symbol)
    if not adjacent_symbol:
        return 0

    return int(number)


def solve_part_1(grid, dimensions):
    total = 0
    max_i, max_j = dimensions
    for j in range(max_j+1):
        for i in range(max_i+1):
            char = grid[(i,j)]
            if is_digit(char) and (not is_digit(grid[(i-1,j)])):
                total += get_number_value(grid, (i,j))

    return total 

def solve_part_2(puzzle_input, dimensions):
    return ""

if __name__ == "__main__":
    puzzle_input, dimensions = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input, dimensions)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input, dimensions)
    print(f"Part 2: {answer_2}")
