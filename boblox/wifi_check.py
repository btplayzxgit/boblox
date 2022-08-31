import requests
import pyautogui
from boblox.nointernet.NotSoMinecraft import start

url = 'https://www.google.com'

def internet():
    while True:
        try:
            requests.get(url, timeout=5)
            return True
        except:
            ni = pyautogui.confirm(title='Boblox', text='No internet\nX _ X\nDo you want to play Minecraft while you are disconnected?', buttons=['Play Minecraft', 'Quit'])
            if ni == 'Play Minecraft': start()
            else: quit()