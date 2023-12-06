#!/usr/bin/python3

import sys
import functools

class Section:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
    
    def __str__(self) -> str:
        return f"start: {self.start} - end: {self.end}"

class Range:
    def __init__(self, destination:int, source:int, range: int):
        self.destination = destination
        self.source = source
        self.range  = range
    
    def split_section(self, section:Section) -> "list[Section]":
        # Out left
        if section.end < self.source:
            return [section]
        # Out right
        if section.start >= self.source + self.range:
            return [section]
        # In left
        if section.start < self.source and section.end >= self.source and section.end < (self.source + self.range):
            return [Section(section.start, self.source-1), Section(self.source, section.end)]
        # In right
        if section.start >= self.source and section.end >= (self.source + self.range):
            return [Section(section.start, self.source + self.range - 1), Section(self.source + self.range, section.end)]
        # Section bigger than range, including it
        if section.start < self.source and section.end >= (self.source + self.range):
            return [Section(section.start, self.source - 1), Section(self.source, self.source + self.range - 1), Section(self.source + self.range, section.end)]
        # full included
        return [section]

    def convert(self, section:Section) -> "tuple[Section,bool]":
        if section.start >= self.source and section.end < (self.source + self.range):
            return (Section(self.destination + (section.start - self.source), self.destination + (section.end - self.source)), True)
        return (section, False)

class Conversor:
    def __init__(self, name:str):
        self.name = name
        self.ranges: list[Range] = []
    
    def add_range(self, range:Range) -> None:
        self.ranges.append(range)
    
    def convert(self, sections: "list[Section]") -> "list[Section]":
        current_sections: "list[Section]" = sections
        next_sections: "list[Section]" = []
        for r in self.ranges:
            for section in current_sections:
                next_sections.extend(r.split_section(section))

            current_sections = next_sections
            next_sections = []


        transformed_sections: "list[Section]" = []
        pending_sections: "list[Section]" = current_sections
        # the problem is here, i cannot convert a converted section, as its range can have changed
        for section in pending_sections:
            for r in self.ranges:
                (new_section, transformed) = r.convert(section)
                if transformed:
                    transformed_sections.append(new_section)
                    break
            else:
                transformed_sections.append(section)

        return transformed_sections

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
        seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
        sections:"list[Section]" = []
        for i in range(0, len(seeds), 2):
            sections.append(Section(seeds[i], seeds[i] + seeds[i+1] - 1))
        conversors : "list[Conversor]" = []
        for line in lines[1:]:
            if len(line) < 2:
                continue
            if "map" in line:
                   conversors.append(Conversor(line))
            else:
                (dest, source, range) = line.split(" ")
                conversors[-1].add_range(Range(int(dest), int(source), int(range)))

        for c in conversors:
            sections = c.convert(sections)
        
        starts = [x.start for x in sections]        

        print(f"Second star: {min(starts)}")

