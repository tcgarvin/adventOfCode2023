from rich import print
from dataclasses import dataclass
import re
from typing import List

@dataclass
class Grab:
    red: int = 0
    green: int = 0
    blue: int = 0

@dataclass
class Game:
    id: int
    grabs: List[Grab]

def parse_game(line):
    game_prefix, game_body = line.split(":")
    game_number = int(game_prefix.split(" ")[1])
    grab_strings = game_body.split(";")
    grabs = []
    for grab_string in grab_strings:
        color_strings = grab_string.split(",")
        colors = {}
        for color_string in color_strings:
            number, color = color_string.strip().split(" ")
            number = int(number)
            colors[color] = number
        grabs.append(Grab(**colors))

    game = Game(id=game_number, grabs = grabs)
    return game
            
def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(parse_game(line))
    return puzzle_input

def solve_part_1(puzzle_input):
    #print(puzzle_input[0])
    total = 0
    for game in puzzle_input:
        valid_game = True
        for grab in game.grabs:
            if grab.red > 12 or grab.green > 13 or grab.blue > 14:
                valid_game = False

        if valid_game:
            total += game.id

    return total

def solve_part_2(puzzle_input):
    total = 0
    for game in puzzle_input:
        min_red = 0
        min_green = 0
        min_blue = 0
        for grab in game.grabs:
            if grab.red > min_red:
                min_red = grab.red
            if grab.green > min_green:
                min_green = grab.green
            if grab.blue > min_blue:
                min_blue = grab.blue
        total += min_red * min_blue * min_green

    return total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
