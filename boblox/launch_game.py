from boblox.gamemgr import game_db, run
from boblox.gamemgr6 import game_db2, run2


def launch(game):
    game = str(game).capitalize()
    if game in list(game_db.keys()):
        run(game)
    elif game in list(game_db2.keys()):
        run2(game)
    else:
        return None