from drawing.mesh import*

modelview_weapon = [0.25,-0.95,2]

def get_weapon_pos(pos):
    return [pos[0] + modelview_weapon[0], pos[1] + modelview_weapon[1], pos[2] + modelview_weapon[2]]

