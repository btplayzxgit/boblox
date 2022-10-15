from boblox.installer.installer import begin_installation
import os

os.system('title Boblox Processing Console')

begin_installation()
try:
    from boblox.account.account_check import run_account_check
    run_account_check()

    from boblox.home_scr.home import home 
    from boblox.wifi_check import internet

    while True:
        if internet(): home()
except ModuleNotFoundError as e:
    os.system('boblox\\import_error.vbs')
    os.system('pip uninstall PyQt5')
    os.system('pip uninstall PyQtWebEngine')
    os.system('pip uninstall pyautogui')
    os.system('pip uninstall adblockparser')
    os.system('pip uninstall psutil')
    os.system('pip uninstall requests')
    os.system('pip uninstall pillow')
    os.system('pip uninstall pyglet')
    os.system('pip uninstall numpy')
    os.system('pip uninstall beautifulsoup4')
    os.system('pip uninstall vidstream')
    begin_installation()
    print(e)

