import time
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        #for i in range(self.V):
            #print((i, dist[i]))

    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles.  The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print ("Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(dist)


g = Graph(1000)

import random

nodeCount = 999
vertexCount = 499500

vertices = {}
while len(vertices) < vertexCount:
    x = random.randint (0, nodeCount)
    y = random.randint (0, nodeCount)
    if x == y: continue
    #comment the following line if the graph is directed
    if y < x: x, y = y, x
    w = random.randint(1,100)
    vertices [x, y] = w
#just for debug

for (x, y), w in vertices.items():
    #print (x,y,w)
    g.addEdge(x, y, w)

# Print the solution
start_time = time.time()
g.BellmanFord(0)
print ("time elapsed: {:.8f}s".format(time.time() - start_time))