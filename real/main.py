from map import*
from menu import Menu
from first_person_camera import*
import rtime as rt
import screen as sc
from dplayer import*
from utils import*

class Programm:
    def __init__(self):
        pg.init()
        sc.set_res(1024, 768, False)
        pg.display.set_icon(pg.image.load('resources/0.png').convert_alpha())

        self.create_scene()
        self.init()
        self.run()

    def create_scene(self):
        self.is_menu = True
        self.menu = Menu(self)
        self.camera = DBasePlayer(self)
        self.map_1 = Map([load_model(self, 'resources/maps/d0b1', 'None')], [self.camera], self)
        curent_map = self.map_1
        print(all_entitys.keys())


    def init(self):
        curent_programm = self
        self.set_game_menu(False)
        glEnable(GL_DEPTH_TEST)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)

        glEnable(GL_TEXTURE_2D)

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
        while True:
            for i in pg.event.get():
                match i.type:
                    case pg.QUIT:
                        exit(0)
                    case pg.K_ESCAPE:
                        exit(0)

            glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
            self.loop()
            pg.display.flip()
            rt.tick()
            pg.display.set_caption(f'FPS: {int(rt.get_fps())} X: {self.camera.position[0]} Y: {self.camera.position[1]} Z: {self.camera.position[2]}.')


if __name__ == '__main__':
    prog = Programm()
