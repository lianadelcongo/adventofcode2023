import pytest
import day1

def test_nums_from_line():
    assert(day1.parse_line("1aa2") == 12)
    assert(day1.parse_line("aaaa1aa2ddd") == 12)
    assert(day1.parse_line("4aaaa1a3de3d45a2ddd") == 42)


def test_nums_with_literals():
    assert(day1.parse_line(day1.replace_literals("one2threefourfivesixseveneight7")) == 17)
    assert(day1.parse_line(day1.replace_literals("1one2threefour3deseveneight7six")) == 16)
    assert(day1.parse_line(day1.replace_literals("eighttwothree")) == 83)

def test_second_star():
    text = []
    text.append("atwo1nine")
    text.append("eightwothree")
    text.append("abcone2threexyz")
    text.append("xtwone3four")
    text.append("4nineeightseven2")
    text.append("zoneight234")
    text.append("7pqrstsixteen")

    converted = ["a219", "8wo3", "abc123xyz", "x2ne34", "49872", "z1ight234", "7pqrst6teen"]
    first_step = [day1.replace_literals(x) for x in text]

    calibs = [29, 83, 13, 24, 42, 14, 76]

    res = [day1.parse_line(x) for x in first_step]
    assert(calibs == res)