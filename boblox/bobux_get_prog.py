import turtle
from random import randint
from time import sleep
from boblox.account.bobuxmgr import add_to_bobux

def begin_bobux_get():
    try:
        turtle.title('Boblox')
    except:
        turtle.title('Boblox')
    turtle.bgcolor('green')

    write = turtle.Turtle()
    write.speed(0)
    write.hideturtle()
    write.penup()
    write.left(90)
    write.forward(250)
    write.write('You earned', align='center', font=('Arial', 45, 'normal'))
    write.back(550)
    write.write('bobux', align='center', font=('Arial', 45, 'normal'))

    for x in range(20):
        turtle.write(str(randint(0, 100)), align='center', font=('Arial', 65, 'bold'))
        turtle.hideturtle()
        sleep(0.05)
        turtle.clear()

    bobux_to_give = str(randint(0, 100))
    turtle.color('green')
    turtle.bgcolor('lightgreen')
    turtle.write(bobux_to_give, align='center', font=('Arial', 65, 'bold'))
    add_to_bobux(bobux_to_give)


    turtle.mainloop()