import random
deck = []
player_hand = []
computer_hand = []

card_suits = ["Spades","Hearts","Clubs","Diamonds"]
card_suits = {"Spades":4,"Hearts":3,"Clubs":2,"Diamonds":1}
card_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_values_define = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}

class Card():
    def __init__(self,my_suit,my_value):
        self.suit = my_suit
        self.value = my_value
        self.image_path = "C:\\Users\\katie\\Desktop\\Deck & Extras\\" + self.value + self.suit + ".png.png"
        self.in_use = False

for colour in card_suits:
    for value in card_values:
        deck.append(Card(colour,value))
        print(Card.value, "of", Card.colour)

for player_cards in range(4):
    player_cards = deck[random.randrange(len(deck))]
    while player_cards.in_use == True:
        player_cards = deck[random.randrange(len(deck))] 
        print("Player Hand",player_cards)
    player_hand.append(player_cards)   
player_cards.in_use = True
# Picking 5 Random Cards From The Deck For The Computer Hand
for computer_cards in range(4):
    computer_cards = deck[random.randrange(len(deck))]
    while computer_cards.in_use == True:
        computer_cards = deck[random.randrange(len(deck))]
        print("Computer Hand",computer_cards)
    computer_hand.append(computer_cards)
computer_cards.in_use = True