import os, turtle


def begin_installation():
    turtle.title('Boblox')

    turtle.bgpic('boblox\\installer\\loadingimg.gif')
    turtle.setup(1960, 832)

    os.system('python -m pip install --upgrade pip')
    os.system('pip install PyQt5')
    os.system('pip install PyQtWebEngine')
    os.system('pip install pyautogui')
    os.system('pip install adblockparser')
    os.system('pip install psutil')
    os.system('pip install requests')
    os.system('pip install pillow')
    os.system('pip install pyglet')
    os.system('pip install numpy')

    turtle.bye()