# Comp generates a random number and you have to guess what it is

import random

secret_number = int(random.random() * 100)
for x in range(10):
    guess = int(input(f"Guess {x+1} of 10: "))
    if guess == secret_number:
        print("You win you guessed correctly")
        break
    elif guess > secret_number:
        print("Your Guess was too large")
    else:
        print("Your guess what to small ")
