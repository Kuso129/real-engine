

class ModelGroup:
    def __init__(self, models, transform, map):
        self.models = models
        self.transform = transform
        self.init()

    def init(self):
        for i in self.models:
            i.init()




