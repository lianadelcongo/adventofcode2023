#!/usr/bin/python3

import sys

def parse_line(line : str) -> int:
    nums = list(filter(lambda x: x.isnumeric(), line))  
    return 10*int(nums[0]) + int(nums[-1])

def replace_literals(text:str) -> str:
    return text.replace("seven","s7n").replace("nine","n9e").replace("five","f5e").replace("three","t3e").replace("eight","e8t") \
    .replace("one","o1e").replace("two","t2o").replace("four","f4r").replace("six","s6x")

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
        res = sum(map(parse_line, map(replace_literals, lines)))
        print("second star: %s", res)


