class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        self.head = Node(value, self.head)

    def at(self, pos):
        s = self.head
        while pos > 0 and s != None:
            s = s.next
            pos -= 1
        if s != None:
            return s.value
        else:
            return None

    def removeFront(self):
        if self.head != None:
            self.head = self.head.next

    def removeValue(self, value):
        prev = None
        cur = self.head
        while cur != None and cur.value != value:
            prev = cur
            cur = cur.next

        next = None
        if cur != None:
            next = cur.next

        if prev != None:
            prev.next = next
        else:
            self.head = next


class DoubleNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def linkAfter(self, prev, node):
        next = self.head
        if prev != None:
            next = prev.next

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
