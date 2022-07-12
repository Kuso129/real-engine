import mathlib.pmath as pm

class Transform:
    def __init__(self, position=[0,0,0], angle=[0,0,0], scale=1, parant=None):
        self.position = position
        self.angle = angle
        self.scale = scale

        self.childrens = []
        self.parant = parant

    def get_matrix(self):
        if self.parant is None:
            trans = pm.translate(self.position)
            x_ang = pm.rotate_x(self.angle[0])
            y_ang = pm.rotate_x(self.angle[1])
            z_ang = pm.rotate_x(self.angle[2])
            rot = x_ang @ y_ang @ z_ang
            scl = pm.scale(self.scale)

            return trans @ rot @ scl
        else:
            trans = pm.translate(self.position)
            x_ang = pm.rotate_x(self.angle[0])
            y_ang = pm.rotate_x(self.angle[1])
            z_ang = pm.rotate_x(self.angle[2])
            rot = x_ang @ y_ang @ z_ang
            scl = pm.scale(self.scale)

            return trans @ rot @ scl @ self.parant.get_matrix()

    def add_child(self, obj):
        self.childrens.append(obj)
