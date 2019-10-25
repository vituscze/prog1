def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def shiftInplace(l, n):
    if len(l) <= 1:
        return

    length = len(l)
    n = n % length

    cycleCount = gcd(length, n)
    cycleLength = length // cycleCount

    for i in range(cycleCount):
        tmp = l[i]
        ix = i
        for j in range(cycleLength - 1):
            l[ix % length] = l[(ix + n) % length]
            ix += n
        l[ix % length] = tmp

def split(str):
    res = []
    cur = ''
    for x in str + ' ':
        if x == ' ':
            if cur != '':
                res.append(cur)
                cur = ''
        else:
            cur = cur + x
    return res

def readRow():
    res = []
    s = split(input())
    for x in s:
        res.append(int(x))
    return res

def readMatrix():
    res = []
    rows = int(input())
    for i in range(rows):
        res.append(loadRow())
    return res

def isSymmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
