#!/usr/bin/python3

import sys

class Record:
    def __init__(self, line:str):
        (condition, size) = line.split(" ")
        self.condition = condition
        self.size = [int(x) for x in size.split(",")]
    
    def check_condition(self, cond) -> bool:
        group_being_checked = 0
        consecutive = 0
        in_sequence = False
        
        for item in cond:
            if item == "#":
                consecutive += 1
                in_sequence = True
            elif in_sequence == True:
                if group_being_checked == len(self.size):
                    return False
                if self.size[group_being_checked] != consecutive:
                    return False
                group_being_checked += 1
                consecutive = 0
                in_sequence = False
        
        if in_sequence == True:
            if len(self.size) == group_being_checked + 1 and self.size[group_being_checked] == consecutive: 
                return True
            return False
        elif len(self.size) == group_being_checked:
            return True


        return False

    def valid_expansions(self)->int:
        to_expand = [self.condition]
        expanded = []

        while len(to_expand) > 0:
            item = to_expand.pop()
            if "?" not in item:
                expanded.append(item)
                continue
            pos = item.find("?")
            to_expand.append(item.replace("?",".",1))
            to_expand.append(item.replace("?","#",1))

        return [self.check_condition(x) for x in expanded].count(True)

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
            print(f"Star1: {sum([Record(line.strip()).valid_expansions() for line in lines])}")


