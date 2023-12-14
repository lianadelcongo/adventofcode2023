from day14 import Dish

def test_star1():
    lines = ("O....#....",
             "O.OO#....#",
             ".....##...",
             "OO.#O....O",
             ".O.....O#.",
             "O.#..O.#.#",
             "..O..#O..O",
             ".......O..",
             "#....###..",
             "#OO..#....")
    
    d = Dish(lines)
    d.tilt_north()
    assert(d.weight() == 136)