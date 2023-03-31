import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    massage = input("-> ")
    while massage != "q":
        s.send(massage.encode("utf-8"))
        data = s.recv(1024).decode("utf-8")
        print("Rcevied from server: " + data)
        massage = input("->")
    s.close()

if __name__=="__main__":
    Main()
        
