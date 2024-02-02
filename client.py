import socket
import threading




HEADER=64
PORT =5050
SERVER ="192.168.1.108"
FORMAT ="utf-8"
DISCONNECT = "!DISCONNECTED"

ADDR =(SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)


def send(msg):
    
    
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    print(send_len)
    send_len += b' ' *(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)



while True:

        chat =input("Message: ")    
        send(chat)       
    