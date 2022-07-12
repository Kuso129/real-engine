import entity as ent

all_entitys = {

}

def link_entity(entity):
    all_entitys[entity.name] = entity

def get_entity(name):
    return all_entitys.get(name)

