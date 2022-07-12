from OpenGL.GL import *
import pygame as pg
import numpy as np


def draw_mesh_ev(edges, verticies, lene, stock_vertex, normals, uv):
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)

    glVertexPointer(4, GL_FLOAT, 0, verticies)
    glNormalPointer(GL_FLOAT, 0, normals)
    glTexCoordPointer(2, GL_FLOAT, 0, uv)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, edges)
    glDrawElements(GL_TRIANGLES, lene, GL_UNSIGNED_INT, None)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glDisableClientState(GL_NORMAL_ARRAY)


def load_image(path):
    image = pg.image.load(path).convert_alpha()
    arr = np.array(pg.surfarray.pixels3d(image))
    p_arr = pg.PixelArray(image)
    # arr = p_arr.
    data = np.array(arr / 255)

    width = image.get_width()
    height = image.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA , GL_UNSIGNED_BYTE, data)
    glBindTexture(GL_TEXTURE_2D, 0)

    return texture

def draw_rect(pos, size):
    verticies = np.array([
        [pos[0], pos[1]],
        [pos[0] + size[0], pos[1]],
        [pos[0] + size[0], pos[1] + size[1]],
        [pos[0], pos[1] + size[1]]
    ])

    glBegin(GL_TRIANGLE_FAN)
    glVertex2fv(verticies[0])
    glVertex2fv(verticies[1])
    glVertex2fv(verticies[2])
    glVertex2fv(verticies[3])
    glEnd()



