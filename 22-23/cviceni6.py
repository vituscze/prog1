class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SortedList:
    def __init__(self):
        self.head = None

    def member(self, value):
        it = self.head
        while it != None and it.value < value:
            it = it.next
        return it != None and it.value == value

    def insert(self, value):
        prev = None
        it = self.head
        while it != None and it.value < value:
            prev = it
            it = it.next
        if it != None and it.value == value:
            return
        if prev == None:
            self.head = Node(value, it)
        else:
            prev.next = Node(value, it)

    def remove(self, value):
        prev = None
        it = self.head
        while it != None and it.value < value:
            prev = it
            it = it.next
        if it == None or it.value != value:
            return
        if prev == None:
            self.head = it.next
        else:
            prev.next = it.next

    def print(self):
        it = self.head
        while it != None:
            print(it.value, end=' ')
            it = it.next
        print()

def merge(left, right):
    l = 0; r = 0; merged = []
    while True:
        hasLeft = l < len(left)
        hasRight = r < len(right)
        if hasLeft and (not hasRight or left[l] < right[r]):
            merged.append(left[l])
            l += 1
        elif hasRight:
            merged.append(right[r])
            r += 1
        else:
            break
    return merged

def mergesort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    return merge(mergesort(array[:mid]), mergesort(array[mid:]))
