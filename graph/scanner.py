from graph import Graph
from graph_automorphism_group import getSymmetryGroup

if __name__ == '__main__':
    graph = Graph('graph5.txt')
    group = getSymmetryGroup(graph)

    for line in group.getTable():
        print(line)
    
