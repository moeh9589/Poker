import random

class Hand:
    def __init__(self, Card1, Card2):
        self.Card1 = Card1
        self.Card2 = Card2

    def get_cards(self, deck):
        self.Card1 = random.choice(deck)
        deck.remove(self.Card1)
        self.Card2 = random.choice(deck)
        deck.remove(self.Card2)
        return deck