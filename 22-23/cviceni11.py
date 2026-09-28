import math

undirGraph1 = \
   [7, 8,
    0, 1,
    0, 2,
    0, 3,
    1, 3,
    3, 4,
    4, 5,
    4, 6,
    5, 6]

undirGraph2 = \
   [9, 8,
    0, 1,
    1, 2,
    2, 3,
    3, 4,
    3, 5,
    2, 6,
    1, 7,
    7, 8]

dirGraph1 = \
    [4, 4,
     0, 1,
     1, 2,
     2, 3,
     3, 0]

dirGraph2 = \
    [4, 4,
     0, 1,
     0, 2,
     1, 3,
     2, 3]

def loadAsMatrix(list, sym=True):
    v, e, *edges = list
    matrix = [[0] * v for _ in range(v)]
    for i in range(0, 2 * e, 2):
        matrix[edges[i]][edges[i + 1]] = 1
        if sym: matrix[edges[i + 1]][edges[i]] = 1
    for line in matrix:
        print(*line)
    return matrix

def loadAsNeighborsList(list, sym=True):
    v, e, *edges = list
    neighbors = [[] for _ in range(v)]
    for i in range(0, 2 * e, 2):
        neighbors[edges[i]].append(edges[i + 1])
        if sym: neighbors[edges[i + 1]].append(edges[i])
    for n in neighbors:
        print(*n)
    return neighbors

class Node:
    def __init__(self, ix):
        self.index = ix
        self.neighbors = []

    def __repr__(self):
        return str(self.index)

def loadAsNodes(list, sym=True):
    v, e, *edges = list
    nodes = [Node(i) for i in range(v)]
    for i in range(0, 2 * e, 2):
        nodes[edges[i]].neighbors.append(nodes[edges[i + 1]])
        if sym: nodes[edges[i + 1]].neighbors.append(nodes[edges[i]])
    for n in nodes:
        print(n.index, n.neighbors)
    return nodes

# Pro následující funkce budeme používat seznam sousedů.

def undirConnected(graph):
    visited = [False for _ in graph]
    def dfs(vertex):
        nonlocal visited
        if visited[vertex]:
            return
        visited[vertex] = True
        for next in graph[vertex]:
            dfs(next)
    dfs(0)
    for v in visited:
        if not v: return False
    return True

# Pro jednoduchost v následujících "undir" funkcích předpokládáme, že je graf souvislý.

def undirCyclic(graph):
    visited = [False for _ in graph]
    stack = [(0, None)]
    while len(stack) > 0:
        vertex, parent = stack.pop()
        if visited[vertex]:
            return True
        visited[vertex] = True
        for next in graph[vertex]:
            if parent != next:
                stack.append((next, vertex))
    return False

def undirFurthest(graph, begin=0):
    bestVertex = -1
    bestDistance = -1

    visited = [False for _ in graph]
    queue = [(begin, 0)]
    while len(queue) > 0:
        vertex, distance = queue.pop(0)
        if visited[vertex]:
            continue
        visited[vertex] = True
        if distance > bestDistance:
            bestVertex = vertex
            bestDistance = distance
        for next in graph[vertex]:
            queue.append((next, distance + 1))

    return (bestVertex, bestDistance)

def undirLongestPath(graph):
    start, _ = undirFurthest(graph)
    end, _ = undirFurthest(graph, start)
    return (start, end)

def undirPath(graph, begin, end):
    prevs = [None for _ in graph]
    visited = [False for _ in graph]
    queue = [(begin, None)]
    while len(queue) > 0:
        vertex, prev = queue.pop(0)
        if visited[vertex]:
            continue
        visited[vertex] = True
        if prevs[vertex] == None:
            prevs[vertex] = prev
        for next in graph[vertex]:
            queue.append((next, vertex))

    if prevs[end] == None:
        return None
    else:
        path = []
        vertex = end
        while vertex != None:
            path.append(vertex)
            vertex = prevs[vertex]
        return path

def dirCyclicRec(graph):
    active = [False for _ in graph]
    explored = [False for _ in graph]

    def dfs(vertex):
        nonlocal active, explored
        if explored[vertex]:
            return False
        if active[vertex]:
            return True
        active[vertex] = True
        cycle = False
        for next in graph[vertex]:
            cycle = cycle or dfs(next)
        active[vertex] = False
        explored[vertex] = True
        return cycle

    for start in range(len(graph)):
        if explored[start]:
            continue
        if dfs(start):
            return True
    return False

def dirCyclic(graph):
    active = [False for _ in graph]
    explored = [False for _ in graph]
    for start in range(len(graph)):
        if explored[start]:
            continue
        stack = [(start, True)]
        while len(stack) > 0:
            vertex, first = stack.pop()
            if first:
                if explored[vertex]:
                    continue
                if active[vertex]:
                    return True
                active[vertex] = True
                stack.append((vertex, False))
                for next in graph[vertex]:
                    stack.append((next, True))
            else:
                active[vertex] = False
                explored[vertex] = True
    return False

def dirTopologicalSort(graph):
    active = [False for _ in graph]
    explored = [False for _ in graph]
    topo = []
    for start in range(len(graph)):
        if explored[start]:
            continue
        stack = [(start, True)]
        while len(stack) > 0:
            vertex, first = stack.pop()
            if first:
                if explored[vertex]:
                    continue
                if active[vertex]:
                    return None
                active[vertex] = True
                stack.append((vertex, False))
                for next in graph[vertex]:
                    stack.append((next, True))
            else:
                active[vertex] = False
                explored[vertex] = True
                topo.append(vertex)
    return topo
