from first_person_camera import*
from dplayer import*
from funk_brush import*
# from ibase_skybox import*

def link_all_entitys():
    link_entity(defoult_fps_camera, 'info_first_person_camera')
    link_entity(demo_game_player, 'info_demo_player')
    # link_entity(def_skybox, 'r_skybox')
