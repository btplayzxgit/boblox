import socket
import pyautogui
from boblox.nointernet.NotSoMinecraft import start

url = 'www.google.com'


def internet():
    try: 
        socket.create_connection((url, 80))
        return True
    except OSError:
        ni = pyautogui.confirm(title='Boblox', text='No internet\nX _ X\nDo you want to play Minecraft while you are disconnected?\nThis could be due to the firewall on. If you believe this is a glitch click "Continue".', buttons=['Play Minecraft', 'Quit', 'Retry', 'Continue'])
        if ni == 'Play Minecraft': start()
        elif ni == 'Quit': quit()
        elif ni == None: quit()
        elif ni == 'Retry': internet()
        elif ni == 'Continue': return True