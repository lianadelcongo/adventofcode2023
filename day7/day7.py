#!/usr/bin/python3

import sys
from enum import Enum
from collections import Counter

class Type(Enum):
    REPOKER = 7
    POKER = 6
    FULL = 5
    THREE = 4
    TWO_TWO = 3
    PAIR = 2
    NOTHING = 1
 
class Play():
    def __init__(self, hand:str, bid:int = 0):
        self.hand = hand
        self.bid  = bid
        self.type = self.compute_type()

    def compute_type(self) -> Type:
        c = Counter(self.hand)
        if len(c) == 1:
            return Type.REPOKER
        if len(c) == 5:
            return Type.NOTHING
        
        sizes = [c[x] for x in c]

        if 4 in sizes:
            return Type.POKER
        
        if 3 in sizes:
            if 2 in sizes:
                return Type.FULL
            else:
                return Type.THREE
        
        if len(sizes) == 3:
            return Type.TWO_TWO
        return Type.PAIR

    def is_better_hand_by_card(self, other) -> bool:
        order = "AKQJT98765432"
        for i in range(0, len(self.hand)):
            if self.hand[i] == other.hand[i]:
                continue
            return order.index(self.hand[i]) < order.index(other.hand[i])
        return False

    def __lt__(self, other):
        if self.type != other.type:
            return self.type.value < other.type.value
        return not self.is_better_hand_by_card(other)



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
        plays = []
        for line in lines:
            (hand, bid) = line.split(" ")
            plays.append(Play(hand, int(bid)))
            sorted_plays = sorted(plays)

        ans = 0
        for i in range(1, len(sorted_plays) + 1):
            ans += sorted_plays[i-1].bid * i
        
        print(f"Star 1: {ans}")

