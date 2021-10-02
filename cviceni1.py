# Algoritmizace: Vážení N kuliček
# * Nalezení nejtěžší kuličky pomocí N - 1 zvážení (formální důkaz správnosti a optimality)
# * Nalezení nejtěžší a nejlehčí kuličky pomocí 3/2 N - 2 zvážení
# * Nalezení dvou nejtěžších kuliček pomocí N + log N - 2 zvážení (turnajový postup)
# * Nalezení jedné odlišné kuličky pomocí log N zvážení

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
