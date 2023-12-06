import day5
import functools

def test_conversion():
    c = day5.Conversor("test")
    c.add_range(day5.Range(50, 98, 2))
    c.add_range(day5.Range(52, 50, 48))

    assert(c.convert(0) == 0)
    assert(c.convert(1) == 1)
    assert(c.convert(49) == 49)
    assert(c.convert(50) == 52)
    assert(c.convert(51) == 53)
    assert(c.convert(96) == 98)
    assert(c.convert(97) == 99)
    assert(c.convert(98) == 50)
    assert(c.convert(99) == 51)

def test_nested_conversion():
    tests = {79:82, 14:43, 55:86, 13:35}

    conversors = []
    c = day5.Conversor("test1")
    c.add_range(day5.Range(50, 98, 2))
    c.add_range(day5.Range(52, 50, 48))
    conversors.append(c)

    c = day5.Conversor("test2")
    c.add_range(day5.Range(0, 15, 37))
    c.add_range(day5.Range(37, 52, 2))
    c.add_range(day5.Range(39, 0, 15))
    conversors.append(c)

    c = day5.Conversor("test3")
    c.add_range(day5.Range(49, 53, 8))
    c.add_range(day5.Range(0, 11, 42))
    c.add_range(day5.Range(42, 0, 7))
    c.add_range(day5.Range(57, 7, 4))
    conversors.append(c)

    c = day5.Conversor("test4")
    c.add_range(day5.Range(88, 18, 7))
    c.add_range(day5.Range(18, 25, 70))
    conversors.append(c)

    c = day5.Conversor("test5")
    c.add_range(day5.Range(45, 77, 23))
    c.add_range(day5.Range(81, 45, 19))
    c.add_range(day5.Range(68, 64, 13))
    conversors.append(c)

    c = day5.Conversor("test6")
    c.add_range(day5.Range(0, 69, 1))
    c.add_range(day5.Range(1, 0, 69))
    conversors.append(c)

    c = day5.Conversor("test7")
    c.add_range(day5.Range(60, 56, 37))
    c.add_range(day5.Range(56, 93, 4))
    conversors.append(c)

    for input in tests:
        assert(tests[input] == functools.reduce(lambda v, c: c.convert(v), conversors, input))