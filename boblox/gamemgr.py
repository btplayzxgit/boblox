from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from sys import argv
import random
import requests

game_db = {
     'Slither.IO': 'https://www.slither.io'
    ,'Paper.IO': 'https://www.paper-io.com'
    ,'Minecraft': 'https://classic.minecraft.net' 
    ,'Google Pacman': 'https://www.google.com/logos/2010/pacman10-i.html'
    , 'Hole.IO': 'https://www.hole-io.com'
    , 'Agar.IO': 'https://www.agar.io'
    , '1v1.lol': 'https://www.1v1.lol'
    , 'Cookie Clicker': 'https://trixter9994.github.io/Cookie-Clicker-Source-Code/'
    , 'Google Snake': 'https://www.google.com/fbx?fbx=snake_arcade'
    , 'Google Maps Snake': 'https://snake.googlemaps.com/'
    , 'DigDig.IO': 'https://www.digdig.io'
    , 'Google Maps': 'https://www.google.com/maps/'
    , 'Wormate.IO': 'https://www.wormate.io'
    , 'FlyUFO.IO': 'https://www.flyufo.io'
    , 'Tunnel Rush': 'https://tunnelrush.github.io'
}

app = QApplication(argv)

def get_choices():
    choices_randomized = []
    take_choices = list(game_db.keys())
    for x in list(game_db.keys()):
        choice = random.choice(take_choices)
        take_choices.remove(choice)
        choices_randomized.append(choice)
        
    del x
    return choices_randomized + ['Close Boblox']

def run(choice):
    if choice == 'Close Boblox' or choice not in game_db: 
        quit()
    site = game_db[choice]
    gamemgr = QWebEngineView()
    gamemgr.setWindowTitle('Boblox')
    gamemgr.load(QUrl(site))
    gamemgr.show()
    app.exec_()