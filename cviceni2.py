### Cvičení z Algoritmizace ###

# Bonusové body za účast

# Nová úloha na ReCodExu

## Problém stabilním párování ##

# Pro připomenutí, algoritmus GS dostane jako vstup N můžu a N žen,
# a pro každého seznam preferencí (N žen resp. mužů). Úkolem je najít
# *stabilní* párování mužů a žen. Párování je stabilní, pokud neexistují
# dvojice (m1, z1) a (m2, z2) kde m1 preferuje z2 (vs z1) a z2 preferuje
# m1 (vs m2) (pak by párování šlo "vylepšit" použitím dvojice (m1, z2)).

# Algoritmus funguje takto:
#
# dokud existuje nespárovaný muž m:
#   z = první nevyškrnutá žena na seznamu m
#   pokud z není v párování:
#     přidej pár (m, z)
#   jinak:
#     (m', z) = stávající párování pro z
#     pokud m' > m:  (žena preferuje stávajícího partnera)
#       odstraň z ze seznamu m
#     jinak:  (žena preferuje nového partnera)
#       odeber pár (m', z)
#       přidej pár (m, z)
#       odstraň z ze seznamu m'

# Je GS párování nejlepší možné pro muže?
#
# Pomocná definice: z je stabilní partnerkou m pokud (m, z) je v *nějakém*
# stabilním párování.
#
# Pro důkaz sporem předpokládejme, že GS párování není nejlepší pro muže.
# V nějakém kroku musel být nějaký muž odmítnut nějakou svou stabilní partnerkou
# (jinak by párování bylo nejlepší).
#
# Podívejme se na první případ, kdy se tak stane. Žena z odmítne muže m ve prospěch
# m'. Jelikož z je stabilní partnerkou m, musí existovat nějaké jiné stabilní párování, kde
# jsou dvojice (m, z) a (m', z') (pro nějakou ženu z'). Co můžeme říct o preferencích z a m'?
#
# Zjevně m' > m pro ženu z (jinak by muže m neodmítla). Žena může odmítnout muže ve dvou případech:
#
# a) (m, z) jsou spárovaní a muž m' vybírá partnerku. m' nemohl být ještě odmítnut nějakou stabilní
#    partnerkou (z předpokladu zatím k jinému odmítnutí nedošlo) a pokud si tedy vybral ženu z,
#    tak nutně z > z'.
#
# b) (m', z) jsou spárovaní a muž m vybírá partnerku. To nám sice moc o prefereních m' neřekne, ale
#    je dobré si uvědomit, že dvojice (m', z) se do párování musela v nějakém předchozím kroce dostat.
#    V tu chvíli si muž m' vybíral partnerku a, podobně jako v předchozím případě, vybral ženu z.
#
# Jinými slovy, jelikož je po tomto kroce dvojice (m', z) v párování a m' nemohl být odmítnut žádnou
# svou stabilní partnerkou (m je první muž odmítnutý stabilní partnerkou), musí nutně preferovat z
# místo z'.
#
# To je ale spor s tím, že (m, z) a (m', z') jsou součástí stabilního párování!

# Je GS párování nejhorší možné pro ženy?
#
# Pro důkaz sporem předpokládejme, že dvojice (m, z) není nejhorší možné párování pro ženu z. Musí
# tedy existovat jiné stabilní párování, které obsahuje dvojice (m', z) a (m, z') kde m > m' pro ženu z.
#
# Podle předchozího výsledku víme, že z je nejlepší možná partnerka pro m. Tj. z > z' pro muže m.
# To je ale triviálně spor s tím, že je (m', z) a (m, z') stabilní párování -- lze jednoduše vylepšit
# dvojicí (m, z).

## Asymptotická notace ##

# Připomenutí:
#
# f \in O(g(n)) <=>
#  existuje c > 0, n_0 > 0 tak, že pro každé n >= n_0 platí 0 <= f(n) <= c * g(n)
#
# f \in Omega(g(n)) <=>
#  existuje c > 0, n_0 > 0 tak, že pro každé n >= n_0 platí 0 <= c * g(n) <= f(n)
#
# f \in Theta(g(n)) <=> f \in O(g(n)) & f \in Omega(g(n))

