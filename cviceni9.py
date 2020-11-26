def parens(opening, closing, string):
    if opening <= 0 and closing <= 0:
        print(string)
    else:
        if opening > 0:
            parens(opening - 1, closing + 1, string + '(')
        if closing > 0:
            parens(opening, closing - 1, string + ')')

def parensList(opening, closing, string, results):
    if opening <= 0 and closing <= 0:
        results.append(string)
    else:
        if opening > 0:
            parensList(opening - 1, closing + 1, string + '(', results)
        if closing > 0:
            parensList(opening, closing - 1, string + ')', results)

def hanoi(n, start, end, via):
    if n == 1:
        print('Move', start, 'to', end)
    else:
        hanoi(n - 1, start, via, end)
        print('Move', start, 'to', end)
        hanoi(n - 1, via, end, start)

def pay(amount, coins, solution):
    if amount == 0:
        print(*solution)
    else:
        for c in coins:
            if c <= amount:
                pay(amount - c, coins, solution + [c])

def payUnique(amount, coins, solution):
    if amount == 0:
        print(*solution)
    else:
        for i, c in enumerate(coins):
            if c <= amount:
                payUnique(amount - c, coins[i:], solution + [c])

def permutation(items, result):
    if len(items) == 0:
        print(*result)
    else:
        for i, v in enumerate(items):
            newItems = items.copy()
            del newItems[i]
            permutation(newItems, result + [v])

def permutationsInPlace(items, rem, result):
    if rem == 0:
        print(*result)
    else:
        for ix in range(len(items)):
            if result[ix] != None:
                continue

            result[ix] = items[-rem]
            permutationsInPlace(items, rem - 1, result)
            result[ix] = None

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def printTree(root):
    def go(node, depth):
        if node == None:
            return

        go(node.left, depth + 1)
        print(' ' * 2 * depth + str(node.value))
        go(node.right, depth + 1)

    go(root, 0)
