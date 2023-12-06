#!/usr/bin/python3

import sys
import functools

class Range:
    def __init__(self, destination:int, source:int, range: int):
        self.destination = destination
        self.source = source
        self.range  = range
    
    def in_range(self, value:int) -> bool:
        return value >= self.source and value <= (self.source + self.range)
    
    def convert(self, value:int) -> int:
        return self.destination + (value-self.source)

class Conversor:
    def __init__(self, name:str):
        self.name = name
        self.ranges: list[Range] = []
    
    def add_range(self, range:Range) -> None:
        self.ranges.append(range)
    
    def convert(self, value:int) -> int:
        for r in self.ranges:
            if r.in_range(value):
                return r.convert(value)
        return value

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
        seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
        conversors : "list[Conversor]" = []
        for line in lines[1:]:
            if len(line) < 2:
                continue
            if "map" in line:
                   conversors.append(Conversor(line))
            else:
                (dest, source, range) = line.split(" ")
                conversors[-1].add_range(Range(int(dest), int(source), int(range)))
            
        end = [functools.reduce(lambda v, c: c.convert(v), conversors, seed) for seed in seeds]
        print(f"First star: {min(end)}")

