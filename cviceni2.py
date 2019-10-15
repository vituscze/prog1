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

def palindrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True
