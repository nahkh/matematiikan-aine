class Graph:
    def __init__(self, filename, directed=False):
        self.nodes = []
        self.edges = set()
        self.neighbors = {}
        with open(filename) as f:
            for line in f.readlines():
                a, b = line.strip('\n').split(' ')
                if a not in self.nodes:
                    self.nodes.append(a)
                if b not in self.nodes:
                    self.nodes.append(b)
                self.addEdge(a, b)
                if not directed:
                    self.addEdge(b, a)

    def addEdge(self, a, b):
        self.edges.add((a, b))
        if a not in self.neighbors:
            self.neighbors[a] = set()
        self.neighbors[a].add(b)

    def getVertices(self):
        return self.nodes

    def getNeighbors(self, a):
        return self.neighbors[a] if a in self.neighbors else set()

    def areConnected(self, a, b):
        return (a, b) in self.edges



    
        
