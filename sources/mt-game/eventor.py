import pygame as pg

def i_despatch_events(i):
    match i.type:
        case pg.QUIT:
            exit(0)
        case pg.K_ESCAPE:
            exit(0)
