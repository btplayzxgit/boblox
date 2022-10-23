from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *
from sys import argv
import random
import pyautogui
import turtle
from psutil import cpu_percent

game_db2 = {
    'Roblox': 'https://v3.now.gg/play/5349'

}

def tryFindUrl(choice):
    val = (choice if choice else '').lower()

    for k in game_db2:
        if k.lower() == val:
            return game_db2[k]
    
    del k, val
    return ''

app = QApplication(argv)

def get_choices2():
    choices_randomized = []
    take_choices = list(game_db2.keys())
    for x in range(len(take_choices)):
        choice = random.choice(take_choices)
        take_choices.remove(choice)
        choices_randomized.append(choice)
        
    del x, choice, take_choices
    return choices_randomized





def run2(choice):
    if choice == None: pass
    elif choice.capitalize() in game_db2:
        game = tryFindUrl(choice)

        pyautogui.alert(title='Boblox', text=f'{choice.capitalize()}\n\n\nGame URL: {game}', button='PLAY')
        
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
        turtle.write('Loading game...', align='center', font=('Open Sans', 15, 'normal'))
        cpu = int(cpu_percent())
        if cpu > 79: 
            confirm_play = pyautogui.confirm(title='Boblox', text='Your CPU usage is very high.\nThis game may be slow.\nAre you sure you want to play?\nWARNING: If you click "No, don\'t start the game", then Boblox will close.', buttons=['Yes, start the game', 'No, don\'t start the game'])
            if confirm_play == 'Yes, start the game': del confirm_play, cpu
            elif confirm_play == 'No, don\'t start the game': del confirm_play, cpu; quit()
        else:
            pass
        
        
        class MyWebBrowser(QMainWindow):
            def __init__(self, *args, **kwargs):
                super(MyWebBrowser, self).__init__(*args, **kwargs)

                self.window = QWidget()
                self.window.setWindowTitle('Boblox')
                self.window.setWindowIcon(QIcon('boblox\\icon.png'))
                self.window.setGeometry(20, 50, 800, 700)
                

                self.layout = QVBoxLayout()
                self.horizontal = QHBoxLayout()

                self.go_btn = QPushButton('Leave game')
                self.go_btn.setMinimumHeight(30)

                self.horizontal.addWidget(self.go_btn)

                self.browser = QWebEngineView()

                self.go_btn.clicked.connect(lambda: app.closeAllWindows())

                self.layout.addLayout(self.horizontal)
                self.layout.addWidget(self.browser)

                self.browser.setUrl(QUrl(game))

                self.window.setLayout(self.layout)
                self.window.show()
            def navigate(self, url):
                self.browser.setUrl(QUrl(url))
        turtle.bye()

        app = QApplication([])
        window = MyWebBrowser()
        del choice, game
        app.exec()
    elif choice.capitalize() not in game_db2:
        pyautogui.alert(title='Boblox', text=f'No results found for {choice}', button='Okay')