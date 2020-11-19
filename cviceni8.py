class DoubleNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def link(self, prev, next, node):
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

    def linkAfter(self, prev, node):
        self.link(prev, self.head if prev == None else prev.next, node)

    def linkBefore(self, next, node):
        self.link(self.tail if next == None else next.prev, next, node)

    def unlink(self, node):
        prev = node.prev
        next = node.next

        node.prev = None
        node.next = None

        if prev != None:
            prev.next = next
        else:
            self.head = next

        if next != None:
            next.prev = prev
        else:
            self.tail = prev

    def unlinkHead(self):
        node = self.head
        if node != None:
            self.unlink(node)
        return node

    def unlinkTail(self):
        node = self.tail
        if node != None:
            self.unlink(node)
        return node

    def linkHead(self, node):
        self.linkAfter(None, node)

    def linkTail(self, node):
        self.linkBefore(None, node)

    def empty(self):
        return self.head == None

    def fromArray(self, array):
        for a in array:
            self.linkTail(DoubleNode(a))

    def toArray(self):
        result = []
        cur = self.head
        while cur != None:
            result.append(cur.value)
            cur = cur.next
        return result

class Stack:
    def __init__(self):
        self.list = DoublyLinkedList()

    def empty(self):
        return self.list.empty()

    def push(self, value):
        self.list.linkHead(DoubleNode(value))

    def pop(self):
        if not self.empty():
            return self.list.unlinkHead().value

class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def empty(self):
        return self.list.empty()

    def push(self, value):
        self.list.linkTail(DoubleNode(value))

    def pop(self):
        if not self.empty():
            return self.list.unlinkHead().value

def split(list):
    fst, snd = DoublyLinkedList(), DoublyLinkedList()
    while not list.empty():
        fst, snd = snd, fst
        fst.linkHead(list.unlinkTail())
    return fst, snd

def merge(fst, snd):
    fstHead = fst.unlinkHead()
    sndHead = snd.unlinkHead()

    result = DoublyLinkedList()

    while fstHead != None and sndHead != None:
        if fstHead.value < sndHead.value:
            result.linkTail(fstHead)
            fstHead = fst.unlinkHead()
        else:
            result.linkTail(sndHead)
            sndHead = snd.unlinkHead()

    while fstHead != None:
        result.linkTail(fstHead)
        fstHead = fst.unlinkHead()

    while sndHead != None:
        result.linkTail(sndHead)
        sndHead = snd.unlinkHead()

    return result

def mergesort(list):
    if list.head == list.tail:
        return list

    left, right = split(list)
    leftSorted = mergesort(left)
    rightSorted = mergesort(right)
    return merge(leftSorted, rightSorted)

##########

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

mem = {}
def fibMem(n):
    if n in mem:
        return mem[n]

    r = None
    if n <= 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        r = fibMem(n - 1) + fibMem(n - 2)

    mem[n] = r
    return r
