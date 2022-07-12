import math
import numpy as np


class Projection:
    def __init__(self, camera):
        self.camera = camera
        self.update()

    def update(self):
        NEAR = self.camera.near_plane
        FAR = self.camera.far_plane
        RIGHT = math.tan(self.camera.h_fov / 2)
        LEFT = -RIGHT
        TOP = math.tan(self.camera.v_fov / 2)
        BOTTOM = -TOP

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])


