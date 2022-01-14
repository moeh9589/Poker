class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.string = ''

    def card_string(self):
        self.string = str(self.value) + self.suit
        return self.string
