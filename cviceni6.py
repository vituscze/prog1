### Cvičení z Algoritmizace ###

# Bonusové body za účast

# Řešení DÚ + nové úlohy

# Mírně modifikovaný kód z přednášky
def prihradkoveTrideni(a, pos):
    k = 10 # 0..9
    def klic(n):
        return (n // 10**pos) % 10
        # V praxi se netřídí podle jednotlivých číslic (o základu 10),
        # ale bere se několik bitů najednou, např.
        # return (n >> pos * 8) & 0xFF
        # (potřebuje k = 256)

    c = [0] * k

    for x in a:
        c[klic(x)] += 1

    sum = 0
    for i in range(k):
        c[i], sum = sum, c[i] + sum

    b = [None] * len(a)

    for x in a:
        b[c[klic(x)]] = x
        c[klic(x)] += 1

    return b

# Proč je zapotřebí v Radix sortu třídit od poslední položky klíče?
# (což je v našem případě poslední číslice)

def radix_sort(a, digits):
    for d in range(digits):
        a = prihradkoveTrideni(a, d)
    return a

def radix_sort_alt(a, digits):
    for d in reversed(range(digits)):
        a = prihradkoveTrideni(a, d)
    return a

import random

def generate_test(digits=3):
    return [random.randrange(10**digits) for _ in range(30)]

### Cvičení z Programování ###

# Řešení DÚ + nové úlohy

# Práce se soubory. V Pythonu na to máme funkci open, která
# otevře/vytvoří soubor. První argument je jméno souboru (resp. cesta
# k souboru - absolutní či relativní). Pokud neuvedete žádný další
# argument, otevře se soubor pro čtení v textovém módu.
#
# 'r' -> čtení textu
# 'w' -> zapisování textu (odstraní předchozí obsah souboru)
# 'a' -> zapisování textu (přidá nový text na konec)
#
# Navíc se ještě dá přidat 'b'; pak se soubor otevře v binárním módu
# (čtení/zápis bytů).
#
# Soubor je také zapotřebí zavřít. Pokud na to zapomenete, je možné
# že část obsahu bude chybět (buffer).
#
# Zapisování: metoda write
# Čtení: metody read, readline, readlines
#
# read - můžete si říct, kolik znaků chcete přečíst; jinak přečte vše
# readlines - přečte vše a vrátí to jako seznam řádek

def test_write():
    f = open('a.txt', 'w')
    f.write('Hello world!\n')
    f.write('test\n')
    f.close()

def test_read():
    f = open('a.txt', 'r')
    print(f.readlines())
    f.close()

# Pokud se vám \n na konci nelíbí, můžete použít metodu strip resp. rstrip.

# Problém!
def test_read2():
    f = open('a.txt', 'r')
    lines = f.readlines()
    print(lines[2]) # Vyhodí výjimku; soubor se nikdy nezavře
    f.close()

# V Pythonu se standardně řeší pomocí speciálního příkazu 'with':

def test_read3():
    with open('a.txt', 'r') as f:
        lines = f.readlines()
        print(lines[2]) # Vyhodí výjimku
        # Nemusíme soubor manuálně zavřít; zavře se automaticky na konci with bloku

# Viděli jsme, že se for cyklus dá použít na sys.stdin; lze taky použít na jiné
# (obyčejné) soubory.

def test_read4():
    with open('a.txt', 'r') as f:
        for line in f:
            print(line, end='') # line obsahuje \n

# print taky umí psát do souboru, což se občas může hodit
# print('abc', file=f)

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, val):
        self.head = Node(val, self.head)

    def pop_front(self):
        if self.head is None:
            return

        n = self.head
        self.head = self.head.next
        return n.val

    def print(self):
        it = self.head # Iterátor
        while it is not None:
            print(it.val, end=' ')
            it = it.next # Přesuneme na další
        print()

class SortedList:
    def __init__(self):
        self.head = None

    def member(self, val):
        '''
        Určí, jestli se hodnota val nachází v setříděném spojovém seznamu.
        '''
        # Seznam můžete projít klidně celý, ale protože víme, že je setříděný,
        # stačí projít pouze tu část, která je menší nebo rovna val.
        pass

    def insert(self, val):
        '''
        Vloží nový prvek do setříděného spojového seznamu. Pokud již
        seznam prvek obsahuje, nedělá nic.
        '''
        # Nejprve musíte najít poslední uzel, který je ostře menší než val.
        # Za něj potom přijde nový uzel s touto hodnotou.
        # Speciální případ: co když je nová hodnota menší než všechny prvky v
        # spojovém seznamu?
        pass

    def remove(self, val):
        '''
        Odstraní prvek ze setříděného seznamu. Pokud v seznamu není,
        nedělá nic.
        '''
        # Najít uzel, který daný prvek obsahuje je jednoduché. Abychom ho
        # ale mohli ostranit, musíme znát jeho předka. Musíte tedy najít
        # oba tyto uzly.
        # Speciální případ: co když je hledaný prvek na začátku seznamu?
        pass

    def print(self):
        it = self.head
        while it is not None:
            print(it.val, end=' ')
            it = it.next
        print()

def test_ll():
    import random
    vals = list(range(20))
    random.shuffle(vals)
    print(f'testuji na {vals}')
    ll = SortedList()
    for v in vals:
        ll.insert(v)
    for v in vals:
        assert ll.member(v), f'chybi prvek {v}'
    for v in vals[:10]:
        ll.remove(v)
    for v in vals[:10]:
        assert not ll.member(v), f'prvek {v} nebyl smazan'
    for v in vals[10:]:
        assert ll.member(v), f'prvek {v} byl omylem smazan'
    print('vse OK')
