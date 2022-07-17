from model import*
from gl_view import*

class modelRenderer:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera

        self.filter = self.model.material[2]
        self.tex = load_image(self.model.material[0], self.filter)
        self.color = self.model.material[1]

    def draw(self):
        if self.model != None:
            vertices = self.model.c_vertex @ self.camera.camera_matrix()
            vertices = vertices @ self.camera.projection.projection_matrix
            glBindTexture(GL_TEXTURE_2D, self.tex)
            draw_mesh_ev(self.model.element_buffer, vertices, self.model.lenv, self.model.c_vertex, self.model.normals, self.model.uv)
            glBindTexture(GL_TEXTURE_2D, 0)
