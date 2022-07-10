from weapons import*

class Camera:
    def __init__(self, render):
        self.render = render

        self.position = np.array([0,1.25,-15, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)
        self.near_plane = 0.01
        self.far_plane = 96

        self.moving_speed = 3.5
        self.rotation_speed = 32
        self.base_cur = [self.render.H_WIDTH, self.render.H_HEIGHT]

        self.jump_power = 0.0032
        self.yaw = 0
        self.mass = 4

    def bihawiur(self):
        self.loock()
        self.key_controll()

    def key_controll(self):
        speed = self.moving_speed * get_delta_time(self.render.clock.get_fps())
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.position -= self.right * speed
        if key[pg.K_d]:
            self.position += self.right * speed

        if key[pg.K_w]:
            self.position += self.forward * speed
        if key[pg.K_s]:
            self.position -= self.forward * speed

        if key[pg.K_q]:
            self.position += self.up * speed
        if key[pg.K_e]:
            self.position -= self.up * speed

        if key[pg.K_SPACE]:
            self.position[1] += math.sqrt(self.jump_power * self.mass)

        if key[pg.K_ESCAPE]:
            exit(0)

    def loock(self):
        sens = self.rotation_speed * get_delta_time(self.render.clock.get_fps())

        m_pos = pg.mouse.get_pos()
        angle_m = [self.base_cur[0] - m_pos[0], self.base_cur[1] - m_pos[1]]

        self.pitch = 0
        self.pitch += angle_m[1]
        self.pitch = clamp(self.pitch, -90, 90)
        self.pitch = (self.pitch * math.pi / 180) * sens

        # self.camera_roll(-(self.pitch / 3))
        self.yaw = (math.pi * angle_m[0] / 180) * -sens
        self.camera_yaw((math.pi * angle_m[0] / 180) * -sens)
        #self.camera_roll(0)

        pg.mouse.set_pos(self.base_cur[0], self.base_cur[1])

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
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
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
        pass