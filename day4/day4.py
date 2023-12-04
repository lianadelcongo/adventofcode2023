#!/usr/bin/python3

import sys

def parse_line(line : str) -> int:
    (id, numbers) = line.split(":")
    (winners, in_card) = numbers.split("|")
    win_set = set([int(x.strip()) for x in filter(lambda x: len(x) > 0, winners.strip().split(" "))])
    card_set = set([int(x.strip()) for x in filter(lambda x: len(x) > 0, in_card.strip().split(" "))])
    matches = win_set.intersection(card_set)
    if (len(matches) == 0):
        return 0
    if (len(matches) == 1):
        return 1
    return 2**(len(matches)-1)


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
        res = sum(map(parse_line, lines))
        print("first star: %s", res)
