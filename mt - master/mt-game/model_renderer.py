from model import*
from gl_view import*

class modelRenderer:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera
        self.tex = load_image('resources/0.png', False)

    def draw(self):
        vertices = self.model.c_vertex @ self.camera.camera_matrix()
        vertices = vertices @ self.camera.projection.projection_matrix
        glBindTexture(GL_TEXTURE_2D, self.tex)
        draw_mesh_ev(self.model.element_buffer, vertices, self.model.lenv, self.model.c_vertex, self.model.normals, self.model.uv)
        glBindTexture(GL_TEXTURE_2D, 0)
