import random

target = random.randint(1, 10)
available_guesses = 3
guess_left = available_guesses

while guess_left > 0:
    guess = random.randint(1, 10)
    guess_left -= 1
    if guess == target:
        print("you won 10 points!")
        break
    elif abs(guess - target) <= 2:
        print("your are almost close")
    else:
        print("your are too far away")
        

    