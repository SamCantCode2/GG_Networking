import PyEncry as pe
import socket

ip = socket.gethostbyname(socket.gethostname())
port = 8008
addr = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)
print(f"Connected at {addr[0]}/{addr[1]}")
flag = True
while flag:
    #receive key over here
    msg = input("> ")
    #encrypt here
    client.send(msg.encode('utf-32'))
    if msg == '-disc':
        flag = False
    else:
        reply = client.recv(1024).decode('utf-32')
        #decrypt here
        print(f"> {reply}")
client.close()

