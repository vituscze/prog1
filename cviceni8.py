def generate(toOpen, toClose=0, str=''):
    if toOpen == 0 and toClose == 0:
        print(str)
    if toOpen > 0:
        generate(toOpen - 1, toClose + 1, str + '(')
    if toClose > 0:
        generate(toOpen, toClose - 1, str + ')')

def generateReturn(toOpen, toClose=0, str=''):
    if toOpen == 0 and toClose == 0:
        return [str]
    r = []
    if toOpen > 0:
        r += generateReturn(toOpen - 1, toClose + 1, str + '(')
    if toClose > 0:
        r += generateReturn(toOpen, toClose - 1, str + ')')
    return r

def generateParam(result, toOpen, toClose=0, str=''):
    if toOpen == 0 and toClose == 0:
        result.append(str)
    if toOpen > 0:
        generateParam(result, toOpen - 1, toClose + 1, str + '(')
    if toClose > 0:
        generateParam(result, toOpen, toClose - 1, str + ')')

def hanoi(n, start, end, via):
    if n > 0:
        hanoi(n - 1, start, via, end)
        print('Move', start, 'to', end)
        hanoi(n - 1, via, end, start)

def pay(amount, coins, solution=[]):
    if amount == 0:
        print(*solution)
    else:
        for c in coins:
            if c <= amount:
                pay(amount - c, coins, solution + [c])

def payUnique(amount, coins, solution=[]):
    if amount == 0:
        print(*solution)
    else:
        for i, c in enumerate(coins):
            if c <= amount:
                payUnique(amount - c, coins[i:], solution + [c])

def powerset(list, set=[]):
    if len(list) == 0:
        print(*set)
    else:
        head, *tail = list
        powerset(tail, set)
        powerset(tail, set + [head])

def powersetNonrecursive(list):
    for i in range(1 << len(list)):
        for j in range(len(list)):
            if (i >> j) & 1 != 0:
                print(list[j], end=' ')
        print()

def permutations(items, result=[]):
    if len(items) == 0:
        print(*result)
    else:
        for i, v in enumerate(items):
            newItems = items[:i] + items[i + 1:]
            permutations(newItems, result + [v])

def permutationsInPlace(items, start=0, result=None):
    if result == None:
        result = [None] * len(items)
    if start == len(items):
        print(*result)
    else:
        for ix in range(len(result)):
            if result[ix] != None:
                continue

            result[ix] = items[start]
            permutationsInPlace(items, start + 1, result)
            result[ix] = None
