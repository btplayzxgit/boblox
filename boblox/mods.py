import pyautogui
from ast import literal_eval


def display_mods():
    mods = open('boblox\\mods_list', 'r').read()
    print()
    change_mod = open('boblox\\mods_list', 'w')
    change_mod.write(mods)
    mod = pyautogui.confirm(title='Boblox', text='Select a mod to enable.', buttons=list(literal_eval(mods)))
    mod_info = literal_eval(mods)[mod]
display_mods()