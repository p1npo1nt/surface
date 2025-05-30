#defining the structure of shapes
#vertex and edge, edges posess spring constants k
class Vertex:
    def __init__(self, pos, mass, fixed=False):
        self.pos = pos
        self.vel = vec(0,0,0)
        self.force = vec(0,0,0)
        self.mass = mass
        self.fixed = fixed
        self.visual = sphere(pos=pos, radius=0.1, color=color.white)

class Edge:
    def __init__(self, v1, v2, k, rest_length):
        self.v1 = v1
        self.v2 = v2
        self.k = k
        self.L0 = rest_length
        self.visual = cylinder(pos=v1.pos, axis=v2.pos - v1.pos, radius=0.03, color=color.gray(0.5))
