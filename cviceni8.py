def combination(input, k, cur):
    if k == 0:
        print(cur)
    elif len(input) == 0:
        return
    else:
        head = input[0]
        tail = input[1:]
        combination(tail, k - 1, cur + [head])
        combination(tail, k, cur)

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
