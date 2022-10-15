import threading, socket

def create_server():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 2070

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    clients = []
    nicknames = []

    def broadcast(message):
        for client in clients:
            client.send(message)
            

    def handle(client):
        while True:
            try:
                message = client.recv(1024)
                print(f'{nicknames[clients.index(client)]} says {message}')
                broadcast(message)
            except:
                index = clients.index(client)
                if client == clients[0]: server.close()
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)
                break

    def receive():
        while True:
            client, address = server.accept()
            print(f'connected with {str(address)}')


            nickname = client.recv(1024)
            nickname = nickname.split('BOBLOX.CODES.SEND'.encode('utf-8'))[0]

            nicknames.append(nickname)
            clients.append(client)

            print(f'Nickname is {nickname}')

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
    receive()
