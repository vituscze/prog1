import math
import random

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def testTree(depth, cutearly=0.0):
    if depth == 0 or random.random() < cutearly:
        return None
    l = testTree(depth - 1, cutearly)
    r = testTree(depth - 1, cutearly)
    return TreeNode(random.randint(0, 100), l, r)

def printTree(node, prefix=''):
    if node == None:
        return
    printTree(node.left, prefix + '    ')
    print(prefix + str(node.value))
    printTree(node.right, prefix + '    ')

def printTreePreorder(node, prefix='    '):
    if node == None:
        return

    print(prefix[:-4] + '+-- ' + str(node.value))

    if node.left != None:
        print(prefix + '|')
        printTreePreorder(node.left, prefix + '|   ' if node.right != None else prefix + '    ')

    if node.right != None:
        print(prefix + '|')
        printTreePreorder(node.right, prefix + '    ')

def printTreeInorder(node, leftPrefix='    ', rightPrefix='    '):
    if node == None:
        return

    if node.left != None:
        printTreeInorder(node.left, leftPrefix + '    ', leftPrefix + '|   ')
        print(leftPrefix + '|')

    print(leftPrefix[:-4] + '+-- ' + str(node.value))

    if node.right != None:
        print(rightPrefix + '|')
        printTreeInorder(node.right, rightPrefix + '|   ', rightPrefix + '    ')

def depthFirst(root):
    stack = [root]
    while len(stack) > 0:
        n = stack.pop()
        if n != None:
            print(n.value)
            stack.append(n.left)
            stack.append(n.right)

def breadthFirst(root):
    queue = [root]
    while len(queue) > 0:
        n = queue.pop(0)
        if n != None:
            print(n.value)
            queue.append(n.right)
            queue.append(n.left)

def layer(node, n):
    if node == None:
        return []
    if n == 0:
        return [node.value]

    return layer(node.left, n - 1) + layer(node.right, n - 1)

def cut(node, n):
    if node == None:
        return None
    if n == 0:
        return None

    node.left = cut(node.left, n - 1)
    node.right = cut(node.right, n - 1)
    return node

def fill(node, val, n):
    if node == None and n <= 0:
        return None

    if node == None:
        node = TreeNode(val)
    node.left = fill(node.left, val, n - 1)
    node.right = fill(node.right, val, n - 1)
    return node

def removeLeft(node):
    if node == None:
        return None
    if node.left == None:
        return node.right

    node.left = removeLeft(node.left)
    return node

######

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'<{self.x}, {self.y}>'

