
from boblox.installer.installer import begin_installation
import os

os.system('title Boblox Processing Console')

begin_installation()
from boblox.account.account_check import run_account_check
run_account_check()

from boblox.home_scr.home import home 
from boblox.wifi_check import internet
import pyautogui

while True:
    if internet(): home()
    else: pyautogui.alert(title='Boblox', text='No internet\nX _ X', button='Quit'); quit()