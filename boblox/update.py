import requests
from bs4 import BeautifulSoup
import pyautogui

files = ['https://github.com/btplayzxgit/boblox/blob/main/boblox/block',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/experience_search_prog.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/experiencemgr.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/settings_prog.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/wifi_check.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/nointernet/minecraft.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/nointernet/NotSoMinecraft.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/nointernet/source/title.bat',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/nointernet/source/noise_gen.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/installer/installer.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/home_scr/home.py',
        'https://github.com/btplayzxgit/boblox/blob/main/boblox/account/account_check.py']

def update(url):
    global fail
    fail = False
    try:
        response = requests.get(url)
        fail = False
    except:
        update_fail = pyautogui.confirm(title='Boblox', text='Failed to attempt to update Boblox.', buttons=['Exit', 'Continue'])
        if update_fail == 'Continue': fail = True
        else: fail = True; exit()
    
    if not fail:
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        print(f'Updating {soup.title.get_text()}\n\n')
        



for file in files:
    update(file)