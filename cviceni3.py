### Cvičení z Algoritmizace ###

# Bonusové body za účast

# Nová úloha na ReCodExu

## Síto bez sudých čísel ##

# Pro připomenutí:

n = int(input())
is_prime = [True] * (n + 1)
for p in range(2, n + 1):
    if is_prime[p]: # Našli jsme prvočíslo
        for k in range(2 * p, n + 1, p): # stačí od p*p
            is_prime[k] = False

for i in range(2, n + 1):
    if is_prime[i]:
        print(i, end=' ')
print()

# Časová složitost? Z přednášky víme, že síto je O(n log log n), důkaz ale není
# jednoduchý (potřebujeme znát hustotu prvočísel, což si ukazovat nebudeme).
# Můžeme ale jednoduše ukázat slabší trvzení: O(n log n)

# n = int(input())                          # 2 operace
# is_prime = [True] * (n + 1)               # n + 1 operací
# for p in range(2, n + 1):
#     if is_prime[p]:                       # \
#         for k in range(2 * p, n + 1, p):  #  - proběhne (n - 1)-krát
#             is_prime[k] = False           # /

# Kolik operací potřebujeme pro vnitřní cyklus (v závislosti na n a p)?

# for k in range(2 * p, n + 1, p):
#     is_prime[k] = False           # <= n/p operací
#
# Tenhle vnitřní cyklus se ale pustí jen pro prvočísla! Takže dostaneme něco jako
# n/2 + n/3 + 1 + 1 + n/5 + 1 + n/7 + ...
#
# (Tohle pak dá přesně to n log log n). Můžeme si tento odhad ale trochu jednodušit:
#
# n/2 + n/3 + 1 + 1 + n/5 + 1 + n/7 + ... <= n/2 + n/3 + n/4 + n/5 + n/6 + n/7 + n/8 + n/9 ...
#                                         <= (n/2 + n/3) + (n/4 + n/5 + n/6 + n/7) + (n/8 + ...) + ...
#                                         <= (n/2 + n/2) + (n/4 + n/4 + n/4 + n/4) + (n/8 + ...) + ...
#                                         <= n + n + n + n + ...

# Kolik těch n v tomto součtu bude? Přibližně log n (protože v každém dalším kroku bereme 2x tolik zlomků).
# A tedy celkový čas je n log n + n \in O(n log n)

# Jak ze síta vyhodit sudá čísla?
n = int(input())
# Místo pole, co bude mít informaci o čísle 0, 1, 2, 3, ...
# budeme mít pouze informaci o 3, 5, 7, 9, 11, ...

# Nejdřív potřebujeme způsob, jak převést číslo na index
def to_index(n):
    return (n - 3) // 2

# Původní pole šlo od 0..n, nové pole půjde od 0..to_index(n)
is_prime = [True] * (to_index(n) + 1)
for p in range(3, n + 1, 2): # Vynecháme sudá čísla
    if p * p > n: # Fígl: od sqrt(n) už je range(p*p, ...) vždy prázdný; šlo by taky upravit první for cyklus
        break
    if is_prime[to_index(p)]: # Číslo -> index
        for k in range(p * p, n + 1, 2 * p): # p*p je liché, p*p + p je sudé, tj. můžeme vynechat
            is_prime[to_index(k)] = False

print(2, end=' ')
for i in range(3, n + 1, 2):
    if is_prime[to_index(i)]:
        print(i, end=' ')
print()


### Cvičení z Programování I ###

# Nová úloha na ReCodExu

# Seznamy:
a = [1, 2, 3]
b = []

# V Pythonu nemusí být seznam homogenní, ale je to dobrý zvyk (v C# to pak možné nebude)
a = [1, True, 'hello']

# Přístup na prvek
print(a[0])
print(a[-1]) # Od konce

# Slice.
u = 'understandable'
print(u[5:10]) # funguje podobně jako range: včetně počátku a kromě konce
print(u[:10]) # jedna hodnota může chybět, pak se to chová jako by to bylo 0 resp. len(u) - 1
print(u[:]) # ???
print(u[5:10:-1]) # ???
print(u[10:5:-1]) # Záporný krok potřebuje obrácený začátek a konec
print(u[::-1])

# u[0] = 'a' # string nepodporuje modifikaci
a[0] = 'test' # seznam OK

# Pozor: tohle je dvousečná zbraň
a = [1, 2, 3]
b = a
b[0] = 10
print(a) # ???

# Přiřazení nevytváří kopii!
# Jak zjistit, jestli jsou dva seznamy identické?
print(a == b) # pouze porovná prvky
print(a is b) # True pouze pokud a a b ukazují na ten samý seznam

