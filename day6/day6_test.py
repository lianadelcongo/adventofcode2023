import day6

def test_race_distance():
    r0 = day6.Race(7, 9)
    r1 = day6.Race(15, 40)
    r2 = day6.Race(30, 200)

    assert(r0.get_victories() == 4)
    assert(r1.get_victories() == 8)
    assert(r2.get_victories() == 9)

def test_first_star():
    races = []
    races.append(day6.Race(7, 9))
    races.append(day6.Race(15, 40))
    races.append(day6.Race(30, 200))

    assert(day6.compute_answer(races) == 288)
    