#!/usr/bin/python3

import sys

class Card:
    def __init__(self, line : str):
        (id, numbers) = line.split(":")
        self.id = int(id.split(" ")[-1])
        (winners, in_card) = numbers.split("|")
        self.win_set = set([int(x.strip()) for x in filter(lambda x: len(x) > 0, winners.strip().split(" "))])
        self.card_set = set([int(x.strip()) for x in filter(lambda x: len(x) > 0, in_card.strip().split(" "))])
        self.matches = len(self.win_set.intersection(self.card_set))


def process_cards(cards: "dict[int, Card]") -> int:
    processed = 0
    pending = {k:1 for k in cards} # the number of pending cards for each card id
    for round in range(1, len(cards) + 1):
        processed += pending[round]
        for i in range(1, cards[round].matches+1):
            pending[round + i] += pending[round]

    return processed

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
        cards = {}
        for line in lines:
            c = Card(line)
            cards[c.id] = c
        print(f"star2: {process_cards(cards)}")
