from camera import Camera
from projection import Projection
from weapons import*
from map import*
from menu import Menu

class Programm:
    def __init__(self):
        pg.init()
        self.res = [self.WIDTH, self.HEIGHT] = 1280, 720
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH / 2, self.HEIGHT / 2
        self.screen = pg.display.set_mode(self.res, pg.DOUBLEBUF | pg.OPENGL)
        self.clock = pg.time.Clock()

        self.create_scene()
        self.init()
        self.run()

    def create_scene(self):
        self.is_menu = True
        self.menu = Menu(self)

        self.camera = Camera(self)
        self.projection = Projection(self)

        self.map_1 = Map([load_model(self, 'resources/rock.obj')], [self.camera])
        self.map_1.brushes[0].scale(2)


    def init(self):
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
            self.clock.tick()
            pg.display.set_caption(f'FPS: {int(self.clock.get_fps())}.')


if __name__ == '__main__':
    prog = Programm()
