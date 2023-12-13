#!/usr/bin/python3.9

import sys

class Figure:
    def __init__(self, lines:"list[str]"):
        self.rows = lines

        self.columns = []
        for x in range(0, len(lines[0])):
            column = []
            for y in range(0, len(lines)):
                column.append(lines[y][x])
            self.columns.append(column)

    def print_columns(self):
        for c in self.columns:
            print("".join(c))

    def reflection(self, lines:"list[str]", smudge = 0)->int:
        for c in range(0, len(lines)-1):
            differences = 0
            for offset in range(0, len(lines)-1):
                if c-offset >= 0 and c+1+offset < len(lines):
                    differences += len([x for x in zip(lines[c-offset], lines[c+1+offset]) if x[0] != x[1]])
            else:
                if differences == smudge:
                        return c+1
        return 0
    
    def column_reflection(self, smudge = 0)->int:
        return self.reflection(self.columns, smudge)

    def row_reflection(self, smudge = 0)->int:
        return self.reflection(self.rows, smudge)*100


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
        lines = [x.strip() for x in lines]
        star1 = 0
        star2 = 0
        figure = []
        for line in lines:
            if line == "":
                f = Figure(figure)
                star1 += f.column_reflection() + f.row_reflection()
                star2 += f.column_reflection(1) + f.row_reflection(1)
                figure = []
            else:
                figure.append(line)
        print(f"Star1: {star1}")
        print(f"Star2: {star2}")
            


