from entity import *
from utils import *
from model import *


class FunkBrush(IBaseEntity):
    def __init__(self, map, model_name='resources/models/cube.obj'):
        super(FunkBrush, self).__init__()
        self.map = map
        self.model = load_model(curent_programm, model_name)
        self.name = 'funk_brush'

