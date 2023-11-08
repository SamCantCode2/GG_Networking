import socket
import threading
import _thread
import PyEncry as pe

ip = socket.gethostbyname(socket.gethostname())
port = 8008
addr = (ip, port)
dc = '-disc'

def clientthread(conn, addr):
    print(f"New connection: {addr[0]}/{addr[1]}")
    flag = True
    while flag:
        #send public keys here
        msg = conn.recv(1024).decode('utf-32')
        #decrypt here
        if msg == dc:
            flag = 0
        print(f"[{addr}]: {msg}")
        reply = input("Enter your reply: ")
        #encrypt here
        conn.send(reply.encode('utf-32'))
    conn.close()

print("Server is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
server.listen()
print(f"Server is listening on {ip}/{port}")
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=clientthread, args=(conn, addr))
    thread.start()
    print(f"Connection Count: {threading.activeCount() - 1}")
