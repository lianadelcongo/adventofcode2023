#!/usr/bin/python3

import sys
from dataclasses import dataclass

@dataclass
class Info:
    index: int
    red: int = 0
    green: int = 0
    blue: int = 0

    def power(self):
        return self.red * self.green * self.blue

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

def extract_info(line):
    (index_info, plays) = line.split(':')
    index = int(index_info.split(" ")[1])
    info = Info(index)
    play = plays.split(";")
    for p in play:
        for color in p.split(","):
            (num, name) = color.strip().split(" ")
            num = int(num)
            if name == "red":
                info.red = max(info.red, num)
            elif name == "green":
                info.green = max(info.green, num)
            elif name == "blue":
                info.blue = max(info.blue, num)
    return info

def possible(line: str) -> int:
    info = extract_info(line)
    if info.red <=12 and info.green <= 13 and info.blue <= 14:
        return info.index
    return 0


if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    lines = read_file_lines(file_path)

    if lines is not None:
        s1 = sum([possible(x) for x in lines])
        print("First star: %s"%s1)
        s2 = sum([extract_info(x).power() for x in lines])
        print("Second star: %s"%s2)


