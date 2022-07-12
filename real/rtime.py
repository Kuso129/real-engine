import pygame as pg

c_clock = pg.time.Clock()
target_frameraate = 60
delta_time = 1

def tick():
    c_clock.tick(target_frameraate)

def get_fps():
    return c_clock.get_fps()

def get_delta_time():
    fps = get_fps()
    d_time = 0
    if fps != 0:
        d_time = 1 / get_fps()

    if d_time != 0:
        return d_time
    else:
        return 1

