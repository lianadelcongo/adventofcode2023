import day2


def test_single_game_extraction():
    line0 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    info = day2.extract_info(line0)
    assert(info == day2.Info(1, 4, 2, 6))
    line1 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    info = day2.extract_info(line1)
    assert(info == day2.Info(2, 1, 3, 4))
    line2 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    info = day2.extract_info(line2)
    assert(info == day2.Info(3, 20, 13, 6))
    line3 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    info = day2.extract_info(line3)
    assert(info == day2.Info(4, 14, 3, 15))
    line4 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    info = day2.extract_info(line4)
    assert(info == day2.Info(5, 6, 3, 2))

def test_possible_games():
    line0 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert(day2.possible(line0) == 1)
    line1 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    assert(day2.possible(line1) == 2)
    line2 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert(day2.possible(line2) == 0)
    line3 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    assert(day2.possible(line3) == 0)
    line4 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    assert(day2.possible(line4) == 5)

def test_power():
    line0 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    info = day2.extract_info(line0)
    assert(info.power() == 48)
    line1 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    info = day2.extract_info(line1)
    assert(info.power() == 12)
    line2 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    info = day2.extract_info(line2)
    assert(info.power() == 1560)
    line3 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    info = day2.extract_info(line3)
    assert(info.power() == 630)
    line4 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    info = day2.extract_info(line4)
    assert(info.power() == 36)

