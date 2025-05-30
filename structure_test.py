from vpython import rate, vec, canvas, color
from structures import Vertex, Edge

scene = canvas()

#2x2 grid
vertices = [
    Vertex(vec(x, 0, z), 1.0, fixed=(x==0 or x==1))
    for z in range(2) for x in range(2)
]

edges = [
    Edge(vertices[0], vertices[1]),
    Edge(vertices[0], vertices[2]),
    Edge(vertices[1], vertices[3]),
    Edge(vertices[2], vertices[3]),
    Edge(vertices[0], vertices[3])  #diagonal spring
]

dt = 0.01
g = vec(0, -9.8, 0)

