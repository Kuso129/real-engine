import numpy as np
from PIL import Image
import pygame as pg

class Image2DLoader:
    def __init__(self, path, name):
        self.name = name
        self.path = path
        self.data = None
        self.create_image()


    def load_image_data(self, path):
        img = Image.open(path)
        img.load()
        data = np.asarray(img)
        return data

    def get_image_size(self, path):
        img = pg.image.load(path).convert()
        return img.get_size()

    def create_image(self):
        self.data = self.load_image_data(self.path)
        self.normalize_color()

    def normalize_color(self):
        self.data = self.data / 255

    def __str__(self):
        return self.data.__str__()

    def get_pk_file_name(self):
        return f".i {self.name}"

    def get_file_struct(self):
        string = []
        string.append(self.data[0])
        return string.__str__()

    def write_image_data(self, f):
        for i in self.data:
            f.write(f"\n{i.__str__()}")

