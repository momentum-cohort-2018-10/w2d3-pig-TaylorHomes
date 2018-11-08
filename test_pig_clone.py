from pig_clone import Dice, Score, Player


def test_create_dice():
    dice = dice(6)
    assert dice == 6


# rom blackjack import Card, Deck, Hand


# def test_create_card():
#     card = Card(9, "Clubs")
#     assert card.rank == 9
#     assert card.suit == "Clubs"
