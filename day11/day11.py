#!/usr/bin/python3.9

import sys
from itertools import combinations

class Universe:
    def __init__(self, expand_factor:int, lines:list[str]):
        self.initial_map(lines)
        self.expand_factor = expand_factor

    def initial_map(self, lines: list[str]) -> None:
        self.galaxies: list[tuple[int, int]] = []

        self.max_x = len(lines[0])
        self.max_y = len(lines)

        for x in range(0, self.max_x):
            for y in range(0, self.max_y):
                if lines[y][x] == "#":
                    self.galaxies.append((x, y))

    def expand_map(self) -> None:
        new_galaxies : list[tuple[int, int]] = []

        used_columns = set()
        used_lines = set()
        for (x, y) in self.galaxies:
            used_columns.add(x)
            used_lines.add(y)

        columns_to_expand = [x for x in range(0, self.max_x) if x not in used_columns]
        lines_to_expand   = [y for y in range(0, self.max_y) if y not in used_lines]

        for (x, y) in self.galaxies:
            new_x = x + (self.expand_factor-1)*len(list(filter(lambda s: s < x, columns_to_expand))) 
            new_y = y + (self.expand_factor-1)*len(list(filter(lambda s: s < y, lines_to_expand)))

            new_galaxies.append((new_x, new_y))

        self.galaxies = new_galaxies
        self.max_x = max([x for (x,_) in new_galaxies])
        self.max_y = max([x for (x,_) in new_galaxies])

    def compute_distances(self) -> int:
        total = 0
        for ((x1,y1),(x2,y2)) in combinations(self.galaxies, 2):
            total += abs(x2-x1)  + abs(y2-y1)
        return total

def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    lines = read_file_lines(file_path)

    if lines is not None:
        w = Universe(2, [x.strip() for x in lines])
        w.expand_map()
        print(f"Star1: {w.compute_distances()}")
        w = Universe(100, [x.strip() for x in lines])
        w.expand_map()
        print(f"Test: {w.compute_distances()}")
        w = Universe(1000000, [x.strip() for x in lines])
        w.expand_map()
        print(f"Star2: {w.compute_distances()}")

