import pyautogui
from boblox.gamemgr import get_choices
from boblox.gamemgr6 import get_choices2
from boblox.launch_game import launch
from random import choice

def begin_search_gui():
    search_for = pyautogui.prompt(title='Boblox', text=f'Search\n\nTry searching for: {choice(get_choices()+get_choices2())}')
    launch(search_for)
    del search_for