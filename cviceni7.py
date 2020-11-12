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

    def _at(self, pos):
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node

    def at(self, pos):
        node = self._at(pos)
        if node != None:
            return node.value
        else:
            return None

    def toList(self):
        result = []

        node = self.head
        while node != None:
            result.append(node.value)
            node = node.next

        return result

    def changeAt(self, pos, value):
        node = self._at(pos)
        if node != None:
            node.value = value

    def insertValue(self, pos, value):
        prev = None
        node = self.head
        while pos > 0 and node != None:
            prev = node
            node = node.next
            pos -= 1

        if pos > 0:
            return

        newNode = Node(value, node)
        if prev != None:
            prev.next = newNode
        else:
            self.head = newNode

    def removeValue(self, value):
        prev = None
        node = self.head
        while node != None and node.value != value:
            prev = node
            node = node.next

        if node == None:
            return

        next = node.next
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

    def toList(self):
        result = []
        node = self.head
        while node != None:
            result.append(node.value)
            node = node.next
        return result

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

    def linkAfter(self, prev, node):
        if prev != None:
            next = prev.next
        else:
            next = self.head

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

    def linkBefore(self, next, node):
        if next != None:
            prev = next.prev
        else:
            prev = self.tail

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

    def addFront(self, value):
        node = DoubleNode(value)
        self.linkAfter(None, node)

    def removeFront(self):
        self.unlink(self.head)
