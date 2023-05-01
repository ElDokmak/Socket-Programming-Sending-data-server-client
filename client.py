import socket
import threading

PORT = 5050
FORMAT = "utf-8"
D = "DES"
HEADER = 64
SERVER = "172.22.128.1"
# 172.22.128.1
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    MSG = msg.encode(FORMAT)
    msg_len = len(MSG)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(MSG)


def read():
    msg_len = client.recv(HEADER).encode(FORMAT)
    if msg_len:
        msg_len = int(msg_len)
        msg = client.recv(msg_len).decode(FORMAT)


x = ''
while 1:
    x = input()
    if x != 'DES':
        send(x)
    thread = threading.Thread(target=read)
    thread.start()

send(D)
