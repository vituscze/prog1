x = [int(r) for r in input().split()]
y = int(input())

low = 0
high = len(x)
found = False
while not found and high > low:
    mid = low + (high - low) // 2
    if y > x[mid]:
        low = mid + 1
    elif y < x[mid]:
        high = mid
    else:
        found = True

if found:
    print('Found!')
else:
    print('Too bad')

# ----------

x = [int(r) for r in input().split()]

if len(x) % 2 == 1:
    x.append(x[-1])

if len(x) > 0:
    for i in range(0, len(x), 2):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]
    maybeMin = x[0]
    maybeMax = x[1]
    for i in range(2, len(x), 2):
        if x[i] < maybeMin:
            maybeMin = x[i]
        if x[i + 1] > maybeMax:
            maybeMax = x[i + 1]
    print('min', maybeMin)
    print('max', maybeMax)

# ----------

def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        a, b = 1, 0
        for i in range(n - 1):
            a, b = a + b, a
        return a
