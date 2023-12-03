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

def is_symbol(y:int, x:int, lines:"list[str]")->bool:
    if x < 0 or y < 0 or x >=len(lines[0]) or y>=len(lines):
        return False
    if lines[y][x] == "*":
        return True
    return False

def find_symbol(start_x:int, end_x:int, y:int, lines:"list[str]")-> "tuple[int, int] | None":
    for pos in ((y-1, start_x-1), (y, start_x-1), (y+1, start_x-1), (y-1, end_x+1), (y, end_x+1), (y+1, end_x+1)):
        if is_symbol(pos[0], pos[1], lines):
            return pos
    
    for i in range(start_x, end_x+1):
        if is_symbol(y+1,i, lines):
            return (y+1,i)
        if is_symbol(y-1,i, lines):
            return (y-1,i)
    return None

def find_gears(lines: "list[str]")->"list[int]":
    max_x = len(lines[0])
    max_y = len(lines)

    gears = {} # "map[(int, int):[int]]"
    for y in range(0, max_y):
        num=""
        for x in range(0, max_x):
            if lines[y][x].isnumeric():
                if len(num) == 0:
                    startx = x
                num += lines[y][x]
            elif len(num) > 0:
                symbol_pos = find_symbol(startx, x-1, y, lines)
                if symbol_pos is not None:
                    if symbol_pos not in gears:
                        gears[symbol_pos] = []
                    gears[symbol_pos].append(int(num))
                num = ""
        # At line end
        if len(num) > 0:
            symbol_pos = find_symbol(startx, x-1, y, lines)
            if symbol_pos is not None:
                if symbol_pos not in gears:
                    gears[symbol_pos] = []
                gears[symbol_pos].append(int(num))
            num = ""
    return [gears[gear] for gear in gears if len(gears[gear])==2]



if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    lines = read_file_lines(file_path)
    if lines is not None:
        gears = find_gears([l.strip() for l in lines])
        prods = 0
        for g in gears:
            prods += g[0]*g[1] 
        print("Star 2: %d"%(prods))

