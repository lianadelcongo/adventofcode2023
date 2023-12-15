import day15

def test_hash():
    assert(day15.hash(0, "HASH") == 52)
    
    assert(day15.hash(0, "rn=1") == 30)
    assert(day15.hash(0, "cm-") == 253)
    assert(day15.hash(0, "qp=3") == 97)
    assert(day15.hash(0, "cm=2") == 47)
    assert(day15.hash(0, "qp-") == 14)
    assert(day15.hash(0, "pc=4") == 180)
    assert(day15.hash(0, "ot=9") == 9)
    assert(day15.hash(0, "ab=5") == 197)
    assert(day15.hash(0, "pc-") == 48)
    assert(day15.hash(0, "pc=6") == 214)
    assert(day15.hash(0, "ot=7") == 231)
