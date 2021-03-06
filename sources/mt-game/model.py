#
# Written by: Ivan Solovyov.
#
# Summary:
# This is a refactor of this author's code: "https://www.youtube.com/watch?v=Scn96t7mwC4&t=775s".
#
# The difference is that the rendering of the object is now done by the graphics card, not the processor.
# And also removed the elements on the little things.
# Also, the function for loading an object through a .obj file has been moved from the main file here.
#
# Summary:
# When writing the code responsible for drawing the object, certain difficulties arose.
#
# Python types clashed with types accepted by opengl.
#
# Therefore, I decided to use ebo, and write indexes to the video card. There have been no problems with this. Indexes are written in the init() procedure.
#
from pmath import *
from gl_view import*
from read_materials import*


class model:
    def __init__(self, vertices='', faces='', normals='', uv='', mat=''):
        self.vertices = np.array([np.array(v) for v in vertices])
        self.normals = np.array([np.array(n) for n in normals])
        self.uv = np.array([np.array(u) for u in uv])
        self.faces = np.array([np.array(face) for face in faces])
        self.c_vertex = self.vertices
        self.material = read_material(mat)
        self.init()

    def init(self):
        self.lenv = int(len(self.faces) * 3)
        self.element_buffer = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.element_buffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.faces.nbytes, self.faces, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def translate(self, pos):
        self.c_vertex = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)


def load_model(filename, mat='resources/scripts/def_mat.mtpy'):
    vertex, faces, uv, normals = [], [], [], []
    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]] + [1])
            elif line.startswith('f'):
                faces_ = line.split()[1:]
                faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
            elif line.startswith('vt '):
                uv.append([float(i) for i in line.split()[1:]])
            elif line.startswith('vn '):
                normals.append([float(i) for i in line.split()[1:]])
    mesh = model(vertex, faces, normals, uv, mat)
    return mesh
