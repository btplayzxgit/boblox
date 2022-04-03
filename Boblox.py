from boblox.installer.installer import begin_installation

begin_installation()

import pyautogui
from boblox.account.account_check import run_account_check
from boblox.gamemgr import get_choices, run

run_account_check()

username = open('boblox\\account\\username').read()

while True: run(pyautogui.confirm(title='Boblox', text=f'Hello, {username}!\n\nGames\n', buttons=get_choices()))