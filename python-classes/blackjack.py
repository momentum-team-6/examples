SUITS = ["♣️", "❤️", "♦️", "♠️"]
RANKS = ["A", "J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Card:
    def __init__(self, suit, rank):
        # called when you instantiate the class as we do in line 16   
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # returns a human-readable representation of the object
        return f'card is a {self.rank} of {self.suit}'


# to build one card
three_of_hearts = Card("❤️", 3)


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)


# instantiate a deck using the suits and ranks defined by the constants above 
# and save it to a variable
my_deck = Deck(SUITS, RANKS)


# print out the human-readable representation of each card you made
for card in my_deck.cards:
    print(card)
