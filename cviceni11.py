import math

rawString = """
            7
            8
            0 1 1
            0 2 5
            0 3 3
            1 3 3
            3 4 2
            4 5 1
            4 6 3
            5 6 4
            """

graphList = [int(x) for x in rawString.split()]

def loadAsMatrix(list):
    v, e, *edges = list
    matrix = [[0] * v for _ in range(v)]
    for i in range(0, 3 * e, 3):
        matrix[edges[i]][edges[i + 1]] = 1
        matrix[edges[i + 1]][edges[i]] = 1
    for line in matrix:
        print(*line)
    return matrix

def loadAsWeightedMatrix(list):
    v, e, *edges = list
    matrix = [[math.inf] * v for _ in range(v)]
    for i in range(0, 3 * e, 3):
        matrix[edges[i]][edges[i + 1]] = edges[i + 2]
        matrix[edges[i + 1]][edges[i]] = edges[i + 2]
    for line in matrix:
        print(*line)
    return matrix

def loadAsNeighborsList(list):
    v, e, *edges = list
    neighbors = [[] for _ in range(v)]
    for i in range(0, 3 * e, 3):
        neighbors[edges[i]].append(edges[i + 1])
        neighbors[edges[i + 1]].append(edges[i])
    for n in neighbors:
        print(*n)
    return neighbors

def loadAsWeightedNeighborsList(list):
    v, e, *edges = list
    neighbors = [[] for _ in range(v)]
    for i in range(0, 3 * e, 3):
        neighbors[edges[i]].append((edges[i + 1], edges[i + 2]))
        neighbors[edges[i + 1]].append((edges[i], edges[i + 2]))
    for n in neighbors:
        print(*n)
    return neighbors

class Node:
    def __init__(self, ix):
        self.index = ix
        self.neighbors = []

    def __repr__(self):
        return str(self.index)

def loadAsNodes(list):
    v, e, *edges = list
    nodes = [Node(i) for i in range(v)]
    for i in range(0, 3 * e, 3):
        nodes[edges[i]].neighbors.append(nodes[edges[i + 1]])
        nodes[edges[i + 1]].neighbors.append(nodes[edges[i]])
    for n in nodes:
        print(n.index, n.neighbors)
    return nodes

def loadAsWeightedNodes(list):
    v, e, *edges = list
    nodes = [Node(i) for i in range(v)]
    for i in range(0, 3 * e, 3):
        nodes[edges[i]].neighbors.append((nodes[edges[i + 1]], edges[i + 2]))
        nodes[edges[i + 1]].neighbors.append((nodes[edges[i]], edges[i + 2]))
    for n in nodes:
        print(n.index, n.neighbors)
    return nodes
