import pygame as pg

c_screen = None
width = 1024
height = 768
h_width = width / 2
h_height = height / 2
title = ''
is_fullscreen = False

def set_res(width, height, is_fullsc):
    is_fullscreen = is_fullsc
    width = width
    height = height
    h_width = width / 2
    h_height = height / 2
    if is_fullscreen:
        c_screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.OPENGL | pg.FULLSCREEN)
    else:
        c_screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.OPENGL)

def set_tittle(title):
    title = title
    pg.display.set_caption(title)

