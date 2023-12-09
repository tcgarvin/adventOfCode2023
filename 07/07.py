from rich import print
from collections import Counter

CARDS       = "23456789TJQKA"
JOKER_CARDS = "J23456789TQKA"

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            hand, bid = line.split()
            puzzle_input.append((hand, int(bid)))
    return puzzle_input

def score_card(card):
    return CARDS.index(card)

def score_card_jokers(card):
    return JOKER_CARDS.index(card)

def score_hand(hand):
    """Return sortable score object"""
    card_counter = Counter(hand)
    most_common_cards = card_counter.most_common(2)
    top_count = most_common_cards[0][1]
    second_count = 0
    if len(most_common_cards) > 1:
        second_count = most_common_cards[1][1]
    type_score = (top_count, second_count)

    card_scores = tuple(map(score_card, hand))
    return (type_score, card_scores)

def score_hand_jokers(hand):
    """Return sortable score object"""
    card_counter = Counter(hand)
    jokers = card_counter.pop("J", 0)
    most_common_cards = card_counter.most_common(2)

    top_count = 0
    if len(most_common_cards) > 0:
        top_count = most_common_cards[0][1]
    top_count += jokers

    second_count = 0
    if len(most_common_cards) > 1:
        second_count = most_common_cards[1][1]

    type_score = (top_count, second_count)
    card_scores = tuple(map(score_card_jokers, hand))
    return (type_score, card_scores)

def add_score(hand_and_bid):
    return (score_hand(hand_and_bid[0]), hand_and_bid[0], hand_and_bid[1])

def add_score_joker(hand_and_bid):
    return (score_hand_jokers(hand_and_bid[0]), hand_and_bid[0], hand_and_bid[1])

def solve_part_1(puzzle_input):
    scored_hands = sorted(map(add_score, puzzle_input))
    total = 0
    for i, (score, hand, bid) in enumerate(scored_hands):
        rank = i + 1
        total += rank * bid

    return total

def solve_part_2(puzzle_input):
    scored_hands = sorted(map(add_score_joker, puzzle_input))
    total = 0
    for i, (score, hand, bid) in enumerate(scored_hands):
        rank = i + 1
        total += rank * bid

    return total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
