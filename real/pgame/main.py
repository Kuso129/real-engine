import pygame as pg
from camera import Camera
from projection import Projection
from weapons import*

class Programm:
    def __init__(self):
        pg.init()
        self.res = [self.WIDTH, self.HEIGHT] = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH / 2, self.HEIGHT / 2
        self.screen = pg.display.set_mode(self.res, pg.DOUBLEBUF | pg.OPENGL)
        self.clock = pg.time.Clock()

        pg.mouse.set_visible(False)
        self.create_scene()
        self.init()
        self.run()

    def create_scene(self):
        self.camera = Camera(self, [0,1.25,-8])
        self.projection = Projection(self)
        self.map = load_model(self, 'resources/map_2.obj')
        self.sky = load_model(self, 'resources/cube.obj')
        self.weapon = WpVityaz(self, 'resources/w_vityaz.obj')
        self.sky.scale(32)

    def init(self):
        glEnable(GL_DEPTH_TEST)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)

    def loop(self):
        self.camera.control()

        glColor3f(1,1,1)
        self.map.draw()
        glColor3f(0, 0.75, 1)
        self.sky.draw()

        # glColor3f(0.25,0.25,0.26)
        # self.weapon.model.translate(get_weapon_pos(self.camera.position))
        # self.weapon.model.rotate_y(self.camera.position[1])
        # print(self.camera.position)
        # print(f'weapon pos: {get_weapon_pos(self.camera.position)}')
        # self.weapon.model.draw()

    def run(self):
        while True:
            for i in pg.event.get():
                match i.type:
                    case pg.QUIT:
                        exit(0)
                    case pg.K_ESCAPE:
                        exit(0)

            glClear(GL_DEPTH_BUFFER_BIT)
            self.loop()
            pg.display.flip()
            self.clock.tick()
            pg.display.set_caption(f'FPS: {int(self.clock.get_fps())}.')


if __name__ == '__main__':
    prog = Programm()
