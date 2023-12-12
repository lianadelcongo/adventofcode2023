from day12 import Record

def test_validate_valids():
    lines = ("#.#.### 1,1,3", ".#...#....###. 1,1,3", ".#.###.#.###### 1,3,1,6", "####.#...#... 4,1,1", "#....######..#####. 1,6,5", ".###.##....# 3,2,1")
    for line in lines:
        r = Record(line)
        assert(r.check_condition(r.condition) == True)

def test_validate_invalids():
    lines = ("#.##.### 1,1,3", ".#...#....###.# 1,1,3", ".#.###.#.###### 1,3,1,5", "####.#...#...# 4,1,1", "#....######..#####. 1,6", ".###.##....# 3,2,1,3")
    for line in lines:
        r = Record(line)
        assert(r.check_condition(r.condition) == False)

def test_valiate_expansions():
    assert(Record("???.### 1,1,3").valid_expansions() == 1)
    assert(Record(".??..??...?##. 1,1,3").valid_expansions() == 4)
    assert(Record("?#?#?#?#?#?#?#? 1,3,1,6").valid_expansions() == 1)
    assert(Record("????.#...#... 4,1,1").valid_expansions() == 1)
    assert(Record("????.######..#####. 1,6,5").valid_expansions() == 4)
    assert(Record("?###???????? 3,2,1").valid_expansions() == 10)
