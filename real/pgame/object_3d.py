from pmath import *
from gl_view import*

class Model:
    def __init__(self, render, vertices='', faces=''):
        self.render = render
        self.vertices = np.array([np.array(v) for v in vertices])
        self.faces = np.array([np.array(face) for face in faces])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        draw_mesh_ev(self.element_buffer, vertices, self.lenv, self.vertices)

    def init(self):
        self.lenv = int(len(self.faces) * 3)
        self.element_buffer = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.element_buffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.faces.nbytes, self.faces, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)


def load_model(render, filename):
    vertex, faces = [], []
    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]] + [1])
            elif line.startswith('f'):
                faces_ = line.split()[1:]
                faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
    return Model(render, vertex, faces)