class Maze:
    def __init__(self, tiles, start, end):
        self.tiles = []
        for line in tiles:
            l = []
            for tile in line:
                l.append(0 if tile == ' ' else -1)
            self.tiles.append(l)

        self.start = start
        self.end = end

    def getAt(self, pos):
        return self.tiles[pos.x][pos.y]

    def setAt(self, pos, value):
        self.tiles[pos.x][pos.y] = value

    def reset(self):
        for x, line in enumerate(self.tiles):
            for y, tile in enumerate(line):
                pos = Position(x, y)
                if self.getAt(pos) > 0:
                    self.setAt(pos, 0)

    def printTile(self, tile, onPath=False):
        c = ''
        if onPath:
            c = '#'
        elif tile == -1:
            c = '█'
        elif tile == 0:
            c = ' '
        else:
            c = '.'
        print(c, end='')

    def neighbours(self, pos):
        return [pos + Position(dx, dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    def print(self, path=None):
        if path == None:
            path = set()

        for x, line in enumerate(self.tiles):
            for y, tile in enumerate(line):
                self.printTile(tile, Position(x, y) in path)
            print()

    def available(self, pos):
        result = []
        for candidate in self.neighbours(pos):
            if self.getAt(candidate) == 0:
                result.append(candidate)
        return result

    def best(self, pos):
        min = math.inf
        minPos = None
        found = False
        for candidate in self.neighbours(pos):
            val = self.getAt(candidate)
            if val > 0 and val < min:
                min = val
                minPos = candidate
                found = True
        return (min if found else 0, minPos)

    def dfsearch(self):
        stack = [self.start]
        while len(stack) > 0:
            pos = stack.pop()
            b, _ = self.best(pos)
            self.setAt(pos, b + 1)
            # self.print(set(self.path(pos)))
            if pos == self.end:
                return

            stack += self.available(pos)

    def bfsearch(self):
        queue = [self.start]
        while len(queue) > 0:
            pos = queue.pop(0)
            b, _ = self.best(pos)
            self.setAt(pos, b + 1)
            # self.print(set(self.path(pos)))
            if pos == self.end:
                return

            queue += self.available(pos)

    def path(self, pos=None):
        if pos == None:
            pos = self.end
        result = []
        while pos != None and pos != self.start:
            result.append(pos)
            _, pos = self.best(pos)
        if pos == self.start:
            result.append(self.start)
        return result

maze = Maze(
    [list(x) for x in [
        '███████████',
        '█ █  ██   █',
        '█ █ ██  █ █',
        '█ █    ██ █',
        '█   ████  █',
        '█ █ ██ █ ██',
        '█ █    █  █',
        '█ ███████ █',
        '█ █   █ █ █',
        '█   █   █ █',
        '███████████',
    ]], Position(1, 1), Position(9, 9))

bigMaze = Maze(
    [list(x) for x in [
        '█████████████████████████████████████████████████████████████',
        '█         █       █     █     █   █ █     █   █             █',
        '█ ███ █ █ █ █ █████ ███ ███ █ ███ █ ███ ███ ███ █ ███████ █ █',
        '█   █ █ █ █ █     █ █       █       █       █ █ █ █   █   █ █',
        '█ █ █████████████ ███████ █████ ███ █████ █ █ ███ ███ █████ █',
        '█ █ █ █             █         █   █ █     █   █ █ █   █     █',
        '███ █ ███ ███ ███ █████████████ █ █████████ ███ ███ ███████ █',
        '█     █ █ █   █ █ █     █   █   █ █   █ █ █   █   █   █     █',
        '███ ███ ███ █ █ █ ███ █████ █████ ███ █ █ █ █████ ███ █████ █',
        '█ █ █     █ █   █ █       █             █         █ █     █ █',
        '█ █ █████ █ ███ █████ █ █ █ ███ ███████ █ █████████ █ ███ █ █',
        '█ █ █ █       █   █   █ █ █ █ █ █   █               █ █   █ █',
        '█ █ █ █ ███ █ ███████ █ ███ █ █ █ ███ ███████ █ █ ███ ███ █ █',
        '█ █ █   █   █ █       █ █   █       █   █     █ █       █   █',
        '█ █ █ █ ███ █ █████████ █████ █████ ███ ███ █████ ███ █████ █',
        '█ █   █ █ █ █ █     █ █       █       █   █     █   █     █ █',
        '█ █████ █ █ █ ███ ███ █ █ █ █ █████ ███ █████████████ ███████',
        '█       █ █ █ █         █ █ █ █ █     █ █ █ █ █ █       █   █',
        '███ █ ███ ███ ███████ █████ ███ ███ ███ █ █ █ █ █████ █████ █',
        '█   █       █   █ █       █ █         █     █       █   █   █',
        '█ ███ ███████████ █ █ ███ █████ ███ ███████ ███ █ █ █ █████ █',
        '█ █       █     █   █ █     █   █       █     █ █ █     █ █ █',
        '█ ███ █ ███████ ███ █ █████████ █ █████ ███████ █ ███████ █ █',
        '█ █   █ █   █ █   █ █ █   █ █   █ █       █   █ █     █     █',
        '███ █ █████ █ █ █████ ███ █ ███████ █████ █ █ █████ ███████ █',
        '█   █   █ █   █   █ █       █ █ █   █ █ █ █ █ █         █   █',
        '█ █████ █ █ ███ ███ █ █ █████ █ ███ █ █ █████ █ ███████ ███ █',
        '█ █   █     █   █ █   █     █   █             █   █ █ █ █   █',
        '█ █ ███ ███ █ ███ █ ███ ███ ███ █████ ███ █████████ █ █ █ █ █',
        '█   █   █ █ █ █ █ █ █   █ █       █     █     █ █ █       █ █',
        '█████ ███ █ █ █ █ ███ ███ ███████ █████ ███ ███ █ █ █ █ █████',
        '█       █ █ █   █   █       █     █     █ █   █   █ █ █     █',
        '█ ███ █ █ █ █ █ ███ █ █ █ ███ █ █████ ███ █ ███ ███████ ███ █',
        '█   █ █   █   █ █     █ █ █ █ █ █   █ █           █   █   █ █',
        '█████ ███ █ █ ███████ █ ███ █ ███ █████ ███ █ █ █ ███ █████ █',
        '█ █   █   █ █ █     █ █     █     █     █   █ █ █   █     █ █',
        '█ █████ █ █ ███ █████ ███████████████████ ███████ █ ███ █ █ █',
        '█     █ █ █     █         █ █               █     █     █ █ █',
        '███ █ █████ ███████ █ █ ███ █████████ █ █ █████████████ █████',
        '█   █ █ █         █ █ █     █       █ █ █     █ █ █ █   █   █',
        '█ ███ █ █████████ ███████ █ ███ ███ █ █████ ███ █ █ █ ███ ███',
        '█   █ █   █   █ █ █     █ █ █     █ █   █     █   █ █ █   █ █',
        '███ ███ ███ █ █ █ ███ ███████ █████ █ █████ ███ █ █ █ █ ███ █',
        '█       █   █ █ █     █     █ █ █ █   █ █   █   █     █     █',
        '█ █████ █████ █ ███ █ █ ███ ███ █ █ ███ ███████ █████████ █ █',
        '█ █ █     █       █ █     █     █   █       █   █ █       █ █',
        '█ █ ███ █████ █ █ ███ ███ █ █ ███ ███████ █████ █ █ ███ █ █ █',
        '█   █         █ █   █ █   █ █   █ █       █ █   █   █ █ █ █ █',
        '█ █ █ ███ █████ █████████ █ ███████ █████ █ █ █ ███ █ █ █ ███',
        '█ █ █   █ █               █ █   █     █ █ █   █ █ █ █ █ █   █',
        '███ █████████████████ ███ █ ███ █████ █ ███ █████ █ █ ███ ███',
        '█       █       █   █ █ █ █   █ █       █         █   █ █   █',
        '█ █ █████ ███████ █ █ █ ███████ █████ █████ █████ ███ █ █ █ █',
        '█ █ █     █       █ █   █     █     █     █   █         █ █ █',
        '█ ███ ███ █████ ███ █ █████ ███████ █████ █ ███████ █ ███████',
        '█   █   █     █ █ █ █     █ █ █       █           █ █     █ █',
        '█████████ █ ███ █ █ █ ███ █ █ █ ███ █████ █ █████ █ █ █ █ █ █',
        '█         █   █   █ █   █ █ █   █   █ █ █ █ █   █ █ █ █ █   █',
        '█ █████ █████ █████ █████ █ █ █████ █ █ █ █ ███ █ █ █ █████ █',
        '█     █     █                   █         █ █     █ █ █     █',
        '█████████████████████████████████████████████████████████████',
    ]], Position(1, 1), Position(59, 59))
