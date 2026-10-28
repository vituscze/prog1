### Cvičení z Algoritmizace + Programování ###

# Bonusové body za účast

# Dneska: zásobníky, haldy, fronty (algoritmizace) pomocí objektů (programování)

# Řešení všech DÚ + nové úlohy

# Objekty už jsme v Pythonu viděli (list.append, str.split, atp), teďka si ukážeme, jak
# vytvořit vlastní.

# Python je třídový OO jazyk. Nejdřív tedy potřebujeme definovat třídu. Třída
# funguje jako recept, podle kterého se objekty budou vytvářet.

# Data se uloží do tzv. atributů, jednoduše pomocí přiřazení. Typicky se atributy
# inicializují v konstruktoru, což je speciální funkce, která se zavolá když se
# objekt vytváří.

class Person:
    def __init__(self, name, age, gender):
        # Speciální parametr self referuje na právě vytvářený objekt
        self.name = name
        self.age = age
        self.gender = gender

    # pozn.: definici lze zjednodušit pomocí modulu dataclass, možná si ukážeme jindy

    # Definice metody. Vždy musí mít extra parametr navíc: reference na objekt, na kterém
    # se metoda volá. V jiných jazycích není nutné explicitně uvádět.
    def to_str(self):
        return (
            f'name:   {self.name}\n'
            f'age:    {self.age}\n'
            f'gender: {self.gender}\n'
        )

def test():
    p = Person('Adam', 20, 'm')
    print(p.to_str())

# V objektu je přístupné všechno, což není vždy žádoucí. Atributy a metody, které začínají podtržítkem
# jsou určeny pro interní použití. Snažte se to dodržovat (C# to potom vynucuje pomocí klíčových slov
# public, private, protected).

INITIAL_CAPACITY = 10

class Stack:
    '''
    A LIFO container (last-in, first-out) implemented as a dynamic array.
    '''

    def __init__(self):
        '''
        Creates an empty stack with initial capacity of 10.
        '''
        self._array = [None] * INITIAL_CAPACITY
        self._size = 0

    def _full(self):
        return len(self._array) == self._size

    def _expand(self):
        # Python tohle víceméně řeší za nás. V low-level jazyce jako např. C by bylo
        # zapotřebí nejdříve vytvořit pole s dvojnásobnou délkou, prvky do něj zkopírovat
        # a původní pole potom uvolnit.
        self._array = self._array + [None] * len(self._array)

    def size(self):
        '''
        Returns the number of elements in the stack.
        '''
        return self._size

    def push(self, value):
        '''
        Adds a new value to the top of the stack.

        If the stack is full, it first expands it with the _expand method, doubling
        its capacity.
        '''
        if self._full():
            self._expand()

        self._size += 1
        self._array[self._size - 1] = value

    def peek(self):
        '''
        Returns the value at the top of the stack.

        If the stack is empty, returns None.
        '''
        if self._size == 0:
            return None

        return self._array[self._size - 1]

    def pop(self):
        '''
        Removes the top value of the stack and returns it.

        Returns None if the stack is empty.
        '''
        if self._size == 0:
            return None

        value = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return value

class Heap:
    def __init__(self):
        self._array = []

    def _parent(self, i):
        '''
        Najdi index rodiče.
        '''
        return (i - 1) // 2

    def _left(self, i):
        '''
        Najdi index levého potomka.
        '''
        return i * 2 + 1

    def _right(self, i):
        '''
        Najdi index pravého potomka.
        '''
        return i * 2 + 2

    def _bubble_up(self, begin, end):
        '''
        Vybublej novou hodnotu na konci haldy směrem nahoru.
        Předpokládáme, že v rozsahu [begin, end - 1) je halda korektní. Na pozici end - 1 je nová hodnota,
        která nemusí splňovat haldovou podmínku.
        '''
        i = end - 1
        while i > begin:
            p = self._parent(i)
            if self._array[p] < self._array[i]:
                # Haldová podmínka je porušena, prohodíme hodnoty a v dalším kroku zkontrolujeme
                # haldovou podmínku pro rodiče.
                self._array[p], self._array[i] = self._array[i], self._array[p]
                i = p
            else:
                break

    def _bubble_down(self, begin, end):
        '''
        Vybublej novou hodnotu na začátku haldy směrem dolu.
        Předpokládáme, že v rozsahu [begin + 1, end) jsou již haldy korektní. Na pozici begin je nový
        kořen (jehož potomci budou self._left(begin) a self._right(begin)), který nemusí splňovat haldovou podmínku.
        '''
        i = begin
        while self._left(i) < end:
            l = self._left(i)
            r = self._right(i)

            # Hledáme potomka, který porušuje haldovou podmínku. Pokud ji porušují oba potomci,
            # pak hledáme toho většího.
            swap = i
            if self._array[l] > self._array[swap]:
                swap = l
            if r < end and self._array[r] > self._array[swap]:
                swap = r

            if swap != i:
                # Alespoň jeden z potomků porušoval haldovou podmínku. Prohodíme většího z těchto
                # potomků s rodičem (tím pádem bude rodič opět největší) a v dalším kroku zkontrolujeme
                # tohoto potomka.
                self._array[swap], self._array[i] = self._array[i], self._array[swap]
                i = swap
            else:
                break

    def peek_max(self):
        '''
        Najdi maximální hodnotu v haldě.
        '''
        if len(self._array) == 0:
            return None
        return self._array[0]

    def pop_max(self):
        '''
        Odeber maximální hodnotu z haldy.
        '''
        if len(self._array) == 0:
            return None

        max_ = self._array[0] # max už je definovaný
        self._array[0] = self._array[-1]
        del self._array[-1] # O(1)

        # Na pozici 0 je hodnota, která může porušovat haldovou podmínku.
        # Opravíme pomocí self._bubble_down.
        self._bubble_down(0, len(self._array))
        return max_

    def push(self, value):
        '''
        Přidej novou hodnotu do haldy.
        '''
        self._array.append(value)
        self._bubble_up(0, len(self._array))

    def from_array_slow(self, array):
        '''
        Postav celou haldu z pole. O(n log n)
        '''
        self._array = array[:]
        for i in range(2, len(self._array) + 1):
            self._bubble_up(0, i)

    def from_array(self, array):
        '''
        Postav celou haldu z pole. O(n)
        Viz trik z přednášky.
        '''
        self._array = array[:]
        for i in range(self._parent(len(self._array) - 1), -1, -1):
            self._bubble_down(i, len(self._array))

