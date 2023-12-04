import day4
import day4_star2 as st2

def test_parse_card():
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert(day4.parse_line(card) == 8)
    card = "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
    assert(day4.parse_line(card) == 2)
    card = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
    assert(day4.parse_line(card) == 2)
    card = "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
    assert(day4.parse_line(card) == 1)
    card = "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"
    assert(day4.parse_line(card) == 0)
    card = "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    assert(day4.parse_line(card) == 0)

def test_process_cards():
    cards = {}
    card = st2.Card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert(card.id == 1)
    cards[card.id] = card
    card = st2.Card("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    assert(card.id == 2)
    cards[card.id] = card
    card = st2.Card("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    assert(card.id == 3)
    cards[card.id] = card
    card = st2.Card("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
    assert(card.id == 4)
    cards[card.id] = card
    card = st2.Card("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    assert(card.id == 5)
    cards[card.id] = card
    card = st2.Card("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    assert(card.id == 6)
    cards[card.id] = card
    assert(st2.process_cards(cards) == 30)
