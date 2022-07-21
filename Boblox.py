from boblox.home_scr.home import home
from boblox.installer.installer import begin_installation
from boblox.account.account_check import run_account_check
import os

os.system('title Boblox Processing Console')

begin_installation()
run_account_check()
while True: home()