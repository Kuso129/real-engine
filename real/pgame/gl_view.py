from OpenGL.GL import *

def draw_mesh_ev(edges, verticies, lene, stock_vertex):
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, edges)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)

    glVertexPointer(4, GL_FLOAT, 0, verticies)
    glNormalPointer(GL_FLOAT, 0, stock_vertex)
    glDrawElements(GL_TRIANGLES, lene, GL_UNSIGNED_INT, None)

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_NORMAL_ARRAY)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)



