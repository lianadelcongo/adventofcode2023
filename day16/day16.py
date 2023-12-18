#!/usr/bin/python3.9

import sys
from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Laser:
    pos: Point
    direction: Direction

class Grid:
    def __init__(self, lines:"list[str]", laser:Laser):
        self.max_y = len(lines)
        self.max_x = len(lines[0])
        self.energized:set[tuple[Point,Direction]] = set()
        self.lasers:list[Laser] = [laser]
        self.grid = lines

    def energized_tiles(self)->int:
        return len(set([p for (p,d) in self.energized]))


    def step(self):
        new_lasers = []
        for laser in self.lasers:
            if laser.pos.x < 0 or laser.pos.y < 0 or laser.pos.x == self.max_x or laser.pos.y == self.max_y:
                continue
            if (Point(laser.pos.x, laser.pos.y), laser.direction) in self.energized:
                continue # Already checked this path
            self.energized.add((Point(laser.pos.x, laser.pos.y), laser.direction))
            if laser.direction == Direction.RIGHT:
                if self.grid[laser.pos.y][laser.pos.x] in ("\\", "|"):
                    new_lasers.append(Laser(Point(laser.pos.x, laser.pos.y+1), Direction.DOWN))
                if self.grid[laser.pos.y][laser.pos.x] in ("/", "|"):
                    new_lasers.append(Laser(Point(laser.pos.x, laser.pos.y-1), Direction.UP))
                if self.grid[laser.pos.y][laser.pos.x] in (".", "-"):
                    new_lasers.append(Laser(Point(laser.pos.x+1, laser.pos.y), Direction.RIGHT))
                

            elif laser.direction == Direction.LEFT:
                if self.grid[laser.pos.y][laser.pos.x] in ("/", "|"):
                    new_lasers.append(Laser(Point(laser.pos.x, laser.pos.y+1), Direction.DOWN))
                if self.grid[laser.pos.y][laser.pos.x] in ("\\", "|"):
                    new_lasers.append(Laser(Point(laser.pos.x, laser.pos.y-1), Direction.UP))
                if self.grid[laser.pos.y][laser.pos.x] in (".", "-"):
                    new_lasers.append(Laser(Point(laser.pos.x-1, laser.pos.y), Direction.LEFT))
                
            elif laser.direction == Direction.DOWN:
                if self.grid[laser.pos.y][laser.pos.x] in ("/","-"):
                    new_lasers.append(Laser(Point(laser.pos.x - 1, laser.pos.y), Direction.LEFT))
                if self.grid[laser.pos.y][laser.pos.x] in ("\\","-"):
                    new_lasers.append(Laser(Point(laser.pos.x + 1, laser.pos.y), Direction.RIGHT))
                if self.grid[laser.pos.y][laser.pos.x] in ("|","."):
                    new_lasers.append(Laser(Point(laser.pos.x, laser.pos.y + 1), Direction.DOWN))
                
            elif laser.direction == Direction.UP:
                if self.grid[laser.pos.y][laser.pos.x] in ("\\","-"):
                    new_lasers.append(Laser(Point(laser.pos.x - 1, laser.pos.y), Direction.LEFT))
                if self.grid[laser.pos.y][laser.pos.x] in ("/","-"):
                    new_lasers.append(Laser(Point(laser.pos.x + 1, laser.pos.y), Direction.RIGHT))
                if self.grid[laser.pos.y][laser.pos.x] in ("|","."):
                    new_lasers.append(Laser(Point(laser.pos.x, laser.pos.y - 1), Direction.UP))
                

        self.lasers = new_lasers
        return True if len(self.lasers) > 0 else False
    


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
        g = Grid(lines, Laser(Point(0,0), Direction.RIGHT))
        while g.step() == True:
            continue

        print(f"Star1: {g.energized_tiles()}")

        starting_points = []
        for x in range(0, g.max_x):
            starting_points.append(Laser(Point(x,0), Direction.DOWN))
            starting_points.append(Laser(Point(x,g.max_y-1), Direction.UP))

        for y in range(0, g.max_y):
            starting_points.append(Laser(Point(0, y), Direction.RIGHT))
            starting_points.append(Laser(Point(g.max_x-1, y), Direction.LEFT))

        ans = []
        for initial in starting_points:
            g = Grid(lines, initial)
            while g.step() == True:
                continue

            ans.append(g.energized_tiles())
        
        print(f"Star2: {max(ans)}")
