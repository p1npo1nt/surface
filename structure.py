#defining the structure of shapes
#vertex and edge, edges posess spring constants k
from vpython import vec, sphere, cylinder, color

class Vertex:
    def __init__(self, pos, mass, fixed=False):
        self.pos = pos
        self.vel = vec(0, 0, 0)
        self.force = vec(0, 0, 0)
        self.mass = mass
        self.fixed = fixed
        self.visual = sphere(pos=pos, radius=0.1, color=color.white)

    def update_visual(self):
        self.visual.pos = self.pos

class Edge:
    def __init__(self, v1, v2, k=50, damping=0.2):
        self.v1 = v1
        self.v2 = v2
        self.k = k
        self.damping = damping #apply damping constant
        self.L0 = mag(v1.pos - v2.pos)
        self.visual = cylinder(pos=v1.pos, axis=v2.pos - v1.pos, radius=0.03, color=color.gray(0.5))

    def apply_force(self):
        delta = self.v2.pos - self.v1.pos
        dist = mag(delta)
        direction = delta.norm()
        spring_force = self.k * (dist - self.L0) * direction

        #damping force
        relative_velocity = self.v2.vel - self.v1.vel
        damping_force = self.damping * relative_velocity.dot(direction) * direction

        total_force = spring_force + damping_force

        #equal and opposite forces
        if not self.v1.fixed:
            self.v1.force += total_force
        if not self.v2.fixed:
            self.v2.force -= total_force

    def update_visual(self):
        self.visual.pos = self.v1.pos
        self.visual.axis = self.v2.pos - self.v1.pos

