### Cvičení z Algoritmizace ###

# Bonusové body za účast

# Řešení DÚ + nové úlohy

## Rekurze ##

# V Pythonu můžeme zavolat funkci, kterou právě definujeme. Tj. definice
# funkce f může obsahovat volání samotné funkce f.

def f(x):
    # ...
    f(x)
    # ...

# Tomuto konceptu se říká rekurze. Aby rekurze vůbec fungovala, potřebujeme
# splnit dvě podmínky:
#
# a) funkce má nějaký základní případ, který se dá vyřešit nerekurzivně
# b) funkce se rekurzivně volá na menší a menší argumenty
#
# (v praxi jsou podmínky a) a b) trochu komplexnější, ale pro úvod nám to bude stačit)

def g1(n):
    return 1 + g1(n - 1)  # Špatně: chybí základní případ

def g2(n):
    if n == 0:
        return 1
    return 2 * g2(n) # Špatně: argument se nezmenšuje

def g3(n):
    if n == 0:
        return 1
    return 1 + g3(n // 2) # OK, alespoň pro nezáporná čísla

# Pár typických příkladů:

# Faktoriál
def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

# n-té Fibonacciho číslo
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# Lepší řešení
def fib_fast(n):
    def go(rem, a, b):  # Parametry a a b si pamatují poslední dvě Fib. čísla
        if rem == 0:
            return a
        return go(rem - 1, b, a + b)

    return go(n, 0, 1)

# Proč je pomalé řešení tak pomalé?

# Rekurze je v Pythonu celkem limitovaná.

def test():
    def go(n):
        return 0 if n == 0 else n + go(n - 1)

    print(go(1000))

# Limit se dá ale upravit. V praxi je 1000 dost na většinu problémů.

def fac_iter(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

import time

def time_it(fn, arg, count=10000):
    t1 = time.time()  # Python na podobné věci má i specializované nástroje
    for _ in range(count):  # Jedno volání je příliš rychlé, tak jich uděláme více najednou
        fn(arg)
    t2 = time.time()
    print(f'took {t2 - t1:.3f} s')

# time_it(fac, 50)
# time_it(fac_iter, 50)

# Jak o rekurzi přemýšlet? Určitě už teď dobře ovládáte matematickou indukci. Rekurze je
# jen indukce v přestrojení (a to není náhoda). Když píšete rekurzivní funkci, tak nejdřív
# najděte jednoduché případy, které se dají řešit nerekurzivně (v matematice: ukažte tvrzení
# pro nulu nebo pár malých čísel). Pak předpokládejte, že funkce už funguje korektně
# pro všechny menší vstupy (indukční přepoklad) a pomocí toho postavte řešení pro větší vstup.

# Hanoiské věže

def hanoi(n, source, target, spare, moves):
    if n == 0:
        return
    hanoi(n - 1, source, spare, target, moves)
    moves.append((source, target))
    hanoi(n - 1, spare, target, source, moves)

# Kolik tahů potřebujeme pro N disků?

# Tvrzení: tahy(N) = 2^N - 1.
#
# Důkaz indukcí. Pro N = 0 zjevně fce neudělá žádný tah, tahy(0) = 2^0 - 1 = 0. OK.
# Pro N > 0: počet kroků je tahy(N - 1) + 1 + tahy(N - 1) = 2 * (2^(N - 1) - 1) + 1 = 2*2^(N - 1) - 2 + 1 = 2^N - 1. OK.

# Vizualizace pomocí tkinter

import time
import tkinter as tk

DISK_HEIGHT = 40          # height of one disk
SMALLEST_DISK_WIDTH = 70  # width of the smallest disk
DISK_WIDTH_STEP = 40      # each bigger disk is this much wider than the previous one
POLE_WIDTH = 8            # width of a pole
GAP = 40                  # space between the biggest disks of neighbouring towers
TOP_MARGIN = 80           # space above the poles (for the text)
BOTTOM_MARGIN = 30        # space below the ground
FONT_SIZE = 18            # size of the text

COLORS = ['red', 'orange', 'gold', 'green', 'blue', 'purple', 'pink', 'brown']

def disk_width(disk):
    return SMALLEST_DISK_WIDTH + (disk - 1) * DISK_WIDTH_STEP

def tower_width(n):
    return disk_width(n) + GAP

def ground_y(n):
    return TOP_MARGIN + (n + 1) * DISK_HEIGHT


def draw(canvas, towers, n, message):
    canvas.delete('all')
    ground = ground_y(n)

    canvas.create_text(GAP, TOP_MARGIN // 2, text=message, anchor='w', font=('Arial', FONT_SIZE))

    for i in range(3):
        center = tower_width(n) * i + tower_width(n) // 2

        pole_top = ground - (n + 1) * DISK_HEIGHT
        canvas.create_rectangle(center - POLE_WIDTH // 2, pole_top,
                                center + POLE_WIDTH // 2, ground,
                                fill='black')

        for level in range(len(towers[i])):
            disk = towers[i][level]
            half_width = disk_width(disk) // 2
            top = ground - (level + 1) * DISK_HEIGHT
            color = COLORS[(disk - 1) % len(COLORS)]
            canvas.create_rectangle(center - half_width, top,
                                    center + half_width, top + DISK_HEIGHT,
                                    fill=color)

    canvas.create_line(0, ground, 3 * tower_width(n), ground, width=3)


def visualize(n, moves, delay=1):
    window = tk.Tk()
    window.title('Towers of Hanoi')
    canvas = tk.Canvas(window, width=3 * tower_width(n), height=ground_y(n) + BOTTOM_MARGIN, bg='white')
    canvas.pack()

    towers = [list(range(n, 0, -1)), [], []]
    draw(canvas, towers, n, 'Start')
    window.update()

    step = 1
    for source, target in moves:
        time.sleep(delay)  # pro jednoduchost; lepší je použít window.after(...)
        disk = towers[source].pop()
        towers[target].append(disk)
        message = f'Move {step}: disk {disk} from tower {source} to tower {target}'
        draw(canvas, towers, n, message)
        window.update()
        step = step + 1

    window.mainloop()

# n = 4
# moves = []
# hanoi(n, 0, 2, 1, moves)
# visualize(n, moves)

# Binární půlení rekurzivně

def bin_search(a, x):
    def go(lo, hi):
        if lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] == x:
                return True
            elif a[mid] < x:
                return go(mid + 1, hi)
            else:
                return go(lo, mid - 1)
        else:
            return False  # Prázdný interval

    return go(0, len(a) - 1)

### Cvičení z Programování ###

# Řešení DÚ + nové úlohy

# Obousměrné spojové seznamy

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # První uzel seznamu
        self.tail = None  # Poslední uzel seznamu

    def _link(self, node, prev, next):
        '''
        Zařadí uzel node mezi (po sobě jdoucí) uzly prev a next.
        '''
        if node == None:
            return

        node.prev = prev
        node.next = next

        if prev != None:
            prev.next = node
        else:
            self.head = node

        if next != None:
            next.prev = node
        else:
            self.tail = node

    def _unlink(self, node):
        '''
        Odstraní uzel node ze spojového seznamu.
        '''
        if node == None:
            return

        prev, node.prev = node.prev, None
        next, node.next = node.next, None

        if prev != None:
            prev.next = next
        else:
            self.head = next

        if next != None:
            next.prev = prev
        else:
            self.tail = prev

    def link_front(self, node):
        self._link(node, None, self.head)

    def link_back(self, node):
        self._link(node, self.tail, None)

    def unlink_front(self):
        node = self.head
        self._unlink(node)
        return node

    def unlink_back(self):
        node = self.tail
        self._unlink(node)
        return node

    # Pomocné operace pro testování
    def from_list(self, list_):
        self.head = None; self.tail = None
        for x in list_:
            self.link_back(Node(x))

    def to_list(self):
        list_ = []; it = self.head
        while it != None:
            list_.append(it.value)
            it = it.next
        return list_

# Mergesort na spojových seznamech.

# Jak spojový seznam efektivně rozpůlit? Mergesort nepotřebuje,
# aby prvky byly v nějakém konkrétním pořadí. Nemusíme tedy nutně
# brát první a druhou polovinu. Sudé vs liché pozice je jednodušší.

def split(list_):
    fst, snd = DoublyLinkedList(), DoublyLinkedList()
    while list_.head != None:
        fst, snd = snd, fst
        fst.link_back(list_.unlink_front())
    return fst, snd

def merge(left, right):
    l = left.unlink_front()
    r = right.unlink_front()
    merged = DoublyLinkedList()
    while l != None or r != None:
        if l != None and (r == None or l.value < r.value):
            merged.link_back(l)
            l = left.unlink_front()
        else:
            merged.link_back(r)
            r = right.unlink_front()
    return merged

def mergesort(list_):
    if list_.head == list_.tail:  # Prázdný nebo jednoprvkový seznam
        return list_
    left, right = split(list_)
    return merge(mergesort(left), mergesort(right))

# Další užitečné zabudované datové struktury:
#
# Množiny (sets):

empty_set = set()
nonempty_set = {1,2,3}

# Nemůže obsahovat duplicity!
# Metody: add, remove
# Operátory: &, |, ^, -
# Dá se projít for-cyklem, pořadní prvků není garantováno.
# Ne všechny hodnoty se dají do množin dát, např. seznam, množina.

# Slovníky (dictionaries):

empty_dict = {}  # nebo dict()
nonempty_dict = {'five':5, 'four':4}

# Mapují klíče na hodnoty. Klíče se chovají jako množina (nemohou být duplicitní).
# Metody: items, values, keys
# Operátory: |, del
# Přístup na prvek: [...]

del nonempty_dict['five']
nonempty_dict['six'] = 6

# Typické použití s for-cyklem:
for k, v in nonempty_dict.items():
    print(f'key {k}: {v}')

# Podobně jako množiny se ne všechny hodnoty dají použít jako klíč.

# Odbočka: list, set a dictionary comprehensions

test_list = [2**x for x in range(10) if x % 2 == 1]
test_set = {abs(x) for x in range(-10, 11) if x != 0}
test_dict = {x: x**2 for x in range(10)}

# for funguje podobně jako for-cyklus: přijme libovolnou posloupnost
# (užitečné např. pro soubory).

N = 5
id_matrix = [[int(i == j) for j in range(N)] for i in range(N)]
# Vnořování je taky OK.

# for-ů může být více:
pairs = [(x, y) for x in range(5) for y in 'abcd']

test_gen = (x**2 for x in range(10))  # ???
# Jestli na konci semestru zbyde čas, tak si generátory ukážeme.

def word_frequencies(text):
    '''
    Najde slova v textu a pro každé unikátní slovo určí počet výskytů.
    Výsledek vrátí jako slovník; klíče jsou unikátní slova, odpovídající
    hodnoty pak výskyty.

    Jako slovo označíme souvislý kus textu, který neobsahuje žádné bílé
    znaky. Stačí tedy vhodně použít str.split.
    '''
    pass

def most_common_word(text):
    '''
    Najde nejčetnější slovo v textu. Výsledek vraťte ve formě dvojice (word, count).
    '''
    pass

def same_dict(dict1, dict2):
    '''
    Určí, jestli jsou dva slovníky identické: mají stejné klíče a každý klíč má
    stejné odpovídající hodnoty. Nepoužívejte operátor == na samotných slovnících
    (ten dělá přesně tohle).

    >>> same_dict({10:20, 30:40}, {30:40, 10:20})
    True

    >>> same_dict({10:20, 30:40}, {30:40, 10:20, 5:6})
    False
    '''
    pass

def experiment():
    '''
    V Pythonu občas budete chtít určit, jestli posloupnost obsahuje duplicitní hodnoty.
    Zkuste to implementovat dvěma způsoby: pomocí seznamu a pomocí množin. Proveďte
    malý experiment (podobně jako fce time_it výše), který určí, která z těchto možností
    je lepší.

    Efektivní řešení pomocí seznamu bude potřebovat fci sorted(...).

    Testovací data vygenerujte pomocí modulu random.
    '''
    pass
