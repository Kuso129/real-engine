import first_person_camera as ent
import utils as ut


class DBasePlayer(ent.IBaseFpsCamera):
    def __init__(self, prog):
        super(DBasePlayer, self).__init__()



demo_game_player = DBasePlayer(ut.curent_programm)


