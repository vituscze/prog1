def isSortedAsc(x):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            return False
    return True

def isSortedDesc(x):
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            return False
    return True

def isSortedBoth(x):
    asc, desc = True, True
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            desc = False
        elif x[i] > x[i + 1]:
            asc = False
    return asc, desc

def isSorted(x):
    asc, desc = isSortedBoth(x)
    return asc or desc

def revRange(l, begin, end):
    for i in range((end - begin) // 2):
        l[begin + i], l[end - i - 1] = l[end - i - 1], l[begin + i]

def shift(x, n):
    r = []
    for i in range(len(x)):
        r.append(x[(i + n) % len(x)])
    return r

def shiftInplace(x):
    if len(x) <= 1:
        return

    tmp = x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1]
    x[-1] = tmp

def shiftClever(l, n):
    if len(l) <= 1:
        return

    mid = -n % len(l)
    revRange(l, 0, len(l))
    revRange(l, 0, mid)
    revRange(l, mid, len(l))
