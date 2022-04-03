try:
    import pyautogui
except:
    print()

try:
    from boblox.installer.installer import begin_installation
except Exception as e: pyautogui.alert(title='Boblox', text=f'Boblox failed to launch\n\n{e}', button='Close Boblox'); quit()

begin_installation()

import pyautogui
try:
    from boblox.account.account_check import run_account_check
    from boblox.gamemgr import get_choices, run
except Exception as e: pyautogui.alert(title='Boblox', text=f'Boblox failed to launch\n\n{e}', button='Close Boblox'); quit()

del begin_installation
run_account_check()

username = open('boblox\\account\\username').read()

while True: run(pyautogui.confirm(title='Boblox', text=f'Hello, {username}!\n\nGames\n', buttons=get_choices()))