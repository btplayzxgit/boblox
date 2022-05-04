import pyautogui
from boblox.experiencemgr import experience_db, get_choices, run
from random import choice

def begin_search_gui():
    search_for = pyautogui.prompt(title='Boblox', text=f'Search\n\nTry searching for: {choice(get_choices())}')
    if search_for == None: pass
    elif search_for.capitalize() not in experience_db: pyautogui.alert(title='Boblox', text=f'There are no results for {search_for}', button='Okay')
    elif search_for.capitalize() in experience_db:
        if ' ' not in search_for:
            h = pyautogui.alert(title='Boblox', text=f'Result found for {search_for}!\n\n', button=f'Play {search_for.capitalize()}')
            if h == None: del h; pass
            elif h == f'Play {search_for.capitalize()}': run(search_for)
        elif ' ' in search_for:
            search_for = search_for.capitalize([search_for.index(' ') + 1])
            h = pyautogui.alert(title='Boblox', text=f'Result found for {search_for}!\n\n', button=f'Play {search_for.capitalize()}')
            if h == None: del h; pass
            elif h == f'Play {search_for.capitalize()}': run(search_for)






    del search_for