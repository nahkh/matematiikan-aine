from group import Group
from mapping import Mapping
from itertools import permutations

def factorial(vertices):
    i = 1
    for v in range(2, len(vertices) + 1):
        i = i * v
    return i

def findAutomorphisms(graph):
    '''Trivial automorhism scanner. O(n!) runtime'''
    automorphisms = []
    originalVertices = graph.getVertices()
    expectedRounds = factorial(originalVertices)
    print(expectedRounds)
    for permutation in permutations(originalVertices):
        mapping = Mapping(originalVertices, permutation)
        isAutomorphism = True
        for vertex in originalVertices:
            mappedNeighbors = set(map(mapping, graph.getNeighbors(vertex)))
            if mappedNeighbors != graph.getNeighbors(mapping[vertex]):
                isAutomorphism = False
                break
                
        if isAutomorphism:
            automorphisms.append(mapping)
            
    return automorphisms



def getSymmetryGroup(graph, namingStrategy=None):
    elements = findAutomorphisms(graph)
    return Group(elements, lambda x, y: x.merge(y), namingStrategy)
    
