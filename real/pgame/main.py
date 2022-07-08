import pygame as pg
from camera import Camera
from projection import Projection
from object_3d import*

class Programm:
    def __init__(self):
        pg.init()
        self.res = [self.WIDTH, self.HEIGHT] = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH / 2, self.HEIGHT / 2
        self.screen = pg.display.set_mode(self.res, pg.DOUBLEBUF | pg.OPENGL)
        self.clock = pg.time.Clock()

        self.camera = Camera(self, [0,1.25,-25])
        self.projection = Projection(self)
        self.map = load_model(self, 'resources/map_2.obj')
        self.sky = load_model(self, 'resources/cube.obj')
        self.sky.scale(32)

        self.init()
        self.run()

    def init(self):
        glEnable(GL_DEPTH_TEST)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)

    def loop(self):
        self.camera.control()
        self.map.draw()
        self.sky.draw()

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
