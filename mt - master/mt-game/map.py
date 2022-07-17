from model_renderer import*

class Map:
    def __init__(self, brushes, entitys, camera, app):
        self.entitys = entitys
        self.brushes = brushes
        self.brushes_renderrs = []
        self.app = app
        self.camera = camera
        self.create_brush_renderers()

    def action(self):
        for i in self.brushes_renderrs:
            i.draw()

        for j in self.entitys:
            j.bihawiur()


    def start(self):
        for i in self.brushes:
            i.init()

        for j in self.entitys:
            j.spawn()

    def create_brush_renderers(self):
        for i in self.brushes:
            self.brushes_renderrs.append(modelRenderer(i, self.camera))

