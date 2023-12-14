#!/usr/bin/python3.9

import sys
from functools import reduce

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Coords):
            return (self.x, self.y) == (other.x, other.y)
        return False

    def __lt__(self, other):
        # Compare based on x first, then y if x is equal
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y


class Dish():
    def __init__(self, lines: "list[str]"):
        self.max_y = len(lines)
        self.max_x = len(lines[0])

        self.rounded:set[Coords] = set()
        self.cubes:set[Coords]   = set()

        for y in range(0, self.max_y):
            for x in range(0, self.max_x):
                if lines[y][x] == "O":
                    self.rounded.add(Coords(x,y))
                elif lines[y][x] == "#":
                    self.cubes.add(Coords(x,y))
    
    def print(self):
        for y in range(0, self.max_y):
            line = []
            for x in range(0, self.max_x):
                if Coords(x,y) in self.rounded:
                    line.append("O")
                elif Coords(x,y) in self.cubes:
                    line.append("#")
                else:
                    line.append(".")
            print("".join(line))
        print("--") 

    def tilt_south(self)->None:
        stones = sorted(self.rounded, reverse = True)
        placed_stones = set()

        for stone in stones:
            for new_y in range(stone.y, self.max_y + 1):
                next_pos = Coords(stone.x, new_y)
                if next_pos in self.cubes or next_pos in placed_stones or new_y == self.max_y:
                    placed_stones.add(Coords(stone.x, new_y-1))
                    break

        self.rounded = placed_stones
        return

    def tilt_north(self)->None:
        stones = sorted(self.rounded)
        placed_stones = set()

        for stone in stones:
            for new_y in range(stone.y, -2, -1):
                next_pos = Coords(stone.x, new_y)
                if next_pos in self.cubes or next_pos in placed_stones or new_y == -1:
                    placed_stones.add(Coords(stone.x, new_y+1))
                    break

        self.rounded = placed_stones
        return

    def tilt_west(self)->None:
        stones = sorted(self.rounded)
        placed_stones = set()

        for stone in stones:
            for new_x in range(stone.x, -2, -1):
                next_pos = Coords(new_x, stone.y)
                if next_pos in self.cubes or next_pos in placed_stones or new_x == -1:
                    placed_stones.add(Coords(new_x + 1, stone.y))
                    break

        self.rounded = placed_stones
        return

    def tilt_east(self)->None:
        stones = sorted(self.rounded, reverse = True)
        placed_stones = set()

        for stone in stones:
            for new_x in range(stone.x, self.max_x + 1):
                next_pos = Coords(new_x, stone.y)
                if next_pos in self.cubes or next_pos in placed_stones or new_x == self.max_x:
                    placed_stones.add(Coords(new_x - 1, stone.y))
                    break

        self.rounded = placed_stones
        return


    def weight(self)->int:
        return reduce(lambda x,y: x + (self.max_y-y.y), self.rounded, 0)



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
        d = Dish(lines)
        d.tilt_north()
        d.print()
        print(f"Star 1 :{d.weight()}")

        d2 = Dish(lines)
        print("The second star is to be deduced rom the printed serie, looking for the cycle.")
        for i in range(0, 1000000000):
        #for i in range(0, 1):
            d2.tilt_north()
            #d2.print()
            d2.tilt_west()
            #d2.print()
            d2.tilt_south()
            #d2.print()
            d2.tilt_east()
            #d2.print()
            print(f"{i+1}: {d2.weight()}")


