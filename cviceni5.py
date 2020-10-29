import random

def isSorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

# Index předka
def parent(i):
    return (i - 1) // 2

# Index levého potomka
def left(i):
    return i * 2 + 1

# Index pravého potomka
def right(i):
    return i * 2 + 2

def isHeap(array):
    for i in range(len(array)):
        l = left(i)
        r = right(i)

        if l < len(array) and array[i] < array[l]:
            return False
        if r < len(array) and array[i] < array[r]:
            return False

    return True

def test(tries, fn, check):
    for _ in range(tries):
        size = random.randint(0, 300)

        oldArray = []
        for _ in range(size):
            oldArray.append(random.randint(0, 600))

        newArray = oldArray.copy()

        fn(newArray)
        if not check(newArray):
            return oldArray

    return True

# Přidej nový prvek na konec haldy.
#
# Předpokládáme, že halda je korektní v rozmezí [begin, end - 1). Na pozici
# end - 1 je nový prvek, který nemusí splňovat haldovou podmínku.
def bubbleUp(array, begin, end):
    i = end - 1
    while i > begin:
        p = parent(i)
        if array[p] < array[i]:
            # Pokud je haldová podmínka porušena, prohoď potomka s rodičem a
            # v dalším kroku zkontroluj rodiče.
            array[p], array[i] = array[i], array[p]
            i = p
        else:
            break

# Přidej nový prvek na začátek a vytvoř novou haldu sloučením dvou menších.
#
# Předpokládáme, že v rozmezí [begin + 1, end) jsou již korektní haldy. Na
# pozici begin je nový kořen (jehož potomci budou left(begin) a right(begin)),
# který nemusí splňovat haldovou podmínku.
def bubbleDown(array, begin, end):
    i = begin
    while left(i) < end:
        l = left(i)
        r = right(i)

        # Najdi největšího potomka, který porušuje haldovou podmínku.
        swap = i
        if array[l] > array[swap]:
            swap = l
        if r < end and array[r] > array[swap]:
            swap = r

        if swap != i:
            # Pokud je nalezený prvek jedním z potomků, prohoď potomka
            # s rodičem a v dalším kroku zkontroluj tohoto potomka.
            array[swap], array[i] = array[i], array[swap]
            i = swap
        else:
            # Pokud je největší nalezený prvek rodič, podmínka nebyla porušena
            # a můžeme skončit.
            break

# Postav haldu v poli. O(n log n)
def heapifySlow(array):
    for i in range(2, len(array) + 1):
        bubbleUp(array, 0, i)

# Postav haldu v poli. O(n)
def heapifyFast(array):
    for i in range(parent(len(array) - 1), -1, -1):
        bubbleDown(array, i, len(array))

def heapsort(array):
    heapifyFast(array)
    for i in range(len(array) - 1, 0, -1):
        # V každém kroku prohodíme kořen haldy (což je vždy největší prvek)
        # s posledním prvkem haldy. Po tomto kroku nemusí být haldová podmínka
        # splněna, takže vezmeme nový kořen a postavíme haldu o jeden prvek
        # menší.
        array[i], array[0] = array[0], array[i]
        bubbleDown(array, 0, i)
