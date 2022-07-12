from weapons import*
from entity import*
import utils as ut
import screen as sc
import projection as proj

class IBaseCamera(IBaseEntity):
    def __init__(self):
        super(IBaseCamera, self).__init__()
        self.name = 'd_camera'

        self.position = np.array([0,1.25,-15, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (sc.height / sc.width)
        self.near_plane = 0.01
        self.far_plane = 192

        self.projection = proj.Projection(self)

    def camera_yaw(self, angle):
        rotate = rotate_y(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_pitch(self, angle):
        rotate = rotate_x(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_roll(self, angle):
        rotate = rotate_z(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def translate_matrix(self):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-self.position[0], -self.position[1], -self.position[2], 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()

    def spawn(self):
        self.position[0] = self.parameters['position'][0]
        self.position[1] = self.parameters['position'][1]
        self.position[2] = self.parameters['position'][2]

        self.camera_pitch(self.parameters['angle'][0])
        self.camera_yaw(self.parameters['angle'][1])

