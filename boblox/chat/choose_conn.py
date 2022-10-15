from boblox.chat.encrypt import encrypt
import boblox.chat.server as server
import boblox.chat.client as client
from tkinter import *
import threading
from PIL import Image, ImageTk
from socket import gethostname, gethostbyname
from boblox.chat.decode import decode
import time


def choose():
    root = Tk()
    root.title('Boblox')
    root.iconphoto(False, PhotoImage(file='boblox\\icon.png'))
    root.geometry('1200x800')

    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=TRUE)
    print(encrypt(gethostbyname(gethostname())))

    def photoimg(img): return ImageTk.PhotoImage(img)
    def place_button(btn_x, btn_y, btn): canvas.create_window(btn_x, btn_y, window=btn)
    def create_server():
        time.sleep(0.1)
        root.destroy()
        global ip
        ip = gethostbyname(gethostname())
        server_thread = threading.Thread(target=server.create_server)
        self_client_thread = threading.Thread(target=client.connect_client, args=(ip,))
        server_thread.start()
        self_client_thread.start()
    def connect():
        time.sleep(0.1)
        ip = input_ip_area.get('1.0', 'end')
        input_ip_area.delete('1.0', 'end')
        try:
            client.connect_client(decode(ip))
        except:
            error_label = Image.open('boblox\\chat\\' + 'conn_error.png')
            root.error_label = photoimg(error_label)
            error_label = Button(root, image=root.error_label, width=357, height=169, bd=0)
            place_button(960, 505, error_label)
        else:
            root.destroy()
    input_ip_area = Text(root, height=5)
    input_ip_area.pack(pady=120)
    btn_create_chat = Image.open('boblox\\chat\\' + 'create_chat_button.png')
    btn_connect = Image.open('boblox\\chat\\' + 'connect_button.png')
    root.btn_create_chat = photoimg(btn_create_chat)
    root.btn_connect = photoimg(btn_connect)
    create_chat_button = Button(root, image=root.btn_create_chat, width=415, height=197, command=create_server)
    connect_button = Button(root, image=root.btn_connect, width=330, height=55, command=connect)
    place_button(600, 200, create_chat_button)
    place_button(600, 505, connect_button)



    root.mainloop()