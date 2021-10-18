# faktorial
# n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
# 0! = 1
def faktorial(n):
    soucin = 1
    for i in range(1, n + 1):
        soucin *= i
    return soucin

# fibonacci
# 0 1 1 2 3 5 8...
# fib(5) = 5
# fib(0) = 0
# fib(1) = 1
def fib(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a

# rostouci podle <=
# ascending([1,2,3]) == True
# ascending([1,1,1]) == True
# ascending([3,2,1]) == False
def ascending(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def descending(s):
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            return False
    return True

# setrideny
# ordered(...)
def ordered(a):
    return ascending(a) or descending(a)

# palindrom
# palindrom('radar') == True
# palindrom('(())') == False
def palindrom(s):
    return s == s[::-1]

def betterPalindrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True


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
