from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from sys import argv

game_db = {
     'Slither.IO': 'https://www.slither.io'
    ,'Paper.IO': 'https://www.paper-io.com'
    ,'Minecraft': 'https://classic.minecraft.net' 
    ,'Google Pacman': 'https://www.google.com/logos/2010/pacman10-i.html'
    , 'Hole.IO': 'https://www.hole-io.com'
    , 'Agar.IO': 'https://www.agar.io'
    , '1v1.lol': 'https://www.1v1.lol'
    , 'github': 'https://github.com'
    , 'Cookie Clicker': 'http://orteil.dashnet.org/cookieclicker'
}

app = QApplication(argv)

def request_gamemgr(site):
    gamemgr = QWebEngineView()
    gamemgr.setWindowTitle('Boblox')
    gamemgr.load(QUrl(site))
    gamemgr.show()
    app.exec_()