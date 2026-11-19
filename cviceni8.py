### Cvičení z Algoritmizace ###

# Bonusové body za účast

# Řešení DÚ + nové úlohy

## Binární stromy ##

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # občas se může hodit i předek

def test_tree(depth, cut_early=0.0):
    '''
    Vygeneruje strom pro testování. Parametr cut_early slouží k vytváření
    neúplných stromů, dobrá hodnota je mezi 0.3 a 0.5.
    '''
    import random
    if depth == -1 or random.random() < cut_early:
        return None
    l = test_tree(depth - 1, cut_early)
    r = test_tree(depth - 1, cut_early)
    return Node(random.randint(0, 100), l, r)

def print_tree(node, prefix=''):
    '''
    Nakreslí daný strom na standardní výstup. Později vylepšíme.
    '''
    if node is None:
        return
    print_tree(node.left, prefix + 4 * ' ')
    print(prefix + str(node.val))
    print_tree(node.right, prefix + 4 * ' ')

def tree_max(root):
    if root is None:
        return None # prázdný strom nemá maximum

    def go(n):
        vals = [n.val]
        if n.left is not None:
            vals.append(go(n.left))
        if n.right is not None:
            vals.append(go(n.right))
        return max(vals)

    return go(root)

def tree_sum(root):
    total = 0

    def go(n):
        nonlocal total
        if n is None:
            return
        total += n.val # provedeme jako vedlejší efekt
        go(n.left)
        go(n.right)

    # Lze samozřejmě udělat normálně pomocí návratové hodnoty
    go(root)
    return total

def tree_leaf_count(node):
    if node is None:
        return 0
    res = 0
    if node.left is None and node.right is None: # list
        res += 1
    res += tree_leaf_count(node.left)
    res += tree_leaf_count(node.right)
    return res

def tree_depth(node):
    if node is None:
        return -1
    return 1 + max(tree_depth(node.left), tree_depth(node.right))

def deepest_layer(root):
    depth = tree_depth(root)
    result = []

    def go(n, d):
        if n is None:
            return
        # pokud jsme na správně hladině...
        if d == depth:
            result.append(n.val) # ...ulož hodnotu do seznamu
        go(n.left, d + 1)
        go(n.right, d + 1)

    go(root, 0)
    return result

def tree_from_list(elems):
    '''
    Vytvoří balancovaný BVS ze setříděného seznamu.
    '''
    def go(lo, hi):
        if lo == hi: # Rozsah je prázdný
            return None
        mid = (lo + hi) // 2
        return Node(elems[mid], go(lo, mid), go(mid + 1, hi))
    return go(0, len(elems))

def is_tree_symmetric(root):
    '''
    Je strom symetrický podle vertikální osy?
    '''
    if root is None:
        return True # prázdný strom je triviálně symetrický

    def go(first, second):
        if first is None and second is None:
            return True
        if first is None or second is None: # jen jeden z podstromů je prázdný
            return False

        if first.val != second.val:
            return False

        return go(first.left, second.right) and go(first.right, second.left)

    return go(root.left, root.right)


# Připomenutí: jak funguje vkládání a odebírání z BVS

### Cvičení z Programování ###

# Řešení DÚ + nové úlohy

## Debugování programů ##

# Většina z vás už určitě přišla na to, že se do programu
# dají dočasně přidat volání fce print, abyste zjistili,
# co přesně se v programu děje. Na tohle se hodí pár fíglů.

def test1():
    x = 5; y = 6
    print(f'{x=} {y=}') # Automaticky přidá x= a y= do textu

def test2():
    x = 'hello\tworld  ' # mezery na konci, tabulátor mezi slovy
    print(f'the string is {x}') # není zřejmé, že string obsahuje
                                # nějaké netisknutelné znaky navíc
    print(f'the string is {x!r}') # to samé jako repr(x)

# Pokud váš program nefunguje, tak se často nejdřív hodí zkusit
# najít nejmenší protipříklad, který váš program pořád ještě
# rozbije.
#
# Většinou se jedná o problémy s nějakým krajním případem, pro
# které není zapotřebí celý vstup (speciálně pokud je obrovský).

# Pokud se váš program cyklí a nevíte kde, můžete program
# "násilně" zastavit pomocí Ctrl+C a podívat se, ve které části
# kódu byla výjimka KeyboardInterrupt vyvolána.

def inf_loop():
    i = 0
    while True:
        i += 1
    return i

def test3():
    return inf_loop()

# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     test3()
#     ~~~~~^^
#   File "D:\prog1\cviceni8.py", line 168, in test3   <-- odkud byla fce inf_loop zavolána
#     return inf_loop()
#   File "D:\prog1\cviceni8.py", line 164, in inf_loop   <-- přesné místo, kde výjimka vznikla!
#     i += 1
#     ^
# KeyboardInterrupt

# Taky může být užitečné v kódu ověřovat předpoklady, které
# o vašem programu děláte. Pokud se něco pokazí, tak Python
# skončí ihned a řekne vám, který předpoklad byl porušen místo
# toho, aby pokračoval a pak selhal na nějakém úplně jiném místě.

