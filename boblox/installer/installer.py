import os, turtle


def begin_installation():
    turtle.title('Boblox')

    turtle.bgpic('boblox\\installer\\loadingimg.gif')
    turtle.setup(1960, 832)

    os.system('pip install PyQt5')
    os.system('pip install PyQtWebEngine')
    os.system('pip install pyautogui')
    os.system('pip install adblockparser')

    turtle.bye()