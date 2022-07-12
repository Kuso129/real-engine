from entity import *
from utils import *
from drawing.model import *


class FunkBrush(IBaseEntity):
    def __init__(self, map, model_name='resources/models/cube.obj'):
        super(FunkBrush, self).__init__()
        self.map = map
        self.model = load_model(self.map.app, model_name, 'Material')
        self.name = 'funk_brush'


defoult_funk_brush = FunkBrush(curent_map)
link_entity(defoult_funk_brush, 'funk_brush')

