import threading, socket
import tkinter
import tkinter.scrolledtext
from tkinter import *
from PIL import Image, ImageTk
from boblox.chat.encrypt import encrypt
from vidstream import AudioSender
from vidstream import AudioReceiver

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

            self.ip_text = tkinter.Label(self.canvas, text='                                                                                                                                                                                                                                                                                                                                                  '+'Server ID: {}'.format(encrypt(ip)))
            self.ip_text.grid(row=0, column=0)

            def setup_vc_gui(self):
                def photoimg(img): return ImageTk.PhotoImage(img)
                def place_button(btn_x, btn_y, btn): self.canvas.create_window(btn_x, btn_y, window=btn)
                self.vc_on = 'boblox\\chat\\vcon.png'
                self.vc_off = 'boblox\\chat\\vcoff.png'

                self.vc_mode = self.vc_off
                self.vc_btn = Image.open(self.vc_mode)
                self.win.vc_button = photoimg(self.vc_btn)
                self.vc_button = Button(self.win, image=self.win.vc_button, width=202, height=182)
                place_button(930, 210, self.vc_button)



                def change_vc_mode(self):
                    if self.vc_mode == self.vc_on:
                        self.vc_mode = self.vc_off
                    elif self.vc_mode == self.vc_off:
                        self.vc_mode = self.vc_on
                    self.vc_button
                    setup_vc_gui()

                
            self.setup_vc_gui()

            self.gui_done = True

            self.win.protocol('WM_DELETE_WINDOW', self.stop)

            self.win.mainloop()
        
        def write(self):
            message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
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
    