import random

nodeCount = 4
vertexCount = 6

vertices = {}
while len(vertices) < vertexCount:
    x = random.randint (1, nodeCount)
    y = random.randint (1, nodeCount)
    if x == y: continue
    #comment the following line if the graph is directed
    if y < x: x, y = y, x
    w = random.randint(1,10)
    vertices [x, y] = w
#just for debug

for (x, y), w in vertices.items():
    print ((x, y, w))