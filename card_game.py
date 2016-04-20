from __future__ import division
import random

card_map = {
        "A": {
            "card": "Ace of Spades",
            "value": 0
            },
        "B": {
            "card": "King of Spades",
            "value": 1
            },
        "C": {
            "card": "Queen of Spades",
            "value": 2
            },
        "D": {
            "card": "Jack of Spades",
            "value": 3
            },
        "E": {
            "card": "10 of Spades",
            "value": 4
            },
        "F": {
            "card": "9 of Spades",
            "value": 5
            },
        "G": {
            "card": "8 of Spades",
            "value": 6
            },
        "H": {
            "card": "7 of Spades",
            "value": 7
            },
        "I": {
            "card": "6 of Spades",
            "value": 8
            },
        "J": {
            "card": "5 of Spades",
            "value": 9
            },
        "K": {
            "card": "4 of Spades",
            "value": 10
            },
        "L": {
            "card": "3 of Spades",
            "value": 11
            },
        "M": {
            "card": "Deuce of Spades",
            "value": 12
            }
        }

cards = card_map.keys()

class Game:

    def __init__(self, max_attempts=10, card_map=card_map):
        self.max_attempts = max_attempts
        self.card_map = card_map

    def play(self, cards=cards):
        "Run game once"
        self.arrangement = cards
        for player_id, letter in enumerate(self.arrangement):
            successful = False
            attempts = 0
            while not successful:
                current_card = self.card_map[letter]
                if player_id == current_card["value"]:
                    successful = True
                letter = self.arrangement[current_card["value"]]
                attempts += 1
                if attempts > self.max_attempts:
                    return "Game over. Failed."
        return "Success"

G = Game()

# Test strategy
rounds = 50000
win_rate = 0
for i in range(rounds):
    random.shuffle(cards) # important!
    if G.play(cards) == "Success":
        win_rate += 1/rounds
win_rate = round(win_rate * 100, 1)
print "The strategy won {}% of {} rounds.".format(win_rate, rounds)
