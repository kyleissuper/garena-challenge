from __future__ import division
import random

card_map = {
        "A": {
            "card": "Ace of Spades",
            "id": 0
            },
        "B": {
            "card": "King of Spades",
            "id": 1
            },
        "C": {
            "card": "Queen of Spades",
            "id": 2
            },
        "D": {
            "card": "Jack of Spades",
            "id": 3
            },
        "E": {
            "card": "10 of Spades",
            "id": 4
            },
        "F": {
            "card": "9 of Spades",
            "id": 5
            },
        "G": {
            "card": "8 of Spades",
            "id": 6
            },
        "H": {
            "card": "7 of Spades",
            "id": 7
            },
        "I": {
            "card": "6 of Spades",
            "id": 8
            },
        "J": {
            "card": "5 of Spades",
            "id": 9
            },
        "K": {
            "card": "4 of Spades",
            "id": 10
            },
        "L": {
            "card": "3 of Spades",
            "id": 11
            },
        "M": {
            "card": "Deuce of Spades",
            "id": 12
            }
        }

cards = card_map.keys()

class Game:

    def __init__(self, max_attempts=10, card_map=card_map):
        self.max_attempts = max_attempts
        self.card_map = card_map

    def play(self, cards=cards):
        for player_id, letter in enumerate(cards):
            successful = False
            attempts = 0
            while not successful:
                current_card = self.card_map[letter]
                if player_id == current_card["id"]:
                    successful = True
                letter = cards[current_card["id"]]
                attempts += 1
                if attempts > self.max_attempts:
                    return "Game over. Failed."
        return "Success!"

G = Game()

# Test strategy
rounds = 50000
win_rate = 0
for i in range(rounds):
    random.shuffle(cards) # important!
    if G.play(cards) == "Success!":
        win_rate += 1/rounds
win_rate = round(win_rate * 100, 1)
print "The strategy won {}% of {} rounds.".format(win_rate, rounds)
