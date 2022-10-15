from tkinter import *
from PIL import Image, ImageTk
from boblox.gamemgr import get_choices, run
from boblox.game_search_prog import begin_search_gui
from boblox.settings_prog import open_settings
from boblox.chat.choose_conn import choose
import turtle
from random import randint
from time import sleep
import pyautogui
from ast import literal_eval


def home():
    root = Tk()
    root.title('Boblox')
    root.iconphoto(False, PhotoImage(file='boblox\\icon.png'))
    root.geometry('1280x830')

    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=TRUE)
  

    buttons_dir = 'boblox\\home_scr\\buttons\\'
    w = 488 - 55
    h = 140 - 48


    bobux = literal_eval(open('boblox\\bux\\bobux', 'r').read())
    bobux_dict = bobux
    bobux = int(bobux['bobux'])

    bobux_text = Label(canvas, text='\n\n\n\n\n\n                                                                                                                                                                                                                                                                                                                                                           '+str(bobux))
    bobux_text.grid(row=0, column=0)


    btn_games = Image.open(buttons_dir + 'games_button.png')
    btn_game_search = Image.open(buttons_dir + 'game_search_button.png')
    btn_settings = Image.open(buttons_dir + 'settings_button.png')
    btn_mods = Image.open( buttons_dir + 'mods_button.png')
    btn_chat = Image.open(buttons_dir + 'chat_button.png')
    btn_close = Image.open(buttons_dir + 'close_boblox_button.png')

    bobux_icon = Image.open('boblox\\bobux_icon.png')
    boblox_label = Image.open('boblox\\home_scr\\boblox_label.png')

    def photoimg(img): return ImageTk.PhotoImage(img)
    root.btn_games = photoimg(btn_games)
    root.btn_game_search = photoimg(btn_game_search)
    root.btn_settings = photoimg(btn_settings)
    root.btn_close = photoimg(btn_close)
    root.btn_mods = photoimg(btn_mods)
    root.btn_chat = photoimg(btn_chat)

    root.boblox_label = photoimg(boblox_label)
    root.bobux_icon = photoimg(bobux_icon)

    def place_button(btn_x, btn_y, btn): canvas.create_window(btn_x, btn_y, window=btn)
    def destroy(): root.destroy()

    def games(): destroy(); run(pyautogui.confirm(title='Boblox', text='Games\n', buttons=get_choices()))
    def game_search(): destroy(); begin_search_gui()
    def settings(): destroy(); open_settings()
    def chat(): destroy(); choose()
    
    
    games_button = Button(root, image=root.btn_games, width=w, height=h, command=games)
    game_search_button = Button(root, image=root.btn_game_search, width=w, height=h+50, command=game_search)
    settings_button = Button(root, image=root.btn_settings, width=w, height=h+5, command=settings)
    mods_button = Button(root, image=root.btn_mods, width=147, height=86, command=quit)
    chat_button = Button(root, image=root.btn_chat, width=180, height=89, command=chat)
    close_button = Button(root, image=root.btn_close, width=w, height=h+50, command=quit)


    boblox_label = Button(root, image=root.boblox_label, width=w-37, height=h*2-16, bd=0, relief='sunken')
    bobux_icon = Button(root, image=root.bobux_icon, width=111, height=71, bd=0, relief='sunken')


    

    place_button(600, 100, boblox_label)
    place_button(930-int(len(str(bobux*3))), 100, bobux_icon)
    

    place_button(600, 250, games_button)
    place_button(600, 380, game_search_button)
    place_button(600, 510, settings_button)
    place_button(200, 100, mods_button)
    place_button(930, 210, chat_button)
    place_button(600, 650, close_button)






    

    
    

    



    root.mainloop()
