import pygame as pg
import screen
import math
from camera import*
import rtime as rt

class IBaseFpsCamera(IBaseCamera):
    def __init__(self):
        super(IBaseFpsCamera, self).__init__()
        self.name = 'first_person_camera'

        self.normal_height = 1.25
        self.is_grounded = False

        self.moving_speed = 12
        self.rotation_speed = 25
        self.base_cur = [sc.h_width, sc.h_height]

    def bihawiur(self):
        self.physycs()
        self.loock()
        self.key_controll()

    def key_controll(self):
        speed = self.moving_speed * rt.get_delta_time()
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.position -= self.right * speed
            self.translate_model(self.right * -speed)
        if key[pg.K_d]:
            self.position += self.right * speed
            self.translate_model(self.right * speed)

        if key[pg.K_w]:
            self.position += self.forward * speed
            self.translate_model(self.forward * speed)
        if key[pg.K_s]:
            self.position -= self.forward * speed
            self.translate_model(self.forward * -speed)

        if key[pg.K_q]:
            self.position += self.up * speed
            self.translate_model(self.up * speed)
        if key[pg.K_e]:
            self.position -= self.up * speed
            self.translate_model(self.up * -speed)

        if key[pg.K_ESCAPE]:
            exit(0)

    def physycs(self):
        pass

    def loock(self):
        sens = self.rotation_speed * rt.get_delta_time()
        m_pos = pg.mouse.get_pos()
        angle_m = [self.base_cur[0] - m_pos[0], self.base_cur[1] - m_pos[1]]

        self.pitch = 0
        self.pitch += angle_m[1]
        self.pitch = (self.pitch * math.pi / 180) * sens

        self.yaw = (math.pi * angle_m[0] / 180) * -sens
        self.camera_yaw((math.pi * angle_m[0] / 180) * -sens)
        # self.model_yaw((math.pi * angle_m[0] / 180) * -sens)
        pg.mouse.set_pos(self.base_cur[0], self.base_cur[1])

    def spawn(self):
        self.parameters['position'][1] = 2

        self.position[0] = self.parameters['position'][0]
        self.position[1] = self.parameters['position'][1]
        self.position[2] = self.parameters['position'][2]

        self.camera_pitch(self.parameters['angle'][0])
        self.camera_yaw(self.parameters['angle'][1])

        self.translate_model(self.position)

    def translate_model(self, dir):
        if self.model != None:
            self.model.translate(dir)

    def model_yaw(self, a):
        if self.model != None:
            self.model.rotate_y(a)

defoult_fps_camera = IBaseFpsCamera()

