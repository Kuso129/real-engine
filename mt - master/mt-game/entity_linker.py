from first_person_camera import*
from dplayer import*
from funk_brush import*

def link_all_entitys():
    link_entity(defoult_fps_camera, 'info_first_person_camera')
    link_entity(demo_game_player, 'info_demo_player')
    # f = open('meat_town.txt', 'w')
    # f.write(str(all_entitys.keys()))
    # f.close()
