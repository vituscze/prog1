def createHistogram(str):
    hist = {}
    for s in str:
        if s in hist:
            hist[s] += 1
        else:
            hist[s] = 1
    return hist

def printHistogram(histo, n = 10):
    max = 0
    for v in histo.values():
        if v > max:
            max = v
    for k, v in histo.items():
        stars = n * v // max
        print(k + ':', '*' * stars)

def fac(n):
    if n <= 0:
        return 1
    else:
        return n * fac(n - 1)

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

mem = {}
def fibMem(n):
    if n in mem:
        return mem[n]

    r = None
    if n <= 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        r = fibMem(n - 1) + fibMem(n - 2)

    mem[n] = r
    return r

def binarySearch(what, l, begin, end):
    if begin >= end:
        return None
    elif end - begin == 1:
        if l[begin] == what:
            return begin
        else:
            return None
    else:
        mid = begin + (end - begin) // 2
        if l[mid] < what:
            return binarySearch(what, l, mid + 1, end)
        elif l[mid] == what:
            return mid
        else:
            return binarySearch(what, l, begin, mid)
