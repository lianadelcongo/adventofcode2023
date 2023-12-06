#!/usr/bin/python3

import sys
import functools

class Race:
    def __init__(self, time: int, record: int):
        self.time = time
        self.record = record
    
    def compute_distance(self, button_time: int) -> int:
        speed = button_time
        return speed*(self.time - button_time)

    def get_victories(self) -> int:
        distances = [self.compute_distance(t) for t in range(1,self.time)]
        return len(list(filter(lambda x: x > self.record, distances)))

def compute_answer(races: "list[Race]")->int:
    return functools.reduce(lambda x,y:x*y, map(lambda x: x.get_victories(), races))

if __name__ == "__main__":
    races = []
    races.append(Race(54, 446))
    races.append(Race(81, 1292))
    races.append(Race(70, 1035))
    races.append(Race(88, 1007))

    ans = functools.reduce(lambda x,y:x*y, map(lambda x: x.get_victories(), races))
    print(f"Star1: {ans}")

    print(f"Star2: {Race(54817088, 446129210351007).get_victories()}")

    


