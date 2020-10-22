def shift(x, n):
    result = []
    for i in range(len(x)):
        result.append(x[(i + n) % len(x)])
    return result

def shiftInPlace(x):
    if len(x) <= 1:
        return

    tmp = x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1]
    x[-1] = tmp

def gcd(a, b):
    while b > 0:
        a, b = b , a % b
    return a

def shiftInPlaceComplex(x, n):
    if len(x) <= 1:
        return

    length = len(x)
    n = n % length

    cycleCount = gcd(length, n)
    cycleLength = length // cycleCount

    for i in range(cycleCount):
        tmp = x[i]
        ix = i
        for j in range(cycleLength - 1):
            x[ix % length] = x[(ix + n) % length]
            ix += n
        x[ix % length] = tmp

def revRange(x, begin, end):
    for i in range((end - begin) // 2):
        x[begin + i], x[end - i - 1] = x[end - i - 1], x[begin + i]

def shiftInPlaceClever(x, n):
    if len(x) <= 1:
        return

    mid = -n % len(x)
    revRange(x, 0, len(x))
    revRange(x, 0, mid)
    revRange(x, mid, len(x))
