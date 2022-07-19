from image import*
from mesh import*


class MPKFileBuilder:
    def __init__(self, path_to_cfg):
        self.path_to_cfg = path_to_cfg

        # attributes
        self.parameters = {
            'name': None,
        }

        self.images = []
        self.models = []

        self.load_cfg_info(self.path_to_cfg)
        self.write_pack()

    def load_cfg_info(self, path):
        with open(path) as f:
            for line in f:
                if line.startswith('target_name: '):
                    self.parameters['name'] = line.split()[1]
                if line.startswith('image: '):
                    self.images.append(Image2DLoader(line.split()[1], line.split()[2]))
                if line.startswith('mesh: '):
                    self.models.append(MeshBuilder(line.split()[1], line.split()[2]))

    def write_pack(self):
        line_id = 0
        f = open(self.parameters['name'] + ".mpk", "w+")
        f.write(f"pack name: {self.parameters['name']}")
        self.write_images(f)
        f.close()

    def write_images(self, f):
        print('Images write process...')
        for i in self.images:
            f.write(f"\n{i.get_pk_file_name()}")
            i.write_image_data(f)
        print('Images write process end.')