def lower_bound(a, x):
    assert all(a[i] <= a[i + 1] for i in range(len(a) - 1)), 'a is not sorted'

    lo, hi = 0, len(a) - 1
    while lo <= hi: # zkuste změnit na lo < hi
        assert 0 <= lo <= hi + 1 <= len(a), f'bad bounds {lo=} {hi=}'
        # tyhle asserty jsou relativně drahé, můžeme je později odstranit
        # nebo program spustit s python -O
        assert all(v < x for v in a[:lo]), f'a[:{lo}] contains a value >= {x}'
        assert all(v >= x for v in a[hi + 1:]), f'a[{hi + 1}:] contains a value < {x}'

        size = hi - lo + 1
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1 # zkuste změnit na hi = mid
        assert hi - lo + 1 < size, f'range did not shrink ({lo=} {hi=})'

    assert lo == hi + 1, f'loop ended early ({lo=} {hi=})'
    return lo

# Tohle je tedy trochu maximalistický příklad; v praxi byste obvykle
# takhle drahé asserty do cyklů nedávali.

# Pojďme se podívat na debugger ve VSCode (resp. v defaultním Python rozšíření).
# Pokud máte jiné IDE, tak debugger může fungovat trochu jinak, ale základní
# koncepty jsou stejné.

# Základní featury:

# Program se musí spustit v debug režimu (defaultně F5), jinak
# většina těchto věcí nebude k dispozici.

## Breakpoint ##

# Klikněte na červenou tečku u čísla řádky. Program pak na této
# řádce zastaví. Breakpoint se objeví v menu (typicky vlevo dole).
#
# Odeberete stejným způsobem. Pokud chcete jen dočasně vypnout,
# odškrtněte v menu.
#
# Pokud chcete breakpoint aktivovat pouze pokud něco platí, v menu
# se dá přidat podmínka. Program se zastaví na dané řádce pouze pokud
# je breakpoint zapnutý a podmínka platí.
#
# Breakpointy se typicky automaticky zapínají pro neošetřené výjimky.
# V menu případně můžete upravit.
#
# Taky se může hodit fce breakpoint().
#
# Na stejném místě se dá zapnout logpoint, což funguje podobně
# jako print, ale bez nutnosti měnit kód.

## Continue, Step Into, Step Out, Step Over ##

# Když je program pozstaven, tak můžeme buď:
# * pokračovat (F5)
# * udělat jeden krok (F10, +- to znamená posunout se na další řádku)
# * udělat krok dovnitř fce (F11, dává smysl jen, pokud je na řádku nějaké volání fce, jinak se chová jako F10)
# * udělat krok mimo fce (Shift+F11, provede zbytek fce a zastaví se na místě, odkud byla fce zavolána)

## Call Stack ##

# Funkce často volají jiné funkce. Občas je nutné se podívat, co se dělo předtím, než jsme
# se do breakpointu v nějaké hluboce vnořené funkci vůbec dostali. Call stack nám nejen
# dává k dispozici informaci, odkud se naše fce zavolala, ale také i informaci o parametrech
# a lokálních proměnných všech funkcí na call stacku.

def cs_test1(y):
    x = y
    return x

def cs_test2(a):
    a1 = cs_test1(a)
    return a1 + a1

def cs_test3(q1, q2):
    return cs_test2(q1) + cs_test2(q2)

# cs_test3(4, 5)

# Proměnné se z tohoto menu dají i měnit. Může být užitečné pro testování alternativ
# ("co by se stalo kdyby...").

## Watch ##

# Pokud vám informace o proměnných nestačí, můžete do Watch menu přidat nějaký výraz,
# který se automaticky vyhodnotí, když se program zastaví na breakpointu. Pozor na
# vedlejší efekty!

## Debug Console ##

# Pokud vám nestačí ani to, tak se můžete přepnout do tabu "Debug Console", který
# se chová jako interaktivní režim v Pythonu, ale s tím rozdílem, že se nacházíte
# v kontextu breakpointu (a můžete např. měnit lokální proměnné)

STUDENTS = {
    'Adam':  [85, 92, 78, 90],
    'Jana':  [70, 65, 88],
    'Petr':  [95, 91, 99, 100],
    'Dana':  [],
    'Emil':  [55, 70, 65, 75],
}

PASS_LIMIT = 70


def average(scores):
    return sum(scores) / len(scores)


def drop_lowest(scores):
    '''Return the scores without the lowest one.'''
    scores.remove(min(scores))
    return scores


def final_score(scores):
    '''Average of the scores; the lowest one is dropped if there are more than 3.'''
    if len(scores) > 3:
        scores = drop_lowest(scores)
    return average(scores)


def report(students):
    best_name, best_score = None, 0
    for name, scores in students.items():
        score = final_score(scores)
        status = 'pass' if score > PASS_LIMIT else 'FAIL'
        print(f'{name:6} {score:6.1f}  {status}')
        if score > best_score:
            best_name, best_score = name, score
    return best_name