# Dokažte nebo vyvraťte: pro f, g : N -> R
#
# a) pokud f(n) \in O(g(n)) pak g(n) \in Omega(f(n))
#
# Máme c, n_0 tž. 0 <= f(n) <= c * g(n) pro n >= n_0
#
# Potřebujeme najít c', n_0' tž. 0 <= c' * f(n') <= g(n') pro n' >= n_0'
#
# Zvolme c' = 1/c, n_0' = n_0, potom:
#
#   0 <= c' * f(n') <= g(n')
#   0 <= 1/c * f(n') <= g(n')  // * c [kladné]
#   0 <= f(n') <= c * g(n')
#
# b) pokud f(n) \in O(g(n)) pak 2^f(n) \in O(2^g(n))
#
# f(n) = 100n, g(n) = n, zjevně 100n \in O(n)
#
# 2^100n \notin O(2^n)? Předpokládejme, že dostaneme konstanty c, n_0. Naším
# úkolem je najít n takové, že 2^100n > c * 2^n.
#
# c * 2^n = 2^log c * 2^n = 2^(log c + n) < 2^100n
#
# Stačí zvolit např. n = max(n_0 + 1, log c)
#
# c) f(n) \in O(g(n)) nebo g(n) \in O(f(n))
#
# f(n) = 1 pokud n sudé, jinak 0
# g(n) = 1 pokud n liché, jinak 0
#
# f(n) nemůže být v O(g(n)) - nehledě na to, jak velkou konstantu c vezmeme,
# c * g(n) bude vždy nula pro sudá čísla (a f(n) bude 1). Stejný argument lze
# aplikovat pro opačný případ a lichá čísla.
#
# d) f(n) \in O(f(n)^2)
#
# f(n) = 1/n, 1/n \notin O(1/n^2)? Předpokládejme, že dostaneme konstanty c, n_0. Naším
# úkolem je najít n takové, že 1/n > c * 1/n^2.
#
# Pokud n = c, potom máme c * 1/c^2 = 1/c. Což ještě není ostře menší než 1/c. Stačí ale vzít
# např. n = c + 1. c * 1/(c + 1)^2 = 1/(c + 1) * c/(c + 1) < 1/(c + 1)
#
# e) Co pokud fce nabývají pouze nezáporných hodnot?
#
# Náš argument v příkladu c) přestane fungovat. Lze ale vyrobit podobnou fci, která má stejný problém:
#
# f(n) = n pokud n sudé, jinak 1
# g(n) = n pokud n liché, jinak 1

# Uspořádejte fce do posloupnosti tak, že f_1 \in O(f_2), f_2 \in O(f_3), ...
#
# n!, n^(1/ln n), e^n, n^2, 2^(2^(n + 1)), ln ln n, n, 4^log_2 n, n log_2 n
#
# Pár inkluzí vidíme rovnou:
#
# ln ln n < n < n log_2 n < n^2 < e^n
#
# n! vs e^n? Určitě 3^n > e^n, zvažme:
#
# 3^7 * 3 * 3 * 3  ... 3^7 = 2187
# 7!  * 8 * 9 * 10 ... 7! = 5040
#
# Tento argument funguje pro lib. exponenciální fci!
#
# ln ln n < n < n log_2 n < n^2 < e^n < n!
#
# n^(1/ln n) = (e^ln n)^(1/ln n) = e^(ln n/ln n) = e, tj. konstanta!
#
# n^(1/ln n) < ln ln n < n < n log_2 n < n^2 < e^n < n!
#
# 2^(2^(n + 1)) vs n! ? Na každý činitel ve faktoriálu připadne 2^(2^(n+1)/n).
# Určitě není problém zvolit n takové, aby tento výraz byl ostře větší než n.
#
# n^(1/ln n) < ln ln n < n < n log_2 n < n^2 < e^n < n! < 2^(2^(n + 1))
#
# 4^log_2 n = (2^2)^log_2 n = 2^(2 * log_2 n) = (2^log_2 n)^2 = n^2
#
# n^(1/ln n) < ln ln n < n < n log_2 n < n^2 = 4^log_2 n < e^n < n! < 2^(2^(n + 1))
#
# Fígl: Můžete se podívat na to, co se děje s výrazem f(n)/g(n) jak zvyšujeme n. Pokud
# to směřuje k nějaké konečné hodnotě, pak f(n) \in O(g(n)). Tohle není formální důkaz,
# ale hodí se to k rychlému zorientování, co asi bude větší.

