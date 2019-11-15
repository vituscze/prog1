# hanoi(4, 'left', 'middle', 'right')
def hanoi(n, start, end, via):
    if n == 1:
        print('Move', start, 'to', end)
    else:
        hanoi(n - 1, start, via, end)
        print('Move', start, 'to', end)
        hanoi(n - 1, via, end, start)

# a = []
# generate(3, 10, a)
def generate(n, k, finalList, res = 0, first = True):
    if n == 1:
        for i in range(k):
            finalList.append(res + i)
    else:
        for i in range(k):
            if first and i == 0:
                continue
            # Korekce kódu ze cvičení: k**(n - 1) místo 10**(n - 1)
            # např. pro hexadecimální soustavu a dvě číslice korektně dává
            # čísla od 10(hex)/16(dec) do ff(hex)/255(dec)
            generate(n - 1, k, finalList, res + i * k**(n - 1), False)

# pay(10, [])
def pay(rem, solution, max = 5):
    if rem == 0:
        print(solution)
    else:
        for i in [5,2,1]:
            if rem >= i and i <= max:
                pay(rem - i, solution + [i], i)

# permutation([1,2,3], [])
def permutation(input, cur):
    if len(input) == 0:
        print(cur)
    else:
        for i, v in enumerate(input):
            newInput = list(input)
            del newInput[i]
            permutation(newInput, cur + [v])
