#!/usr/bin/python3

import sys
from collections import Counter


class Sequence():

    def __init__(self, seq:str):
        self.seq = [int(x) for x in seq.split(" ")]
    
    def complete(self)->"tuple[int, int]":
        all_seqs = [self.seq]
        seq = self.seq
        while True:
            down = []
            for i in range(1, len(seq)):
                down.append(seq[i] - seq[i-1])
            all_seqs.append(down)
            c = Counter(down)
            if len(c) == 1:
                break # do here
            seq = down
        
        # we have all the sequences down, no we go up
        for (i, seq) in reversed(list(enumerate(all_seqs))):
            if (i == len(all_seqs)-1):
                continue
            all_seqs[i].append(all_seqs[i][-1] + all_seqs[i+1][-1])
            all_seqs[i].insert(0, all_seqs[i][0] - all_seqs[i+1][0])    
        self.seq = all_seqs[0]
        return (self.seq[0], self.seq[-1])

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

        seqs = []
        for line in lines:
            seqs.append(Sequence(line).complete())
        
        print(f"Star1: {sum([s[0] for s in seqs])}")
        print(f"Star2: {sum([s[1] for s in seqs])}")