### Cvičení z Programování I ###

# Nová úloha na ReCodExu

rnd = 42

while True:
    guess = int(input('Enter a guess: '))
    if guess < rnd:
        print('Too low, try again.')
    elif guess > rnd:
        print('Too high, try again.')
    else:
        print('You got it!')
        # Jak ukončit nekonečný cyklus?
        break

import random
rnd = random.randint(1, 100)
# Pozor: náhodná čísla nejsou zas až tak náhodná, viz dokumentace

for _ in range(5):
    random.seed(1) # Magie
    print(random.randrange(1_000_000))

# Generování hesla

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz' # Možná by se dalo x, w, atp vynechat

result = ''
for i in range(10):
    if i % 2 == 0: # Souhláska
        result += random.choice(consonants)
    else: # Samohláska
        result += random.choice(vowels)
print(result)

# Jak dobré je tohle heslo?

# Zkusme si naprogramovat "algoritmy" na vážení boxů z minulého cvičení.

# Nejdřív potřebujeme znát váhy boxů... jak od uživatele přečíst více čísel?

# Možnost 1 (nejhorší): nejdřív se zeptáme, kolik mám uživatel čísel napíše

n = int(input('How many numbers??? '))
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)

# Možnost 2: můžeme uživateli dát nějakou speciální hodnotu, kterou může napsat pro ukončení
print('Enter numbers and then write stop')
nums = []
while True: # Dopředu nevíme, kolik čísel bude...
    line = input()
    if line == 'stop':
        break
    nums.append(int(line))
    # Mohli bychom taky hledat speciální číslo, např. -1. Potom ale -1 nikdy nemůže být v našem
    # seznamu nums (může/nemusí být problém).
print(nums)

# Možnost 3: použít speciální EOF symbol (Ctrl+D na linuxech, Ctrl+Z + Enter na windowsech)

# K celému vstupu se dá přistupovat jako ke speciálnímu souboru. O souborech se budeme bavit
# později. Co ale python umí je projít soubor po řádcích pomocí for cyklu:

import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))
print(nums)

# Možnost 4: Přečíst všechno na jedné řádce.

inp = input()
parts = inp.split() # Rozseká podle bílých znaků
nums = []
for part in parts:
    nums.append(int(part))
print(nums)

# Fígl:

nums = [int(x) for x in input().split()]
print(nums)

# Detailně vysvětlíme později. Může se ale hodit na některé ReCodExové úlohy.

# Hledání maxima:

candidate = nums[0]
for i in range(1, len(nums)):
    if nums[i] > candidate:
        candidate = nums[i]
print(nums)

# Hledání maxima a minima:

for i in range(0, len(nums), 2):
    if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
maybeMin = nums[0]
maybeMax = nums[1]
for i in range(2, len(nums), 2):
    if nums[i] < maybeMin:
        maybeMin = nums[i]
    if nums[i + 1] > maybeMax:
        maybeMax = nums[i + 1]
print(f'min: {maybeMin}')
print(f'max: {maybeMax}')

# Jak to opravit pro lichý počet čísel?

## Project Euler 2 ##

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

a = 1
b = 2

fibSum = 0

while a < 4_000_000:
    if a % 2 == 0:
        fibSum += a
    a, b = b, a + b # Vícenásobné přiřazení; najde další číslo v posloupnosti
print(fibSum)
