import socket
import time

listen_socket = socket.socket()
port = 5000
maxConnections = 999
IP = socket.gethostname()

listen_socket.bind("", Port)

listen_socket.listen(maxConnections)
print("Server started at "+IP+" onn port "+str(Port))

(clientsocket, address) = listen_socket.accept()
print("New connection made!")

running = True;

while running:
    message = clientsocket.recv(1024).decode()
    print(message)
    if not message == "":
        # do something
    else:
        clientsocket.close()
        running = False;
