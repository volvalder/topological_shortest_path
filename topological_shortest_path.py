class Graph:
    def __init__(self, vertices):
        self.adjList = {}
        self.q = []
        for u,v,w in vertices:
            self.addNodes([u,v])
            self.addEdge(u, [w,u,v])
        self.distTo = [float('inf') for v in range(len(self.adjList))]
        self.edgeTo = [None] * len(self.adjList)

    def addNodes(self, n):
        for v in n:
            if v not in self.adjList:
                self.adjList[v] = []

    def addEdge(self, n, e):
        self.adjList[n].append(e)

    def relax(self, vertice):
        w,u,v = vertice
        if self.distTo[v] > self.distTo[u] + w:
            self.distTo[v] = self.distTo[u] + w
            self.edgeTo[v] = vertice[1]

    def topological(self, vertice, visited=set()):
        visited.add(vertice)
        for v in self.adjList[vertice]:
            if v[2] not in visited:
                self.topological(v[2], visited)
            self.q.append(v)

    def printResult(self):
        for i in range(len(self.distTo)):
            print(f"Path {self.edgeTo[i]} => {i} distance: {self.distTo[i]}")

    def dijkstra(self, source):
        self.distTo[source] = 0
        for v in self.q:
            for vert in self.adjList[v[1]]:
                self.relax(vert)
