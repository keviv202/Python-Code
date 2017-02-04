import time
from collections import defaultdict


class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.distances[(to_node, from_node)] = distance
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


g = Graph()
n=1000
for i in range (0,n):
    g.add_node(i)


#g.add_edge('a', 'b', 10)
#g.add_edge('b', 'c', 10)
#g.add_edge('a', 'c', 15)
#g.add_edge('c', 'd', 20)

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
    g.add_edge(x,y,w)
start_time = time.time()
(dijsktra(g, 0))
print ("time elapsed: {:.8f}s".format(time.time() - start_time))