from rich import print

def get_puzzle_input():
    with open("input.txt") as input_txt:
        times = map(int, input_txt.readline().split()[1:])
        distances = map(int, input_txt.readline().split()[1:])

        races = list(zip(times, distances))
        print(races)
    return races

def solve_part_1(races):
    total = 1
    for time, record_distance in races:
        ways_to_win = 0
        for duration in range(time):
            if duration * (time-duration) > record_distance:
                ways_to_win += 1

        total *= ways_to_win
    return total

def solve_part_2(puzzle_input):
    with open("input.txt") as input_txt:
        time = int("".join(input_txt.readline().split()[1:]))
        record_distance = int("".join(input_txt.readline().split()[1:]))

        ways_to_win = 0
        for duration in range(time):
            if duration * (time-duration) > record_distance:
                ways_to_win += 1

    return ways_to_win

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
