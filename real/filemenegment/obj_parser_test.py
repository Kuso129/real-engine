#
# Written by Soloviev Ivan.
#
# This .obj file parser is based again on the code of the Standelone coder.
#
# Summary:
# Added reading of groups of objects, reading of normals and padding of texture coordinates.
#
import drawing.model as msh

def obj_name_translate(name):
    return f'{name}.obj'

def load_objects_names_obj(path):
    names = []
    with open(path) as f:
        for line in f:
            if line.startswith('o '):
                names.append([str(i) for i in line.split()[1:]])
    return names

def load_object_by_name_obj(app, path, name):
    vertex, faces, uv, normals = [],[],[],[]
    is_founded = False
    with open(path) as f:
        for line in f:
            if not is_founded:
                if line.startswith(f'o {name}'):
                    is_founded = True
            else:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
                elif line.startswith('vt '):
                    uv.append([float(i) for i in line.split()[1:]])
                elif line.startswith('vn '):
                    normals.append([float(i) for i in line.split()[1:]])
                if line.startswith(f'o ') or line.startswith(""):                           # what of fuck ?
                    return msh.Mesh(app, vertex, faces, normals, uv)
    return None

def load_mesh_obj(path):
    names = load_objects_names_obj(path)
    print(names)
    mesh = []

    print(len(names))
    for i in range(len(names)):
        mdl = load_object_by_name_obj(path, names[i][0])
        if mdl != None:
            print(names[i][0])
            mesh.append(mdl)
            print(mdl)

    return mesh

