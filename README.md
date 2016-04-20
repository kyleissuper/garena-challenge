## How do we maximize our winning strategy?

Our solution to Garena's challenge at the National University of Singapore School of Computing's 8th Term Project Showcase. We've summarized the challenge in our own words:

There are 13 players in a game, named in order from A to M. Their names are written on playing cards, from the Ace of Spades to the Deuce of Spades, shuffled, and placed, face down, in a line in a separate room. One at a time, they go in, flip over up to 10 cards, and must see their own name. If any one of them fails, the game ends.

There is no way to exchange information after the game has begun. How can they agree on a strategy to win the game as often as possible?

## Our solution

Basically, our strategy is for each player to begin on the card that _would_ be theirs, if the cards were not shuffled. If the card is not theirs, they go to the card in the position of the person whose name is written on the current card.

## Explanation

The Python script here runs the game for 50,000 rounds. I've found that the probability usually ends up being around 75%.

It turns out that the objective probability of the strategy winning is 1 - (1/11 + 1/12 + 1/13) = 0.74883. We wrote a more detailed explanation in our officially submitted solution, but, in hindsight, it seems that the theory is well-documented, and is called "permutation circles".
