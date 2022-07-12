import pygame.mouse as pgm
from drawing.gl_view import*

class Button:
    def __init__(self, size, pos):
        self.size = size
        self.pos = pos

    def get_pressed(self):
        return self.get_overlap() and pgm.get_pressed(3)

    def get_overlap(self):
        return self.pos[0] < pgm.get_pos()[0] + self.size[0] and self.pos[1] < pgm.get_pos()[1] + self.size[1]

    def draw(self):
        r_size = [10 / self.size[0], 10 / self.size[1]]
        r_pos = [10 / self.pos[0], 10 / self.pos[1]]
        draw_rect(r_pos, r_size)


