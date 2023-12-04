from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            winning_side = line[10:40].split()
            elf_side = line[42:].split()
            puzzle_input.append((winning_side, elf_side))
    return puzzle_input

def solve_part_1(cards):
    total = 0
    for winning_side, elf_side in cards:
        matches = len(set(winning_side).intersection(elf_side))
        if matches > 0:
            total += 2 ** (matches - 1) 
    return total

def solve_part_2(cards):
    card_counts = [1 for _ in cards]
    for i, card in enumerate(cards):
        winning_side, elf_side = card
        matches = len(set(winning_side).intersection(elf_side))
        for j in range(matches):
            card_counts[i+j+1] += card_counts[i]
    return sum(card_counts)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
