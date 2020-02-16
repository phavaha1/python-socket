import socket
import sys
from threading import Thread
import thread


def on_new_client(clientsocket, addr):
    notice_msg = 'Client ' + str(addr) + ' has joined the chat'
    broadcast(addr, notice_msg)
    while True:
        recv_msg = clientsocket.recv(128)
        broadcast(addr, recv_msg)


def broadcast(addr, msg):
    for con in connections:
        con.send(str(addr) + ': ' + msg)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket created successfully')
except socket.error:
    print('socket creation failed')
    sys.exit()

port = 12345

s.bind(('', port))

s.listen(5)
print('socket is listening')

connections = []

while True:
    c, addr = s.accept()
    connections.append(c)
    print('got connection from {}'.format(addr))
    thread.start_new_thread(on_new_client, (c, addr))
