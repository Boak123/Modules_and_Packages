import random

Guess = random.randint(1, 100)
print(f"Random guess: {Guess}")

cards = ['jack', 'queen', 'king', 'ace']
random.shuffle(cards)
for card in cards:
    print(card)