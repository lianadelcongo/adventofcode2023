import day9

def test_complete_sequence():
    assert(day9.Sequence("0 3 6 9 12 15").complete() == (-3,18))
    assert(day9.Sequence("1 3 6 10 15 21").complete() == (0,28))
    assert(day9.Sequence("10 13 16 21 30 45").complete() == (5,68))