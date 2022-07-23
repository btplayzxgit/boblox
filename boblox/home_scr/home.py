from tkinter import *
from PIL import Image, ImageTk
from boblox.experiencemgr import get_choices, run
from boblox.experience_search_prog import begin_search_gui
from boblox.settings_prog import open_settings
from boblox.bobux_get_prog import begin_bobux_get
import pyautogui


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

    btn_experiences = Image.open(buttons_dir + 'experience_button.png')
    btn_experience_search = Image.open(buttons_dir + 'experience_search_button.png')
    btn_settings = Image.open(buttons_dir + 'settings_button.png')
    btn_close = Image.open(buttons_dir + 'close_boblox_button.png')
    btn_get_bobux = Image.open(buttons_dir + 'get_bobux.png')

    boblox_label = Image.open('boblox\\home_scr\\boblox_label.png')
    bobux_label = Image.open('boblox\\home_scr\\bobux_icon.png')
    def photoimg(img): return ImageTk.PhotoImage(img)
    root.btn_experiences = photoimg(btn_experiences)
    root.btn_experience_search = photoimg(btn_experience_search)
    root.btn_settings = photoimg(btn_settings)
    root.btn_close = photoimg(btn_close)
    root.btn_get_bobux = photoimg(btn_get_bobux)

    root.boblox_label = photoimg(boblox_label)
    root.bobux_label = photoimg(bobux_label)
    def place_button(btn_x, btn_y, btn): canvas.create_window(btn_x, btn_y, window=btn)
    def destroy(): root.destroy()

    def experiences(): destroy(); run(pyautogui.confirm(title='Boblox', text='Experiences\n', buttons=get_choices()))
    def experience_search(): destroy(); begin_search_gui()
    def settings(): destroy(); open_settings()
    def get_bobux(): destroy(); begin_bobux_get()
    experiences_button = Button(root, image=root.btn_experiences, width=w, height=h, command=experiences)
    experience_search_button = Button(root, image=root.btn_experience_search, width=w, height=h+50, command=experience_search)
    settings_button = Button(root, image=root.btn_settings, width=w, height=h+5, command=settings)
    close_button = Button(root, image=root.btn_close, width=w, height=h+50, command=quit)
    get_bobux_button = Button(root, image=root.btn_get_bobux, width=356, height=140, command=get_bobux)


    boblox_label = Button(root, image=root.boblox_label, width=w-37, height=h*2-16, bd=0, relief='sunken')
    bobux_label = Button(root, image=root.bobux_label, width=97, height=72, bd=0, relief='sunken')



    place_button(600, 100, boblox_label)
    place_button(900, 100, bobux_label)

    place_button(600, 250, experiences_button)
    place_button(600, 380, experience_search_button)
    place_button(600, 510, settings_button)
    place_button(600, 650, close_button)
    place_button(1050, 250, get_bobux_button)

    



    root.mainloop()
