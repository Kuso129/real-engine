import entity as ent

curent_map = None
curent_programm = None

all_entitys = {

}

def link_entity(entity, t_name):
    all_entitys[t_name] = entity

def get_entity(name):
    return all_entitys.get(name)

