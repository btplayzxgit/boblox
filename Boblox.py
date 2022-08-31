from boblox.installer.installer import begin_installation
import os

os.system('title Boblox Processing Console')

begin_installation()
from boblox.account.account_check import run_account_check
run_account_check()

from boblox.home_scr.home import home 
from boblox.wifi_check import internet

while True:
    if internet(): home()