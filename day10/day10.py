#!/usr/bin/python3.9

import sys
from collections import defaultdict

class Field:
    def __init__(self, lines:list[str]):
        self.initial_map(lines)

    def initial_map(self, lines: list[str]) -> None:
        self.ground: defaultdict[tuple[int, int], str] = defaultdict(lambda: ".")

        self.max_x = len(lines[0])
        self.max_y = len(lines)

        for x in range(0, self.max_x):
            for y in range(0, self.max_y):
                self.ground[(x, y)] = lines[y][x]
                if lines[y][x] == "S":
                    self.starting_point = (x,y)

    def visit(self, pos:tuple[int, int], origin: tuple[int, int])->tuple[int, int]:
        # print(f"{origin}->{pos}: {self.ground[pos]}")
        if self.ground[pos] == "|":
            if origin[1] == pos[1] + 1:
                return (pos[0], pos[1] - 1)
            else:
                return (pos[0], pos[1] + 1)

        if self.ground[pos] == "-":
            if origin[0] == pos[0] + 1:
                return (pos[0] - 1, pos[1])
            else:
                return (pos[0] + 1, pos[1])

        if self.ground[pos] == "L":
            if origin[1] == pos[1]:
                return (pos[0], pos[1] - 1)
            else:
                return (pos[0] + 1, pos[1])

        if self.ground[pos] == "J":
            if origin[1] == pos[1]:
                return (pos[0], pos[1] - 1)
            else:
                return (pos[0] - 1, pos[1])

        if self.ground[pos] == "7":
            if origin[1] == pos[1]:
                return (pos[0], pos[1] + 1)
            else:
                return (pos[0] - 1, pos[1])

        if self.ground[pos] == "F":
            if origin[1] == pos[1]:
                return (pos[0], pos[1] + 1)
            else:
                return (pos[0] + 1, pos[1])

        print(f"Should not be here in {pos}")
        return pos

    def compute_cycle_length(self) -> int:

        # we compute the cycle length
        (s_x, s_y) = self.starting_point

        if self.ground[(s_x - 1, s_y)] in ("-","F","L"):
            next = (s_x - 1, s_y)
        elif self.ground[(s_x + 1, s_y)] in ("-","7","J"):
            next = (s_x + 1, s_y)
        else:
            next = (s_x, s_y - 1 )

        current = (s_x, s_y)

        steps = 0
        while self.ground[next] != "S":
            to_visit = self.visit(next, current)
            current = next
            next = to_visit
            # print(f"next: {next}")
            steps += 1

        return steps


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
        f = Field([x.strip() for x in lines])
        print(f"star1: {(f.compute_cycle_length()+1)//2}")

