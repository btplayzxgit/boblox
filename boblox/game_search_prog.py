import pyautogui
from boblox.gamemgr import get_choices, run
from random import choice

def begin_search_gui():
    search_for = pyautogui.prompt(title='Boblox', text=f'Search\n\nTry searching for: {choice(get_choices())}')
    run(search_for)
    del search_for