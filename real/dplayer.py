import first_person_camera as ent
import utils as ut
import drawing.model as mdl

class DBasePlayer(ent.IBaseFpsCamera):
    def __init__(self, prog):
        super(DBasePlayer, self).__init__()



demo_game_player = DBasePlayer(ut.curent_programm)
ut.link_entity(demo_game_player, 'demo_game_player')


