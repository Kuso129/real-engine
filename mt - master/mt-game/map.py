from model_renderer import*

class Map:
    def __init__(self, brushes, entitys, camera, app):
        self.entitys = entitys
        self.brushes = brushes
        self.app = app
        self.camera = camera

        self.brushes_renderrs = []
        self.entity_renderers = []

        self.create_brush_renderers()
        # self.create_entitys_renderers()

    def action(self):
        for j in self.entitys:
            j.bihawiur()

        for i in self.brushes_renderrs:
            i.draw()

    def start(self):
        for i in self.brushes:
            i.init()

        for j in self.entitys:
            j.spawn()

    def create_brush_renderers(self):
        for i in self.brushes:
            self.brushes_renderrs.append(modelRenderer(i, self.camera))

    def create_entitys_renderers(self):
        for i in self.entitys:
            self.entity_renderers.append(modelRenderer(i.model, self.camera))

