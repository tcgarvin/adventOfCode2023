from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(list(map(int,line.strip().split())))
    return puzzle_input

def predict_value(signal, backwards=False):
    derivitives = [signal]
    while not all(x == 0 for x in derivitives[-1]):
        latest_derivitive = derivitives[-1]
        new_derivitive = []
        for i in range(len(latest_derivitive) - 1):
            new_derivitive.append(latest_derivitive[i+1] - latest_derivitive[i])
        derivitives.append(new_derivitive)

    predicted_value = 0
    for i in reversed(range(len(derivitives))):
        if backwards:
            predicted_value = derivitives[i][0] - predicted_value
        else:
            predicted_value = derivitives[i][-1] + predicted_value

    return predicted_value


def solve_part_1(puzzle_input):
    total = 0
    for signal in puzzle_input:
        total += predict_value(signal)
        
    return total

def solve_part_2(puzzle_input):
    total = 0
    for signal in puzzle_input:
        total += predict_value(signal, backwards=True)
        
    return total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
