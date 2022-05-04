from boblox.installer.installer import begin_installation
from boblox.account.account_check import run_account_check
from boblox.experiencemgr import get_choices, run
from boblox.experience_search_prog import begin_search_gui
from platform import system
import os


if system() == 'Windows': os.system('title Boblox Processing Console')
elif system() == 'Mac': os.system('echo -n -e "033]0;Boblox Processing Console007"')

begin_installation()

import pyautogui

run_account_check()

username = open('boblox\\account\\username', 'r').read()

while True:
    home_output = pyautogui.confirm(title='Boblox', text=f'Hello, {username}!', buttons=['Experiences', 'Experience Search', 'Close Boblox'])
    if home_output == None: quit()
    elif home_output == 'Close Boblox': quit()
    elif home_output == 'Experiences': run(pyautogui.confirm(title='Boblox', text='Experiences\n', buttons=get_choices()))
    elif home_output == 'Experience Search': begin_search_gui()