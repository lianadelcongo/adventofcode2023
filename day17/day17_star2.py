#!/usr/bin/python3.9

import sys
from enum import Enum
from collections import defaultdict
import heapq

class Direction(Enum):
    INITIAL = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class State:
    def __init__(self, pos = (0,0), blocks = 1, direction = Direction.INITIAL):
        self.pos: tuple[int,int] = pos
        self.blocks:int = blocks
        self.direction:Direction = direction
    
    def __str__(self) -> str:
        return str(self.pos)+"-"+str(self.blocks)+"-"+str(self.direction)
    
    def __hash__(self) -> int:
        return hash((self.pos, self.blocks, self.direction))
    
    def __eq__(self, other)->bool:
        return self.pos == other.pos and self.blocks == other.blocks and self.direction == other.direction
    
    def __lt__(self, other)->bool:
        return self.pos[0] < other.pos[0] and self.pos[1] < other.pos[1] and self.blocks < other.blocks and self.direction.value < other.direction.value

    
    def get_next_in_line(self):
        (x, y) = self.pos
        if self.direction == Direction.LEFT:
            x -= 1
        elif self.direction == Direction.RIGHT:
            x += 1    
        elif self.direction == Direction.UP:
            y -= 1
        elif self.direction == Direction.DOWN:
            y += 1    
        return State((x,y), self.blocks + 1, self.direction)

    def get_left_turn(self):
        (x, y) = self.pos
        direction = Direction.LEFT
        if self.direction == Direction.LEFT:
            direction = Direction.DOWN
            y += 1            
        elif self.direction == Direction.RIGHT:
            direction = Direction.UP
            y -= 1            
        elif self.direction == Direction.UP:
            direction = Direction.LEFT
            x -= 1            
        elif self.direction == Direction.DOWN:
            direction = Direction.RIGHT
            x += 1            
        return State((x,y), 1, direction)

    def get_right_turn(self):
        (x, y) = self.pos
        direction = Direction.LEFT
        if self.direction == Direction.RIGHT:
            direction = Direction.DOWN
            y += 1            
        elif self.direction == Direction.LEFT:
            direction = Direction.UP
            y -= 1            
        elif self.direction == Direction.DOWN:
            direction = Direction.LEFT
            x -= 1            
        elif self.direction == Direction.UP:
            direction = Direction.RIGHT
            x += 1            
        return State((x,y), 1, direction)


    def possible_states(self)->"list[State]":
        possible:"list[State]" = []
        if self.direction == Direction.INITIAL:
            return [State((1,0), 1, Direction.RIGHT), State((0,1), 1, Direction.DOWN)]
        if self.blocks < 10:
            possible.append(self.get_next_in_line())
        if self.blocks >= 4:
            possible.append(self.get_left_turn())
            possible.append(self.get_right_turn())
        # print(f"{str(self)}--->{''.join([str(x) for x in possible])}")
        return possible

class Walk:
    def __init__(self, lines:list[str]):
        self.target_x = len(lines[0])-1
        self.target_y = len(lines)-1
        self.limit = 10000000000000
        self.heat:defaultdict[tuple[int, int], int] = defaultdict(lambda: self.limit)
        for y in range(0, len(lines)):
            for x in range(0, len(lines[0])):
                self.heat[(x,y)] = int(lines[y][x])

    def start(self):
        steps = {}
        steps[State()] = 0
        routes:list[tuple[int, State]] = [(0, State())]
        heapq.heapify(routes)
        while len(routes) > 0:
            # print(f"{len(steps)} {len(routes)}")
            (loss, state) = heapq.heappop(routes)
            # print(f"Checking {state} {loss}")
            if state.pos[0] == self.target_x and state.pos[1] == self.target_y and state.blocks >=4:
                # print(f"Reached target with loss: {loss}")
                if self.limit > loss:
                    self.limit = loss
                continue
            for s in state.possible_states():
                new_loss = loss + self.heat[s.pos]
                if new_loss > self.limit:
                    continue

                if s in steps:
                        continue
                steps[s] = new_loss
                heapq.heappush(routes, (new_loss, s))
        
        #for key in steps:
        #    print(f"steps {key} {steps[key]}")
        print(self.limit)

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
        w = Walk(lines)
        w.start()


