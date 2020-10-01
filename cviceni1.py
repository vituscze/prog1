import random

rnd = random.randint(1, 100)

while True:
    guess = int(input('Enter a guess: '))
    if guess < rnd:
        print('Too low, try again.')
    elif guess > rnd:
        print('Too high, try again.')
    else:
        print('You got it!')
        break
