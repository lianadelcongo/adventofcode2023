from day13 import Figure

def test_horizontal_reflection():
    fig1 = ("#.##..##." \
           ,"..#.##.#." \
           ,"##......#" \
           ,"##......#" \
           ,"..#.##.#." \
           ,"..##..##." \
           ,"#.#.##.#.")
    
    assert(Figure(fig1).column_reflection() == 5)

    fig2 = ("#...##..#", \
            "#....#..#", \
            "..##..###", \
            "#####.##.", \
            "#####.##.", \
            "..##..###", \
            "#....#..#")
    
    assert(Figure(fig2).column_reflection() == 0)

def test_vertical_reflection():
    fig1 = ("#.##..##." \
           ,"..#.##.#." \
           ,"##......#" \
           ,"##......#" \
           ,"..#.##.#." \
           ,"..##..##." \
           ,"#.#.##.#.")
    
    assert(Figure(fig1).row_reflection() == 0)

    fig2 = ("#...##..#", \
            "#....#..#", \
            "..##..###", \
            "#####.##.", \
            "#####.##.", \
            "..##..###", \
            "#....#..#")
    
    assert(Figure(fig2).row_reflection() == 400)

def test_horizontal_reflection_with_smudge():
    fig1 = ("#.##..##." \
           ,"..#.##.#." \
           ,"##......#" \
           ,"##......#" \
           ,"..#.##.#." \
           ,"..##..##." \
           ,"#.#.##.#.")
    
    assert(Figure(fig1).column_reflection(1) == 0)

    fig2 = ("#...##..#", \
            "#....#..#", \
            "..##..###", \
            "#####.##.", \
            "#####.##.", \
            "..##..###", \
            "#....#..#")
    
    assert(Figure(fig2).column_reflection(1) == 0)

def test_vertical_reflection_with_smudge():
    fig1 = ("#.##..##." \
           ,"..#.##.#." \
           ,"##......#" \
           ,"##......#" \
           ,"..#.##.#." \
           ,"..##..##." \
           ,"#.#.##.#.")
    
    assert(Figure(fig1).row_reflection(1) == 300)

    fig2 = ("#...##..#", \
            "#....#..#", \
            "..##..###", \
            "#####.##.", \
            "#####.##.", \
            "..##..###", \
            "#....#..#")
    
    assert(Figure(fig2).row_reflection(1) == 100)
