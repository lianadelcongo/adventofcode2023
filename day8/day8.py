#!/usr/bin/python3

import sys

class Route:
    def __init__(self, name:str, left:str, right:str):
        self.name = name
        self.left = left
        self.right = right
    
    def go(self, direction: str) -> str:
        if direction == "L":
            return self.left
        if direction == "R":
            return self.right
        return "WRONG"

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
        instructions = lines[0].strip()
        routes : "dict[str, Route]" = {}
        for line in lines[2:]:
            name = line[0:3]
            left = line[7:10]
            right = line[12:15]

            routes[name] = Route(name, left, right)
        
        pos = "AAA"
        steps = 0
        while (pos != "ZZZ"):
            for ins in instructions:
                steps += 1
                pos = routes[pos].go(ins)
        print(f"Star 1: {steps}")


