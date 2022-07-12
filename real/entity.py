

class IBaseEntity:
    def __init__(self):
        self.is_active = True
        self.model = None
        self.name = 'semple_entity'

        self.parameters = {
            'position': [0, 0, 0],
            'angle': [0, 0, 0],
            'scale': 1,
            'c_name': self.name
        }

    def bihawiur(self):
        pass

    def spawn(self):
        pass

    def end(self):
        pass

    def set_active(self, active):
        self.is_active = active

