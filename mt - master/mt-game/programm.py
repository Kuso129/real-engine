from map import*
from menu import Menu
from first_person_camera import*
import rtime as rt
import screen as sc
from dplayer import*
from utils import*
import pygame as pg
from model import*
from eventor import*
from gl_view import*

class Programm:
    def __init__(self):
        pg.init()
        sc.set_res(1280, 720, False)
        pg.display.set_icon(pg.image.load('resources/0.png').convert_alpha())

    def create_scene(self):
        self.is_menu = True
        self.menu = Menu(self)
        self.camera = DBasePlayer(self)
        self.map_1 = Map([load_model('resources/maps/terrain09.obj', 'resources/scripts/terrain.mtpy'),
                          load_model('resources/models/sky 823.obj', 'resources/scripts/sky_8.mtpy')], [self.camera], self.camera, self)
        curent_map = self.map_1
        print(all_entitys.keys())


    def init(self):
        curent_programm = self
        self.set_game_menu(False)
        init_render()

    def loop(self):
        if self.is_menu:
            self.menu.action()
        else:
            self.map_1.action()

    def set_game_menu(self, is_m):
        self.is_menu = is_m
        pg.mouse.set_visible(is_m)
        if not self.is_menu:
            self.map_1.start()


    def run(self):
        self.create_scene()
        self.init()
        while True:
            for i in pg.event.get():
                i_despatch_events(i)

            glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
            self.loop()
            pg.display.flip()
            rt.tick()
            pg.display.set_caption(f'FPS: {int(rt.get_fps())} X: {self.camera.position[0]} Y: {self.camera.position[1]} Z: {self.camera.position[2]}.')

