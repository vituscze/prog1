### Cvičení z Algoritmizace ###

# Bonusové body za účast

## Síto bez sudých čísel ##

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


##############################
### Nová úloha na ReCodExu ###
##############################

## Jak určit počet výskytů pomocí binárního výhledávání?

def binSearch(a, x):
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x: # druha pulka
            start = mid + 1
        else:
            end = mid - 1
    return None

# Tato fce najde *nějaký* výskyt x. Co kdybychom chtěli první?
# S hledáním můžeme pokračovat: pokud jsou hodnoty stejné,
# jdeme dále vlevo dokud nenajdeme místo, ve kterém výskyty
# hledané hodnoty končí.

def lowerBound(a, x):
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

def upperBound(a, x):
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return start

def binSearchRange(a, x):
    i, j = lowerBound(a, x), upperBound(a, x)
    return (i, j) if i != j else None

### Cvičení z Programování I ###

# Nová úloha na ReCodExu

# Jak posunout prvky seznamu?

def shift(x, n):
    result = []
    for i in range(len(x)):
        result.append(x[(i + n) % len(x)]) # Tohle budeme používat často!
    return result

# Čas O(n), paměť O(n). Co pokud chceme změnu provést "in-place",
# tj. destruktivně upravit původní seznam?

# Posun o jeden prvek je celkem jednoduchý.
def shiftInPlace(x):
    if len(x) <= 1: # Nejprve vyřešíme triviální případy
        return

    first = x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1]
    x[-1] = first

# Co pokud chceme posun o více prvků?

def revRange(x, begin, end):
    '''
    Otočí prvky seznamu x v rozsahu [begin, end)
    '''
    for i in range((end - begin) // 2):
        x[begin + i], x[end - i - 1] = x[end - i - 1], x[begin + i]

def shiftInPlaceClever(x, n):
    if len(x) <= 1:
        return

    mid = -n % len(x) # V Pythonu vždy nezáporné číslo
    revRange(x, 0, len(x))
    revRange(x, 0, mid)
    revRange(x, mid, len(x))

# Minule jsme si říkali, proč jsou funkce užitečné. Když píšete funkci, je dobré
# mít na mysli pár věcí:
#
# a) Funkci vhodně pojmenujte; ze jména maximum_index je hned patrné, co fce dělá, ze jména
#    fff nikoliv.
# b) Funkce by se vždy měla soustředit na jeden problém; neřeště více věcí v jedné funkci
#    najedou. Není problém kód rozdělit na více fcí. Typický příklad: funkce co něco spočítá a
#    zároveň to vytiskne.

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    print(r)

# Tohle sice funguje, ale...

def comb(n, k):
    '''
    C(n, k) = n!/(k! * (n - k)!)
    '''
    pass # Tady už faktoriál použít nelze

# c) Použijte rozumná jména pro parametry a lokální proměnné. U parametrů je to docela
#    kritické, protože jsou v Pythonu součástí rozhraní fce.

def power(blabla, bleble):
    r = 1
    while bleble > 0:
        if bleble % 2 == 1:
            r *= blabla
        bleble //= 2
        blabla = blabla * blabla
    return r

print(power(bleble=10, blabla=2)) # ???
# print(power(exp=10, base=2))

# d) Většinu funkcí je také vhodné opatřit docstringem, speciálně pokud to nejsou
#    nějaké interní fce.
# e) Funkce by měla být obecná. Pokud potřebujete na dvou místech kódu spočítat faktoriál
#    čísel mezi 5 a 10, můžete si sice napsat fci, která to umí spočítat JEN pro čísla 5-10,
#    ale pokud pak zjistíte, že to potřebujete i pro 11, musíte se vracet a kód opravovat.
#    Faktoriál je zrovna pěkný příklad, protože jde triviálně spočítat pro nulu, což studenti
#    často vynechají (funguje předešlá definice pro nulu?).

# Když píšete kód a vaše funkce vám začnout "bobtnat", je dobré se na chvilku zastavit
# a rozmyslet si, jestli by nebylo vhodné kód přepsat tak, aby lépe odpovídal výše uvedeným
# bodům. Tomuto procesu se říká "refactoring". Zkuste si to na pár příkladech:

# Určete, co tenhle kód dělá a potom proveďte refactoring. Rozdělete to na funkce, které dělají
# jen jednu věc, funkce a proměnné vhodně přejmenujte, přidejte (jednoduchý) docstring. Funkci
# také zobecněte; není zapotřebí se omezovat na seznamy fixní délky.

def pp(x, y):
    z = [0, 0, 0, 0]
    z[0] = x[0] + y[0]
    z[1] = x[1] + y[1]
    z[2] = x[2] + y[2]
    z[3] = x[3] + y[3]

    w = x[0] * y[0] + x[1] * y[1] + x[2] * y[2] + x[3] * y[3]

    v = True
    if x[0] <= y[0]: v = False
    if x[1] <= y[1]: v = False
    if x[2] <= y[2]: v = False
    if x[3] <= y[3]: v = False

    return [z, w, v]


x = [3, 7, 2, 9]
y = [1, 4, 2, 5]
r = pp(x, y)

print(f"Prvni hodnota: {r[0]}")
print(f"Druha hodnota: {r[1]}")
print(f"Treti hodnota: {r[2]}")

# Druhý příklad:

def q(n):
    a = n // 1000
    b = n // 100 % 10
    c = n // 10 % 10
    d = n % 10

    print(f"Prvni hodnota: {a + b + c + d}")

    k = 4
    if a == 0: k = 3
    if a == 0 and b == 0: k = 2
    if a == 0 and b == 0 and c == 0: k = 1
    print(f"Druha hodnota: {k}")

    r = d * 1000 + c * 100 + b * 10 + a
    print(f"Treti hodnota: {r}")


q(4728)

# Pokud stihneme: co dělá tenhle kód? Jaký bude výsledek?

def bar(a):
    for i in range(len(a)):
        a[i] += 1
        a = a[:]

def foo(a):
    for b in a + a[:]:
        bar(b)
        bar(b[:])

m = [[1, 2], [3, 4]]
foo(m)
print(m)
