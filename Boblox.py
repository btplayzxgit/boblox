from boblox.installer.installer import begin_installation

begin_installation()

import pyautogui
import os
from boblox.account.account_check import run_account_check
from boblox.gamemgr import request_gamemgr, game_db

run_account_check()

username = open('boblox\\account\\username').read()

while True:
    home_output = pyautogui.confirm(title='Boblox', text=f'Hello, {username}!\n\nGames\n', buttons=list(game_db.keys()) + ['Close Boblox'])
    print(home_output)
    if home_output == 'Close Boblox': 
        break
    elif home_output in game_db: 
        request_gamemgr(game_db[home_output]); 
    else: 
        break

quit()