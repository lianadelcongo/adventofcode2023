#!/usr/bin/python3.9

import sys
from functools import reduce
from collections import OrderedDict

def hash(chars:str)->int:
    return reduce(lambda curr, ch: 17*(curr+ord(ch))%256, chars, 0)

box:dict[int, OrderedDict] = {}

def set_label(id:int, label:str, value:int):
    if id not in box:
        box[id] = OrderedDict()
    box[id][label] = value

def remove_label(id:int, label:str):
    try:
        del(box[id][label])
    except Exception as e:
        pass

def box_value(id:int):
    s = 0
    if id not in box:
        return 0
    for (i, label) in enumerate(box[id]):
        s += (id + 1) * ( i + 1) * box[id][label]

    return s

def parse_line(line:str):
    if "=" in line:
        (label, value) = line.split("=")
        box = hash(label)
        set_label(box, label, int(value))
    if "-" in line:
        label = line.split("-")[0]
        box = hash(label)
        remove_label(box, label)
    

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
        chains = lines[0].split(",")
        print(f" Star1: {reduce(lambda curr, c: curr + hash(c), chains, 0)}")
        for chain in chains:
            parse_line(chain)
        print(f"Star 2: {sum(map(lambda x:box_value(x), range(0,255)))}")        