# best = report(STUDENTS)
# print('Best student:', best)
# print("Adam's average over all assignments:", average(STUDENTS['Adam']))

# Problémy:
# 1) ZeroDivisionException, stačí zapnout breakpointy na "uncaught exceptions"
#    řešení: final_score potřebuje případ pro prázdný seznam
# 2) Emil má průměr 70, přesto neprošel
#    může to být floating point error? podmíněný breakpoint na řádku se statusem
#    řešení: neostré porovnání
# 3) Poslední řádka vypíše průměr jako 89, což je špatně
#    breakpoint na print, podíváme se, jak vypadá STUDENTS['Adam']
#    fce report někde musí měnit obsah seznamu, dáme breakpoint na řádku score =
#    a přidáme watch na STUDENTS['Adam'], vkročíme do fce
#    řešení: operaci provedeme na kopii


'''Souhrn objednávek v obchodě.

Pro každého zákazníka vypíše celkovou cenu jeho objednávky a nakonec
položku, které se celkem prodalo nejvíc kusů.

Pravidla:
  * kdo koupí alespoň BULK_LIMIT kusů jedné položky, dostane na tuto položku
    slevu BULK_DISCOUNT,
  * VIP zákazníci dostanou slevu VIP_DISCOUNT na celou objednávku
    (počítanou až po množstevních slevách).

Očekávaný výstup:
alice    119.00 CZK
bob      110.40 CZK
carol    356.25 CZK
dave      84.00 CZK
Most popular item: milk

Program obsahuje 5 chyb. Najděte je a opravte.
Pokud si nebudete vědět rady, na konci souboru najdete nápovědu.
'''

PRICES = {'apple': 12, 'banana': 8, 'bread': 35, 'milk': 24, 'cheese': 89}
BULK_LIMIT = 10        # kdo koupí alespoň tolik kusů jedné položky...
BULK_DISCOUNT = 0.10   # ...dostane na tuto položku slevu 10 %
VIP_CUSTOMERS = {'carol'}
VIP_DISCOUNT = 0.05    # sleva 5 % na celou objednávku

ORDERS = '''
alice: apple x3, bread x1, milk x2
bob: banana x12, apple x2
carol: cheese x1, bread x2, milk x10
dave: milk x1, apple x5
'''


def parse_line(line):
    """'alice: apple x3, bread x1' -> ('alice', [('apple', 3), ('bread', 1)])"""
    customer, rest = line.split(':')
    items = []
    for part in rest.split(','):
        name, qty = part.strip().split(' x')
        items.append((name, qty))
    return customer, items


def item_price(name, qty):
    '''Cena qty kusů dané položky včetně množstevní slevy.'''
    price = PRICE[name] * qty
    if qty >= BULK_LIMIT:
        price = price * (1 - BULK_DISCOUNT)
    return price


def order_total(customer, items):
    '''Celková cena objednávky včetně všech slev.'''
    total = 0
    for name, qty in items:
        total += item_price(name, qty)
        if customer in VIP_CUSTOMERS:
            total = total * (1 - VIP_DISCOUNT)
    return total


def count_items(items):
    '''Kolik kusů jednotlivých položek obsahuje objednávka.'''
    counts = {}
    for name, qty in items:
        if name not in counts:
            counts[name] = 0
        counts[name] += qty
    return counts


def most_popular(orders):
    '''Položka, které se ve všech objednávkách dohromady prodalo nejvíc kusů.'''
    counts = {}
    for customer, items in orders:
        counts.update(count_items(items))

    best = None
    for name in counts:
        if best is None or counts[name] > counts[best]:
            best = name
    return best


def main():
    orders = []
    for line in ORDERS.splitlines():
        orders.append(parse_line(line))

    for customer, items in orders:
        print(f'{customer:6} {order_total(customer, items):8.2f} CZK')
    print('Most popular item:', most_popular(orders))


# main()




























# ------------------------------------------------------------------------------
# Nápověda (čtěte, jen pokud si opravdu nevíte rady)
# ------------------------------------------------------------------------------
#
# 1. Když program spadne, zapněte v debuggeru v panelu Breakpoints volbu
#    „Uncaught Exceptions“. Program se zastaví přímo v místě chyby a vy se
#    můžete podívat na hodnoty proměnných. Jsou takové, jaké čekáte?
#    Všímejte si i jejich typu.
#
# 2. Jaký řádek dostane funkce parse_line úplně jako první?
#
# 3. Porovnejte výstup s očekávaným výstupem řádek po řádku, ne jen první
#    dva nebo tři řádky.
#
# 4. Cena pro carol nesedí. Dejte si do funkce order_total podmíněný breakpoint
#    s podmínkou customer == 'carol' a krokujte. Jak se mění proměnná total?
#
# 5. Nejoblíbenější položka nesedí. Přidejte si do panelu Watch výraz counts
#    a krokujte funkci most_popular. Odpovídají hodnoty v counts po každé
#    objednávce tomu, co čekáte?
