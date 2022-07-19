import numpy as np
from enum import Enum


class ModelFormats(Enum):
    def __init__(self):
        super(ModelFormats, self).__init__()
        self.OBJ_MODEL = 0
        self.COLLADA_MODEL = 1


class MeshBuilder:
    def __init__(self, path, name):
        self.name = name
        self.text = None
        self.create_object(path)

    def create_object(self, path):
        f = open(path, "r")
        self.text = f.read()

    def __str__(self):
        return self.text

