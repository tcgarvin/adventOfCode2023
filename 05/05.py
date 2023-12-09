from bisect import bisect_left, bisect_right
from typing import List

from rich import print

def _bisect_left(ranges, entry):
    return bisect_left(ranges, entry[0], key=lambda e: e[0])

class Mapping():
    def __init__(self, name):
        self.name = name
        self._ranges = [(0,0)]

    def __repr__(self):
        return f"Mapping({self.name})"

    def add_range(self, source, dest, length):
        entry_start = (source, dest)
        entry_end = (source + length, source + length)
        start_insert_point = _bisect_left(self._ranges, entry_start)
        if len(self._ranges) > start_insert_point and self._ranges[start_insert_point][0] == source:
            print("Need to replace rangeend")
            self._ranges[start_insert_point] = entry_start
        else:
            self._ranges.insert(start_insert_point, entry_start)
        end_insert_point = _bisect_left(self._ranges, entry_end)
        if len(self._ranges) > end_insert_point and self._ranges[end_insert_point][0] == source + length:
            print("no need to add end entry")
        else:
            self._ranges.insert(end_insert_point, entry_end)

        pass

    def map_range(self, start, end):
        resulting_ranges = []
        cursor = start
        while cursor <= end:
            range_end_index = bisect_right(self._ranges, cursor, key=lambda e: e[0])
            range_start_index = range_end_index - 1
            assert self._ranges[range_start_index][0] <= cursor
            assert range_end_index == len(self._ranges) or self._ranges[range_end_index][0] > cursor

            source, dest = self._ranges[range_start_index]
            shift = dest - source
            if len(self._ranges) > range_end_index:
                next_range_source = self._ranges[range_end_index][0]
                if next_range_source > end:
                    resulting_range_end = end
                else:
                    resulting_range_end = next_range_source - 1
            else:
                resulting_range_end = end

            resulting_ranges.append((cursor + shift, resulting_range_end - cursor + 1))
            cursor = resulting_range_end + 1

        assert len(resulting_ranges) > 0

        return resulting_ranges
            
class Almanac():
    def __init__(self, seeds, seed_ranges, mappings:List[Mapping]):
        self.seeds = seeds
        self.seed_ranges = seed_ranges
        self.mappings = mappings

    def seed_to_location(self, seed):
        mapped_value = seed
        for mapping in self.mappings:
            mapped_value = mapping.map_range(mapped_value, mapped_value)[0][0]
        return mapped_value

    def seed_ranges_to_location(self, ranges):
        results = ranges
        for mapping in self.mappings:
            next_resulting_ranges = []
            for start, length in results:
                end = start + length - 1
                next_resulting_ranges.extend(mapping.map_range(start, end))
            results = next_resulting_ranges

        return results


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
                    mapping = Mapping(mapping_name)
                    for r in ranges:
                        mapping.add_range(*r)
                    mappings.append(mapping)
                mapping_name = line[:-2]
                ranges = []
                continue

            line_values = list(map(int, line.strip().split()))
            dest_start, source_start, length = line_values
            r = (source_start, dest_start, length)
            ranges.append(r)

        mapping = Mapping(mapping_name)
        for r in ranges:
            mapping.add_range(*r)
        mappings.append(mapping)
    
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))
    return Almanac(seeds, seed_ranges, mappings)

def solve_part_1(almanac):
    min_location = float('inf')
    for seed in almanac.seeds:
        seed_location = almanac.seed_to_location(seed)
        if seed_location < min_location:
            min_location = seed_location

    return min_location

def solve_part_2(almanac):
    everything_mapped = almanac.seed_ranges_to_location(almanac.seed_ranges)

    return min(everything_mapped)[0]

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
