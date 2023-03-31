import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    s  = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    print("Conection from: "+str(addr))
    try:
        while True:
            data = c.recv(1024).decode("utf-8")
            if not data:
                print("No data found")
                break
            print("From connnected user: " + data)
            data = data.upper()
            print("Sending: "+ data)
            c.send(data.encode("utf-8"))
    except:
         print("Lost connection with "+str(addr))
    finally:
        c.close()

if __name__=="__main__":
    print("Server started\n")
    Main()
