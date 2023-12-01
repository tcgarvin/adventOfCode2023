from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line)
    return puzzle_input

def solve_part_1(puzzle_input):
    total = 0
    for line in puzzle_input:
        digits = []
        for c in line:
            if c in "1234567890":
                digits.append(c)
        line_value = int(digits[0] + digits[-1])
        total += line_value
    return total

DIGITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def solve_part_2(puzzle_input):
    total = 0
    for line in puzzle_input:
        digits = []
        for i, c in enumerate(line):
            if c in "1234567890":
                digits.append(c)
            else:
                for digit,word in enumerate(DIGITS):
                    if line[i:i+len(word)] == word:
                        #print(word)
                        digits.append(str(digit))

        line_value = int(digits[0] + digits[-1])
        total += line_value
    return total

def get_part2_value_from_line(line):
    digits = []
    for i, c in enumerate(line):
        if c in "1234567890":
            digits.append(c)
        else:
            for digit,word in enumerate(DIGITS):
                if line[i:i+len(word)] == word:
                    digits.append(str(digit))

    return int(digits[0] + digits[-1])


def solve_part_2_v2(puzzle_input):
    return sum(get_part2_value_from_line(line) for line in puzzle_input)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")

    answer_2_v2 = solve_part_2_v2(puzzle_input)
    print(f"Part 2 v2: {answer_2_v2}")
