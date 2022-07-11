from ui import*

class Menu:
    def __init__(self, app):
        self.init()
        self.app = app

    def init(self):
        pass

    def action(self):
        self.draw()

    def draw(self):
        draw_rect([0,0], [0.1,0.1])


