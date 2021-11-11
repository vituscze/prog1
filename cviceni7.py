import math
import random

def fibBad(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibBad(n - 1) + fibBad(n - 2)

def fibMem(n, mem={}):
    if n in mem:
        return mem[n]
    if n <= 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fibMem(n - 1, mem) + fibMem(n - 2, mem)
    mem[n] = res
    return res

def generate(toOpen, toClose=0, str=''):
    if toOpen == 0 and toClose == 0:
        print(str)
        return
    if toOpen > 0:
        generate(toOpen - 1, toClose + 1, str + '(')
    if toClose > 0:
        generate(toOpen, toClose - 1, str + ')')

def increasing(end, start=0, seq=[]):
    print(seq)
    for i in range(start + 1, end + 1):
        increasing(end, i, seq + [i])

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _link(self, node, prev, next):
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

    def linkFront(self, node):
        self._link(node, None, self.head)

    def linkBack(self, node):
        self._link(node, self.tail, None)

    def unlinkFront(self):
        node = self.head
        self._unlink(node)
        return node

    def unlinkBack(self):
        node = self.tail
        self._unlink(node)
        return node

    def fromList(self, list):
        self.head = None; self.tail = None
        for x in list:
            self.linkBack(Node(x))

    def toList(self):
        list = []; it = self.head
        while it != None:
            list.append(it.value)
            it = it.next
        return list

def split(list):
    fst, snd = DoublyLinkedList(), DoublyLinkedList()
    while list.head != None:
        fst, snd = snd, fst
        fst.linkBack(list.unlinkFront())
    return fst, snd

def merge(left, right):
    l = left.unlinkFront(); r = right.unlinkFront(); merged = DoublyLinkedList()
    while True:
        if l != None and (r == None or l.value < r.value):
            merged.linkBack(l)
            l = left.unlinkFront()
        elif r != None:
            merged.linkBack(r)
            r = right.unlinkFront()
        else:
            break
    return merged

def mergesort(list):
    if list.head == list.tail:
        return list

    left, right = split(list)
    return merge(mergesort(left), mergesort(right))

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Vygeneruje strom pro testování. Parametr cutearly slouží k vytváření
# neúplných stromů, dobrá hodnota je mezi 0.3 a 0.5.
def testTree(depth, cutearly=0.0):
    if depth == 0 or random.random() < cutearly:
        return None
    l = testTree(depth - 1, cutearly)
    r = testTree(depth - 1, cutearly)
    return TreeNode(random.randint(0, 100), l, r)

# Nakreslí daný strom na standardní výstup. Později vylepšíme.
def printTree(node, prefix=''):
    if node == None:
        return
    printTree(node.left, prefix + 4 * ' ')
    print(prefix + str(node.value))
    printTree(node.right, prefix + 4 * ' ')

def treeSize(node):
    if node == None:
        return 0
    return treeSize(node.left) + treeSize(node.right) + 1

def treeDepth(node):
    if node == None:
        return 0
    return max(treeDepth(node.left), treeDepth(node.right)) + 1

def treeMin(node):
    if node == None:
        return math.inf
    return min(treeMin(node.left), treeMin(node.right), node.value)

def treeMember(node, value):
    if node == None:
        return False
    return node.value == value or treeMember(node.left, value) or treeMember(node.right, value)
