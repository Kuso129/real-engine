from object_3d import*

modelview_weapon = [0.25,-0.95,2]

def get_weapon_pos(pos):
    return [pos[0] + modelview_weapon[0], pos[1] + modelview_weapon[1], pos[2] + modelview_weapon[2]]

class WeaponBase:
    def __init__(self,app, mdl_path):
        self.model = load_model(app, mdl_path)
        self.app = app

    def translate(self, pos):
        self.model.translate(pos)


class WpVityaz(WeaponBase):
    def __init__(self, app):
        super(WpVityaz, self).__init__(app, 'resources/w_vityaz.obj')

