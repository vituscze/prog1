def merge(source, target, beginFst, endFst, beginSnd, endSnd, beginTgt):
    fst, snd, tgt = beginFst, beginSnd, beginTgt

    while fst < endFst and snd < endSnd:
        if source[fst] < source[snd]:
            target[tgt] = source[fst]
            fst, tgt = fst + 1, tgt + 1
        else:
            target[tgt] = source[snd]
            snd, tgt = snd + 1, tgt + 1

    while fst < endFst:
        target[tgt] = source[fst]
        fst, tgt = fst + 1, tgt + 1

    while snd < endSnd:
        target[tgt] = source[snd]
        snd, tgt = snd + 1, tgt + 1

def mergesort(array):
    length = len(array)
    
    runLength = 1
    swap = False
    while runLength < length:
        swap = not swap
        runLength *= 2

    src, tgt = array, array.copy()
    if swap:
        src, tgt = tgt, src

    runLength = 1
    while runLength < length:
        for begin in range(0, length, 2 * runLength):
            mid = min(begin + runLength, length)
            end = min(begin + 2 * runLength, length)
            merge(src, tgt, begin, mid, mid, end, begin)
        src, tgt = tgt, src
        runLength *= 2

##########

def id(x):
    return x

def countingSort(array, key, rangeFrom, rangeTo):
    rangeLen = rangeTo - rangeFrom
    counts = rangeLen * [0]
    for x in array:
        counts[key(x) - rangeFrom] += 1

    cumulative = 0
    for i in range(rangeLen):
        counts[i], cumulative = cumulative, counts[i] + cumulative

    result = [None] * len(array)
    for x in array:
        ix = key(x) - rangeFrom
        result[counts[ix]] = x
        counts[ix] += 1
    return result

##########

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        self.head = Node(value, self.head)

    def removeFront(self):
        if self.head != None:
            self.head = self.head.next

    def valueAt(self, index):
        cur = self.head
        while cur != None and index > 0:
            cur = cur.next
            index -= 1
        if cur != None:
            return cur.value
        else:
            return None
