

def read_material(path):
    texture = None
    color = [0, 0, 0]
    filter_tex = True
    with open(path) as f:
        for line in f:
            if line.startswith('color: '):
                r = float(line.split()[1])
                g = float(line.split()[2])
                b = float(line.split()[3])
                color = [r, g, b]
            if line.startswith('tex: '):
                texture = line.split()[1]
            if line.startswith('filter: '):
                filter_tex = bool(line.split()[1])
    return [texture, color, filter_tex]