# Další operace:
a.append(4) # O(1), amortizovaně (bude později)
a += [5] # O(m) kde m je počet prvků druhého seznamu
a += range(6, 10) # lze použít i na jiné sekvence
a = a + [11] # pozor! vytvoří kopii, O(m + n) kde m, n jsou délky každého seznamu

# Jaké další operace vytvářejí kopii?
b = a.copy()
b = list(a)
b = a[:]

b = list(range(5, 10)) # Může být užitečné

# Co udělá tohle?
m = [[1,2]] * 5
m[0][0] = 10
print(m) # ???
print(m[0] is m[1])

# Funkce!
# Často potřebujeme na více místech dělat tu samou věc. Psát pokaždé ten samý kód má několik nevýhod:
# a) je to otravné
# b) je to nepřehledné
# c) pokud je v kódu chyba, musí se opravit na více místech (snadno se pak zapomene to někde opravit)

def hello():
    print('hello')

# Fce může být parametrizovaná; píše se do kulatých závorek
def greet(name):
    print(f'hello {name}!')

# Parametrů může být i více; mohou mít defaultní hodnoty, proměnlivý počet, atp. (bude někdy příště)
def greet2(name='world'):
    print(f'hello {name}!')

greet2()
greet2('test')

# Pokud ve fci není return, tak implicitně vrací speciální hodnotu None
is_none = greet2() == None
print(is_none)

def sqr(n):
    return n * n

# Proměnné
a = 'test'
def f1():
    print(a) # OK, použije a mimo fci

def f2():
    a = 'test2'
    print(a) # Vytiskne test2
f2()
print(a) # Pozor!

# Pokud do proměnné *přiřazujeme* uvnitř fce, Python pro nás automaticky vytvoří lokální
# proměnnou, která s tou vnější nemá nic společného
# Pokud je to skutečně zapotřebí, dá se použít klíčové slovo global -- to je ale v 99% případů
# špatný nápad, takže se tomu pokuste vyvarovat

def f3():
    global a
    a = 'test2'
f3()
print(a)

c = [1,2,3]
def f4():
    c[0] = 10 # Proměnná se zde nemění: pořád ukazuje na ten samý senzam, proto je tohle OK
              # mění se ale obsah seznamu, což Python nekontroluje!
f4()
print(c)

# Často jsou fce dlouhé a není jednoduché zjistit, co přesně který parametr dělá a jaká bude návratová
# hodnota. Potom se hodí na začátek fce přidat tzv. *docstring*, který vysvětluje, co fce dělá

def factorial(n):
    '''
    Computes the factorial of n.

    factorial(n) = n * (n - 1) * (n - 1) * ... * 3 * 2 * 1
    '''
    pass

# Integrace s help(...)!

# Zkuste si doprogramovat factorial a následující fce.

def palindrome(word):
    '''
    Určí, jestli je vstupní slovo word palindrom. Palindrom je slovo,
    které stejně zleva doprava i zprava doleva.

    >>> palindrome('radar')
    True
    >>> palindrome('(())')
    False
    '''
    # Prázdný string je triviálně palindrom. Zvládnete to udělat
    # pomocí len(word)/2 operací?
    pass

def ascending(seq):
    '''
    Určí, zda-li je vstupní posloupnost (neostře) rostoucí.

    >>> ascending([1,2,3])
    True
    >>> ascending([1,1,1])
    True
    >>> ascending([3,2,1])
    False
    '''
    pass

def lottery(start, end, count):
    '''
    Vybere count náhodných čísel z rozsahu [start, end) *bez opakování.* Čísla vrátí jako seznam.

    >>> lottery(1, 7, 3)
    [6, 1, 3]
    '''
    # Můžete předpokládat, že rozsah má více než count možností.
    pass

def contains(haystack, needle):
    '''
    Spočítá, jestli je string needle někde uvnitř stringu haystack.

    >>> contains('hello there', 'th')
    True
    '''
    # Nepoužívejte operátor in, který dělá to samé.
    pass

def histogram(text):
    '''
    Spočítá počet výskytů každého ASCII písmena ve vstupním textu. Výsledek
    vrátí jako seznam čísel délky 26. Nerozlišuje velká a malá písemena.

    >>> histogram('aaabc')
    [3, 1, 1, 0, ..., 0, 0]
    '''
    # Mohou se hodit fce ord a char.
    pass

def fibonacci(n):
    '''
    Spočítá n-té Fibonacciho číslo. fibonacci(0) = 0, fibonacci(1) = 1, každé
    další je pak součet dvou předchozích.

    >>> fibonacci(5)
    5
    '''
    pass