class Deque:
    '''
    Deque implements a double-ended queue with amortized
    O(1) insertion and deletion at both ends of the queue.
    '''

    def __init__(self):
        '''
        Creates an empty queue with initial capacity of 10.
        '''
        # Hint: Pokud chceme efektivně přidávat prvky na konec i na začátek fronty,
        # můžeme se na seznam dívat jako na smyčku: jakmile se dostaneme na konec, další
        # prvek je ten na začátku.
        #
        # Např. pokud máme v seznamu tyto hodnoty (_ označuje prázdné sloty)
        #  [_,_,_,_,1,2,3,4]
        # a chceme přidat číslo 5 na konec *fronty*, tak seznam nemusíme nafukovat,
        # stačí místo toho přidat 5 na začátek *seznamu*:
        #  [5,_,_,_,1,2,3,4]
        #
        # Aby tohle fungovalo, tak si musíte pamatovat, kde prvky začínají a končí.
        self._array = [None] * INITIAL_CAPACITY
        self._start = 0 # Pozice prvního prvku fronty
        self._size = 0 # Počet prvků ve frontě
        # Pro výše uvedený seznam by tedy platilo:
        #  self._array == [5,None,None,None,1,2,3,4]
        #  self._start == 4  <- pozice prvku 1
        #  self._size  == 5
        #
        # Pokud chcete, můžete si místo self._size uložit self._end. self._size je
        # ale trochu jednodušší na implementaci.
        #
        # Při nafukování je jednodušší prvky nakopírovat do nového seznamu pomocí cyklu
        # a dát je hezky na začátek (tj. nastavit self._start = 0)

    # Tady se vám mohou hodit nějaké pomocné metody: přístup k prvku,
    # přiřazení prvku, nafouknutí fronty.

    def size(self):
        '''
        Returns the number of elements currently in the deque.
        '''
        pass

    def push_front(self, value):
        '''
        Adds a new value to the start of the queue.
        '''
        # Pokud je fronta plná, tak ji nejdříve musíte nafouknout.
        pass

    def push_back(self, value):
        '''
        Adds a new value to the end of the queue.
        '''
        # Pokud je fronta plná, tak ji nejdříve musíte nafouknout.
        pass

    def peek_front(self):
        '''
        Returns the value at the start of the queue or None if empty.
        '''
        pass

    def peek_back(self):
        '''
        Returns the value at the end of the queue or None if empty.
        '''
        pass

    def pop_front(self):
        '''
        Removes the value at the start of the queue and returns it.

        Returns None if the queue is empty.
        '''
        pass

    def pop_back(self):
        '''
        Removes the value at the end of the queue and returns it.

        Returns None if the queue is empty.
        '''
        pass

def test_deque():
    d = Deque()
    for i in range(10, 20):
        d.push_back(i) # vloží 10-19 na konec
    for i in range(9, -1, -1):
        d.push_front(i) # vloží 0-9 na začátek
    assert d.peek_front() == 0 # na začátku by měla být 0
    assert d.peek_back() == 19 # na konci 19
    for _ in range(5):
        d.pop_back() # odebere 5 prvků z konce
    for _ in range(5):
        d.pop_front() # odebere 5 prvků za začátku
    assert d.peek_back() == 14
    assert d.peek_front() == 5
