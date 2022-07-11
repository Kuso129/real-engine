

def get_count_mtl(path):
    count = 0
    with open(path) as f:
        for line in f:
            if line.startswith("# Material Count: "):
                line = line.split()
                count = line[3]
    return count

def get_mtl_names(path):
    names = []
    with open(path) as f:
        for line in f:
            if line.startswith("newmtl "):
                ln = line.split()
                names.append(ln[1])
    return names

def load_matereal_by_name(path, name):
    material = {
        'ambient_color': None,
        'defuse_color': None,
        'mirror_color': None,
        'mirror_coeff': None,
        'opacity': None,
        'texture': None
    }
    is_detected = False
    with open(path) as f:
        for line in f:
            if not is_detected:
                if line.startswith(f'newmtl {name}'):
                    is_detected = True
            else:
                if line.startswith('Ka '):
                    mat = [float(line.split()[1]),float(line.split()[2]),float(line.split()[3])]
                    material['ambient_color'] = mat
                elif line.startswith('Kd '):
                    mat = [float(line.split()[1]),float(line.split()[2]),float(line.split()[3])]
                    material['defuse_color'] = mat
                elif line.startswith('Ks '):
                    mat = [float(line.split()[1]),float(line.split()[2]),float(line.split()[3])]
                    material['mirror_color'] = mat
                elif line.startswith('Ns '):
                    mat = float(line.split()[1])
                    material['mirror_coeff'] = mat
                elif line.startswith('Ns '):
                    mat = float(line.split()[1])
                    material['mirror_coeff'] = mat
                elif line.startswith('Tr ') or line.startswith('d '):
                    mat = float(line.split()[1])
                    material['opacity'] = mat
                elif line.startswith('map_Kd '):
                    mat = line.split()[1]
                    material['texture' ] = mat

                if line.startswith('newmtl') or line.startswith(""):
                    return material
    return material

def load_matirial_mtl(path):
    names = get_mtl_names(path)
    materials = []

    for i in names:
        materials.append(load_matereal_by_name(path, i))

    return materials

