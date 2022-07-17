from entity import*
from model_renderer import*

class IBaseSkyBox(IBaseEntity):
    def __init__(self, mat):
        super(IBaseSkyBox, self).__init__()
        self.name = 'v_skybox'
        self.scale = 56
        self.model = load_model('resources/models/cube.obj', mat)
        self.model.scale(self.scale)
        self.model.normals = None

def_skybox = IBaseSkyBox('resources/scripts/sky_8.mtpy')
