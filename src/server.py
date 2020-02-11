import socket
import sys
from threading import Thread
import thread


def on_new_client(clientsocket, addr):
    msg = 'hi new connection {}'.format(addr)
    clientsocket.send(msg)
    clientsocket.close()


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

while True:
    c, addr = s.accept()
    print('got connection from {}'.format(addr))
    thread.start_new_thread(on_new_client, (c, addr))
