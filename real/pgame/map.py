

class Map:
    def __init__(self, brushes, entitys):
        self.entitys = entitys
        self.brushes = brushes

    def action(self):
        for i in self.brushes:
            i.draw()

        for j in self.entitys:
            j.bihawiur()

    def start(self):
        for i in self.brushes:
            i.init()

        for j in self.entitys:
            j.spawn()

