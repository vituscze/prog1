# Algoritmizace:
# * příklady na notaci O, Omega a Theta
# * důkaz časové složitosti síta O(n log n)

# Přečti řádku od uživatele, rozděl ji na slova (oddělená mezerami) a každé slovo transformuj na číslo
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
