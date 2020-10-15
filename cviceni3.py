def sieve(n):
    if n < 2:
        return []

    size = (n - 3) // 2 + 1
    candidates = size * [True]
    result = [2]
    for i in range(size):
        if candidates[i]:
            prime = 3 + 2 * i
            # print('### prime', prime)
            start = (prime * prime - 3) // 2
            result.append(prime)
            for j in range(start, size, 2 * prime // 2):
                # print('crossing out', 3 + 2 * j)
                candidates[j] = False
    return result

# ----------

def getInput(r):
    r = min(3, r)
    while True:
        i = int(input('Enter a number between 1 and ' + str(r) + ': '))
        if i >= 1 and i <= r:
            return i

def nextPlayer(p):
    if p == 'A':
        return 'B'
    else:
        return 'A'

def printGameState(p, r):
    print('---')
    print('Player ', p, "'s turn", sep='')
    print(r, 'remaining coins')

rem = 15
player = 'A'

while rem > 0:
    printGameState(player, rem)
    rem -= getInput(rem)
    if rem == 0:
        print('Player', player, 'won!')
    else:
        player = nextPlayer(player)

# ----------

def palindrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True
