import day7

def test_correct_type():
    assert(day7.Play("AAAAA").type == day7.Type.REPOKER)
    assert(day7.Play("AA2AA").type == day7.Type.POKER)
    assert(day7.Play("2AAAA").type == day7.Type.POKER)
    assert(day7.Play("A2A2A").type == day7.Type.FULL)
    assert(day7.Play("2A2AA").type == day7.Type.FULL)
    assert(day7.Play("2AAA3").type == day7.Type.THREE)
    assert(day7.Play("AA3A2").type == day7.Type.THREE)
    assert(day7.Play("AA232").type == day7.Type.TWO_TWO)
    assert(day7.Play("2AA32").type == day7.Type.TWO_TWO)
    assert(day7.Play("A3A45").type == day7.Type.PAIR)
    assert(day7.Play("354AA").type == day7.Type.PAIR)
    assert(day7.Play("AJK32").type == day7.Type.NOTHING)
    assert(day7.Play("62345").type == day7.Type.NOTHING)
    assert(day7.Play("87654").type == day7.Type.NOTHING)

def test_compare_plays():
    assert(day7.Play("AAAAA") > day7.Play("AA2AA"))
    assert(day7.Play("AA2AA") > day7.Play("2A2AA"))
    assert(day7.Play("AAA22") > day7.Play("AA2A3"))
    assert(day7.Play("A4AA5") > day7.Play("AA227"))
    assert(day7.Play("AA556") > day7.Play("AA245"))
    assert(day7.Play("AA456") > day7.Play("45678"))
    assert(day7.Play("A2347") > day7.Play("A2345"))
    assert(day7.Play("2AAAA") > day7.Play("2222A"))

def test_sort_plays():
    plays = [day7.Play("32T3K"), day7.Play("T55J5"),day7.Play("KK677"),day7.Play("KTJJT"),day7.Play("QQQJA")]
    sorted_plays = [x.hand for x in sorted(plays)]
    assert(sorted_plays == [day7.Play("32T3K").hand,day7.Play("KTJJT").hand,day7.Play("KK677").hand,day7.Play("T55J5").hand,day7.Play("QQQJA").hand])