from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import *
from sys import argv
import random
import pyautogui
import turtle
from time import sleep
from adblockparser import AdblockRules

experience_db = {
      'Slither.io': 'https://www.slither.io'
    , 'Paper.io': 'https://www.paper-io.com'
    , 'Minecraft Classic': 'https://classic.minecraft.net' 
    , 'Google Pacman': 'https://www.google.com/logos/2010/pacman10-i.html'
    , 'Hole.io': 'https://www.hole-io.com'
    , 'Agar.io': 'https://www.agar.io'
    , '1v1.lol': 'https://www.1v1.lol'
    , 'Cookie Clicker': 'https://trixter9994.github.io/Cookie-Clicker-Source-Code/'
    , 'Google Snake': 'https://www.google.com/fbx?fbx=snake_arcade'
    , 'Google Maps Snake': 'https://snake.googlemaps.com/'
    , 'DigDig.io': 'https://www.digdig.io'
    , 'Google Maps': 'https://www.google.com/maps/'
    , 'Wormate.io': 'https://www.wormate.io'
    , 'FlyUFO.io': 'https://www.flyufo.io'
    , 'Tunnel Rush': 'https://tunnelrush.github.io'
    , 'Flappy Bird': 'https://flappybird.io/'
    , 'Diep.io': 'https://www.diep.io'
    , 'Windows 93': 'https://www.windows93.net'
    , 'Elastic Man': 'https://elasticman.co/'
}

case_insensitive_experience_db = {}

for k, v in experience_db.items():
    print(k)
    case_insensitive_experience_db[k.lower()] = v

app = QApplication(argv)

def get_choices():
    choices_randomized = []
    take_choices = list(experience_db.keys())
    for x in range(16):
        choice = random.choice(take_choices)
        take_choices.remove(choice)
        choices_randomized.append(choice)
        
    del x, choice, take_choices
    return choices_randomized

def get_site(value):
    site = case_insensitive_experience_db[(value if value else '').lower()]

    if not site:
        return ''
    
    return site

def run(choice):
    site = get_site(choice)

    if not site:
        return

    # if ' ' not in choice: choice = choice.capitalize()
    # elif ' ' in choice: pass

    pyautogui.alert(title='Boblox', text=f'{choice}\n\n\nGame Link: {site}', button='PLAY')
    gamemgr = QWebEngineView()
    gamemgr.setWindowTitle('Boblox')
    gamemgr.setGeometry(20, 50, 800, 700)
    gamemgr.setWindowIcon(QIcon('boblox\\icon.png'))
    
    try:
        turtle.title('Boblox')
    except:
        turtle.title('Boblox')
    turtle.bgcolor('black')
    turtle.penup()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.goto(0, 10)
    turtle.pencolor('white')
    turtle.write(choice, font=('Open Sans', 35, 'bold'))
    turtle.goto(0, -40)
    turtle.write('Loading experience...', font=('Open Sans', 15, 'normal'))
    with open('boblox\\block') as f:
        raw_rules = f.readlines()
        rules = AdblockRules(raw_rules)
    class WebEngineUrlInterceptor(QWebEngineUrlRequestInterceptor):
        def interceptRequest(self, info):
            url = info.requestUrl().toString()
            if rules.should_block(url): info.block(True); print('Boblox has blocked this ad or website address: {}'.format(url)); del url
    interceptor = WebEngineUrlInterceptor()
    QWebEngineProfile.defaultProfile().setRequestInterceptor(interceptor)
    sleep(0.5)
    gamemgr.load(QUrl(site))
    gamemgr.show()
    turtle.bye()
    app.exec_()
    del choice, site, gamemgr, interceptor, f, raw_rules, rules