# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
wins = 0
losses = 0

START_X = 50
FONT_SIZE = 30
CARD_SPACE = 10

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        ret_str = "Hand contains"
        for i in self.cards:
            ret_str += " "
            ret_str += str(i)
        return ret_str

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        has_aces = False
        for c in self.cards:
            value += VALUES[c.get_rank()]
            if c.get_rank() == 'A':
                has_aces = True
        if has_aces == True and (value + 10) <= 21:
            value += 10
        return value


    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i = 0
        for c in self.cards:
            new_pos = [pos[0] + i * (CARD_SIZE[0] + CARD_SPACE), pos[1]]
            i += 1
            c.draw(canvas, new_pos)

# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s,r))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()

    def __str__(self):
        # return a string representing the deck
        ret_str = "Deck contains"
        for i in self.deck:
            ret_str += " "
            ret_str += str(i)
        return ret_str

def print_console():
    print outcome
    print "Dealer " + str(dealer) + ", Value: " + str(dealer.get_value())
    print "Player " + str(player) + ", Value: " + str(player.get_value())
    print "Wins: " + str(wins) + ", Losses: " + str(losses) + ', Score: ' + str(score)

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, score, losses

    # your code goes here
    if in_play == True:
        score -= 1
        losses += 1
        outcome = "You lost the round."
        print_console()
    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Hand()

    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())

    in_play = True
    outcome = ""
    print "Deal "
    print_console()

def hit():
    # if the hand is in play, hit the player
    global outcome, in_play, score, losses
    if in_play == False:
        return
    print "Hit"
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "You went bust and lose!"
        score -= 1
        losses += 1
        in_play = False
        print_console()
    else:
        outcome = ""

def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global in_play, score, outcome, losses, wins
    if in_play == False:
        return
    print "Stand"
    if player.get_value() > 21:
        outcome = "You have busted. You lose!"
        score -= 1
        losses += 1
        in_play = False
        print_console()
    else:
        while (dealer.get_value() < 17):
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "Dealer busted. You Win!"
            score += 1
            in_play = False
            wins += 1
        elif player.get_value() <= dealer.get_value():
            outcome = "You Lose!"
            score -= 1
            in_play = False
            losses += 1
        else:
            outcome = "You Win!"
            score += 1
            in_play = False
            wins += 1
    # assign a message to outcome, update in_play and score
    print_console()

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global dealer, player, outcome
    canvas.draw_text("Blackjack", [START_X + 10, 100], 50, 'Blue')
    canvas.draw_text("Score " + str(score), [300, 100], FONT_SIZE, 'Black')
    canvas.draw_text("Dealer", [START_X, 190], FONT_SIZE, 'Black')
    canvas.draw_text(outcome, [200, 190], FONT_SIZE, 'Black')
    dealer.draw(canvas, [START_X, 200])
    canvas.draw_text("Player", [START_X, 390], FONT_SIZE, 'Black')
    if in_play == True:
        msg = "Hit or Stand?"
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [START_X + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        msg = "New deal?"
    canvas.draw_text(msg, [200, 390], FONT_SIZE, 'Black')
    player.draw(canvas, [START_X, 400])



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric