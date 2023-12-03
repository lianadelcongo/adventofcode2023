#!/usr/bin/python3

import sys

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

def is_symbol(x:int, y:int, lines:"list[str]")->bool:
    if x < 0 or y < 0 or x >=len(lines[0]) or y>=len(lines):
        return False
    if lines[y][x].isnumeric() or lines[y][x] == ".":
        return False
    return True

def find_symbol(start_x:int, end_x:int, y:int, lines:"list[str]")->bool:
    left = is_symbol(start_x-1, y-1, lines) or is_symbol(start_x-1, y, lines) or is_symbol(start_x-1, y+1, lines)
    right = is_symbol(end_x+1, y-1, lines) or is_symbol(end_x+1, y, lines) or is_symbol(end_x+1, y+1, lines)
    if left or right:
        return True
    for i in range(start_x, end_x+1):
        if is_symbol(i,y+1, lines) or is_symbol(i,y-1, lines):
            return True
    return False

def find_numbers(lines: "list[str]")->"list[int]":
    max_x = len(lines[0])
    max_y = len(lines)

    nums = []
    for y in range(0, max_y):
        num=""
        print(f"Y {y}")
        for x in range(0, max_x):
            print(f"{y}-{x} {max_y} {max_x}")
            if lines[y][x].isnumeric():
                if len(num) == 0:
                    startx = x
                num += lines[y][x]
            elif len(num) > 0:
                has_symbol = find_symbol(startx, x-1, y, lines)
                if has_symbol:
                    nums.append(int(num))
                num = ""
        # At line end
        if len(num) > 0:
                has_symbol = find_symbol(startx, x, y, lines)
                if has_symbol:
                    nums.append(int(num))
                num = ""
    print(f"{nums}")
    return nums



if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    lines = read_file_lines(file_path)
    if lines is not None:
        numbers = find_numbers([l.strip() for l in lines])
    print("Star 1: %d"%(sum(numbers)))



