from tkinter import *
import pyautogui

def run_account_check():
    global username_file
    username_file = open('boblox\\account\\username', 'r')
    username = username_file.read()
    if username == '':
        def create():
            username_file = open('boblox\\account\\username', 'w')
            create_username = send_username.get()
            username_file.write(create_username)
            

            pyautogui.alert(title='Boblox', text='Account Created\nClick the button and restart Boblox', button='Exit')
            exit()

        screen = Tk()
        screen.geometry('600x400')
        screen.title('Boblox')
        Label(text='Boblox', bg='yellow', width='300', height='4', font=('Arial', 30)).pack()
        Label(text='').pack()
        Label(text='Welcome to Boblox!', bg='blue', font=('Arial', 13)).pack()

        global send_username
        send_username = StringVar()
        Label(text='').pack()
        Label(text='Create a username', bg='lightblue').pack()
        Entry(screen, textvariable=send_username).pack()
        Label(screen, text='').pack()
        Button(text='Create Account', bg='green', command=create).pack()
        
        
        screen.mainloop()
    else:
        pass
    

run_account_check()