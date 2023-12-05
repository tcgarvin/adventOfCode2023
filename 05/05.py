from rich import print
from typing import List

class Mapping():
    def __init__(self, name, ranges):
        self.name = name
        self._ranges = sorted(ranges)

    def __repr__(self):
        return f"Mapping({self.name})"

    def map(self, value):
        range = None
        for candidate_range in self._ranges:
            #print(value, candidate_range)
            source_start, _, length = candidate_range
            if value >= source_start and value < source_start + length:
                range = candidate_range

        if range is None:
            return value

        source_start, dest_start, _ = range
        shift = dest_start - source_start
        return value + shift


class Almanac():
    def __init__(self, seeds, mappings:List[Mapping]):
        self.seeds = seeds
        self.mappings = mappings

    def seed_to_location(self, seed):
        mapped_value = seed
        for mapping in self.mappings:
            mapped_value = mapping.map(mapped_value)
        return mapped_value

def get_puzzle_input():
    with open("input.txt") as input_txt:
        seeds = list(map(int, input_txt.readline()[6:].strip().split()))
        mappings = []
        ranges = []
        mapping_name = ""
        for line in input_txt:
            if len(line.strip()) == 0:
                continue
            if ":" in line:
                if len(mapping_name) > 0:
                    mapping = Mapping(mapping_name, ranges)
                    mappings.append(mapping)
                mapping_name = line[:-2]
                ranges = []
                continue

            line_values = list(map(int, line.strip().split()))
            dest_start, source_start, length = line_values
            range = (source_start, dest_start, length)
            ranges.append(range)

        mapping = Mapping(mapping_name, ranges)
        mappings.append(mapping)
    
    return Almanac(seeds, mappings)

def solve_part_1(almanac):
    min_location = float('inf')
    for seed in almanac.seeds:
        seed_location = almanac.seed_to_location(seed)
        if seed_location < min_location:
            min_location = seed_location

    return min_location

def solve_part_2(puzzle_input):
    return ""

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
