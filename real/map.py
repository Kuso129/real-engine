

class Map:
    def __init__(self, brushes, entitys, app):
        self.entitys = entitys
        self.brushes = brushes
        self.app = app

    def action(self):
        for i in self.brushes:
            i.draw()

        for j in self.entitys:
            j.bihawiur()

        for d in self.entitys:
            d.draw()

    def start(self):
        for i in self.brushes:
            i.init()

        for j in self.entitys:
            j.spawn()

