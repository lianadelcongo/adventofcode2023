#!/usr/bin/python3.9

import sys

class Ground:
    def __init__(self, lines:list[str], hexa=False):
        self.lines = lines
        self.max_x = 0
        self.max_y = 0
        self.border:set[tuple[int, int]] = set()
        self.hexa = hexa
    
    def run(self)->int:
        self.compute_border()
        self.fill_hole()
        return len(self.border)

    def compute_border(self)->None:
        x = 0
        y = 0
        self.border.add((x,y))

        for line in self.lines:
            (direction, amount, rgb) = line.split(" ")
            if self.hexa == True:
                amount = int(rgb[2:-2],16)
                dir = rgb[-2:-1]
                if dir == "0":
                    direction = "R"
                elif dir == "1":
                    direction = "D"
                elif dir == "2":
                    direction = "L"
                else:
                    direction = "U"    
            for offset in range(0, int(amount)):
                if direction == "U":
                     y -= 1
                if direction == "D":
                     y += 1
                if direction == "L":
                     x -= 1
                if direction == "R":
                     x += 1
                self.border.add((x,y))
            
            self.max_x = max(x, self.max_x)
            self.max_y = max(y, self.max_y)
    
    def fill_hole(self)->None:
        points_to_expand:list[tuple[int, int]] = [(1,1)]
        while len(points_to_expand) > 0:
            (x, y) = points_to_expand.pop()
            for (xx, yy) in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                if (xx, yy) not in self.border:
                    points_to_expand.append((xx, yy))
                    self.border.add((xx, yy))


    def print_hole(self):
        for y in range(0, self.max_y+1):
            line = []
            for x in range(0, self.max_x+1):
                if (x,y) in self.border:
                    line.append("#")
                else:
                    line.append(".")
            print("".join(line))

def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [l.strip() for l in lines]
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
        g = Ground(lines)
        print(f"Star 1: {g.run()}")
        g = Ground(lines, hexa=True)
        print(f"Star 2: {g.run()}")
