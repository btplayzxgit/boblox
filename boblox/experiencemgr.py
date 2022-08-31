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
from psutil import cpu_percent

experience_db = {
      'Slither.io': 'https://slither.io/'
    , 'Paper.io': 'https://paper-io.com/'
    , 'Minecraft classic': 'https://classic.minecraft.net' 
    , 'Google pacman': 'https://www.google.com/logos/2010/pacman10-i.html'
    , 'Hole.io': 'https://www.hole-io.com'
    , 'Agar.io': 'https://www.agar.io'
    , '1v1.lol': 'https://www.1v1.lol'
    , 'Cookie clicker': 'https://trixter9994.github.io/Cookie-Clicker-Source-Code/'
    , 'Google snake': 'https://www.google.com/fbx?fbx=snake_arcade'
    , 'Google maps snake': 'https://snake.googlemaps.com/'
    , 'Digdig.io': 'https://www.digdig.io'
    , 'Wormate.io': 'https://www.wormate.io'
    , 'Flyufo.io': 'https://www.flyufo.io'
    , 'Tunnel rush': 'https://tunnelrush.github.io'
    , 'Flappy bird': 'https://flappybird.io/'
    , 'Diep.io': 'https://www.diep.io'
    , 'Windows 93': 'https://www.windows93.net'
    , 'Elastic man': 'https://elastic.clambam10.repl.co'
    , 'Paper.io hubspot': 'https://cdn2.hubspot.net/hubfs/5338309/Playables/Paperio3d/ad.html'
    , 'Paper.io top': 'https://www.paperio.top/'
    , 'Tilefall.io': 'https://tilefall.io'
    , 'Powerline.io': 'https://powerline.io'
    , 'Slither.io 3': 'https://slitherio-3.com/'
    , 'Hexgl': 'https://hexgl.bkcore.com/play/'
    , 'Slope': 'https://slope.fun/'
    , 'Geometry dash': 'https://dash.clambam10.repl.co/'
    , 'Funky karts': 'https://funkykarts.rocks/demo.html'
    , 'Five nights at freddys': 'https://fnafunblocked.fun/'
    , 'Among us': 'https://amongusplay.online/'
    , '1 dimension game': 'https://mashpoe.github.io/1D-Game'
    , 'Pie.ai': 'https://pie.ai/'
    , 'Moonlander': 'http://moonlander.seb.ly/'
    , 'Mine-craft.io': 'https://mine-craft.io/'
    , 'Smash the walls': 'https://smashthewalls.com/'
    , 'Litemint.io': 'https://litemint.io'
    , '2048': 'https://2048.org/'
    , 'Wordle': 'https://wordleplay.com/'
    , 'Amogus.fun': 'https://amogus.fun/'
    , 'Battlefields.io': 'https://battlefields.io'
    , 'Roblox': 'https://now.gg/play/roblox-corporation/5349/roblox'
}

def tryFindUrl(choice):
    val = (choice if choice else '').lower()

    for k in experience_db:
        if k.lower() == val:
            return experience_db[k]
    
    del k, val
    return ''

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





def run(choice):
    if choice == None: pass
    elif choice.capitalize() in experience_db:
        site = tryFindUrl(choice)

        pyautogui.alert(title='Boblox', text=f'{choice.capitalize()}\n\n\nExperience Link: {site}', button='PLAY')
        experiencemgr = QWebEngineView()
        experiencemgr.setWindowTitle('Boblox')
        experiencemgr.setGeometry(20, 50, 800, 700)
        experiencemgr.setWindowIcon(QIcon('boblox\\icon.png'))
        
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
        turtle.write(choice.capitalize(), align='center', font=('Open Sans', 35, 'bold'))
        turtle.goto(0, -40)
        turtle.write('Loading experience...', align='center', font=('Open Sans', 15, 'normal'))
        cpu = int(cpu_percent())
        if cpu > 79: 
            confirm_play = pyautogui.confirm(title='Boblox', text='Your CPU usage is very high.\nThis experience may be slow.\nAre you sure you want to play?\nWARNING: If you click "No, don\'t start the experience", then Boblox will close.', buttons=['Yes, start the experience', 'No, don\'t start the experience'])
            if confirm_play == 'Yes, start the experience': del confirm_play, cpu
            elif confirm_play == 'No, don\'t start the experience': del confirm_play, cpu; quit()
        else:
            pass
        try:
            with open('boblox\\block') as f:
                raw_rules = f.readlines()
                rules = AdblockRules(raw_rules)
        except:
            pyautogui.alert(title='Boblox', text='Error\nX_X\nBlocker was not found.', button='Quit'); quit()
        class WebEngineUrlInterceptor(QWebEngineUrlRequestInterceptor):
            def interceptRequest(self, info):
                url = info.requestUrl().toString()
                if rules.should_block(url):
                    info.block(True)
                    if url == 'https://now.gg/': info.block(True)
                    print('Boblox has blocked this ad or website address: {}'.format(url))
                    del url
        interceptor = WebEngineUrlInterceptor()
        QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
        sleep(0.5)
        experiencemgr.load(QUrl(site))
        experiencemgr.show()
        turtle.bye()
        app.exec_()
        del choice, site, experiencemgr, interceptor, raw_rules, rules
    elif choice.capitalize() not in experience_db:
        pyautogui.alert(title='Boblox', text=f'No results found for {choice}', button='Okay')