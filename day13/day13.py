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

    def reflection(self, lines:"list[str]")->int:
        ret = 0
        for c in range(0, len(lines)-1):
            for offset in range(0, len(lines)-1):
                if c-offset >= 0 and c+1+offset < len(lines):
                    if lines[c-offset] != lines[c+1+offset]:
                        break
            else:
                ret += c+1
        return ret
    
    def column_reflection(self)->int:
        return self.reflection(self.columns)

    def row_reflection(self)->int:
        return self.reflection(self.rows)*100


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
        figure = []
        for line in lines:
            if line == "":
                f = Figure(figure)
                star1 += f.column_reflection() + f.row_reflection()
                figure = []
            else:
                figure.append(line)
        print(f"Star1: {star1}")

            


