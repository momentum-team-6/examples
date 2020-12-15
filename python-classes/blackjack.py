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


class Deck:
    def __init__(self, suits, ranks, color):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)
        self.color = color

    def __str__(self):
        return f'{self.color} deck'
    
    def shuffle(self:
        '''rearranges cards in a random order'''
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name} is holding {self.hand}"

    def hit(self):
        '''removes next card from deck and adds to player's hand'''
        pass


class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = []


class Game:
    def __init__(self, player_name, suits, ranks, deck_color):
        self.player = Player(player_name)
        self.dealer = Dealer()
        self.deck = Deck(suits, ranks, deck_color)

    def turn(self):
        '''player hits until they decide to stay, then dealer hits until they 
           decide to stay'''
        pass

    def play(self):
        '''gameplay events in order happen here'''
        pass



# to build one card
# three_of_hearts = Card("❤️", 3)

# instantiate a deck using the suits and ranks defined by the constants above 
# and save it to a variable
# my_deck = Deck(SUITS, RANKS)

# print out the human-readable representation of each card you made
# for card in my_deck.cards:
#     print(card)

# instantiate a new game
# new_game = Game("Rebecca", SUITS, RANKS, "green")
