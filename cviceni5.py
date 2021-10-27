# Třída pro zásobníky (LIFO)
class Stack:
    # Konstruktor
    def __init__(self):
        self._array = [None] * 10
        self._size = 0

    def _full(self):
        return len(self._array) == self._size

    def _expand(self):
        self._array = self._array + [None] * len(self._array)

    # Přidej novou hodnotu na vrchol zásobníku.
    # Pokud je zásobník plný, tak ho nejdřív nafoukneme pomocí metody _expand.
    def push(self, value):
        if self._full():
            self._expand()

        self._size += 1
        self._array[self._size - 1] = value

    # Najdi hodnotu na vrcholu zásobníku.
    def peek(self):
        if self._size == 0:
            return None

        return self._array[self._size - 1]

    # Najdi a odstraň hodnotu z vrcholu zásobníku.
    # Pokud je zásobník prázdný, neprovede se nic.
    def pop(self):
        if self._size == 0:
            return None

        value = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return value

# Třída pro fronty (FIFO)
class Queue:
    # Konstruktor
    def __init__(self):
        self._array = [None] * 10
        self._size = 0
        self._begin = 0

    def _full(self):
        return len(self._array) == self._size

    # Najdi hodnotu na daném indexu.
    def _getAt(self, ix):
        if ix < 0:
            ix += self._size
        return self._array[(self._begin + ix) % len(self._array)]

    # Nastav hodnotu na daném indexu.
    def _setAt(self, ix, value):
        if ix < 0:
            ix += self._size
        self._array[(self._begin + ix) % len(self._array)] = value

    def _expand(self):
        newarray = [None] * (2 * len(self._array))
        # Při nafouknutí stačí zkopírovat vše na začátek pole a pak jen říct, že nový začátek je 0.
        for i in range(self._size):
            newarray[i] = self._getAt(i)
        self._array = newarray
        self._begin = 0

    # Přidej novou hodnotu na začátek fronty.
    # Pokud je fronta plná, tak ji nejdřív nafoukneme pomocí metody _expand.
    def pushFront(self, value):
        if self._full():
            self._expand()

        self._begin -= 1
        self._size += 1
        self._setAt(0, value)

    # Přidej novou hodnotu na konec fronty.
    # Pokud je fronta plná, tak ji nejdřív nafoukneme pomocí metody _expand.
    def pushBack(self, value):
        if self._full():
            self._expand()

        self._size += 1
        self._setAt(-1, value)

    # Najdi hodnotu na začátku fronty.
    def peekFront(self):
        if self._size == 0:
            return None

        return self._getAt(0)

    # Najdi hodnotu na konci fronty.
    def peekBack(self):
        if self._size == 0:
            return None

        return self._getAt(-1)

    # Najdi a odstraň hodnotu ze začátku fronty.
    # Pokud je fronta prázdná, neprovede se nic.
    def popFront(self):
        if self._size == 0:
            return None

        value = self._getAt(0)
        self._setAt(0, None)
        self._begin += 1
        self._size -= 1
        return value

    # Najdi a odstraň hodnotu z konce fronty.
    # Pokud je fronta prázdná, neprovede se nic.
    def popBack(self):
        if self._size == 0:
            return None

        value = self._getAt(-1)
        self._setAt(-1, None)
        self._size -= 1
        return value

# Třída pro (max) haldy
class Heap:
    # Konstruktor
    def __init__(self):
        self._array = []

    # Najdi index rodiče.
    def _parent(self, i):
        return (i - 1) // 2

    # Najdi index levého potomka.
    def _left(self, i):
        return i * 2 + 1

    # Najdi index pravého potomka.
    def _right(self, i):
        return i * 2 + 2

    # Vybublej novou hodnotu na konci haldy směrem nahoru.
    # Předpokládáme, že v rozsahu [begin, end - 1) je halda korektní. Na pozici end - 1 je nová hodnota,
    # která nemusí splňovat haldovou podmínku.
    def _bubbleUp(self, begin, end):
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

    # Vybublej novou hodnotu na začátku haldy směrem dolu.
    # Předpokládáme, že v rozsahu [begin + 1, end) jsou již haldy korektní. Na pozici begin je nový
    # kořen (jehož potomci budou self._left(begin) a self._right(begin)), který nemusí splňovat haldovou podmínku.
    def _bubbleDown(self, begin, end):
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

    # Najdi maximální hodnotu v haldě.
    def peekMax(self):
        if len(self._array) == 0:
            return None
        return self._array[0]

    # Odeber maximální hodnotu z haldy.
    def popMax(self):
        if len(self._array) == 0:
            return None

        max = self._array[0]
        self._array[0] = self._array[-1]
        del self._array[-1]

        # Na pozici 0 je hodnota, která může porušovat haldovou podmínku.
        # Opravíme pomocí self._bubbleDown.
        self._bubbleDown(0, len(self._array))
        return max

    # Přidej novou hodnotu do haldy.
    def push(self, value):
        self._array.append(value)
        self._bubbleUp(0, len(self._array))

    # Postav celou haldu z pole. O(n log n)
    def fromArraySlow(self, array):
        self._array = array[:]
        for i in range(2, len(self._array) + 1):
            self._bubbleUp(0, i)

    # Postav celou haldu z pole. O(n)
    # Viz trik z přednášky.
    def fromArray(self, array):
        self._array = array[:]
        for i in range(self._parent(len(self._array) - 1), -1, -1):
            self._bubbleDown(i, len(self._array))
