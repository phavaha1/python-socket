import socket
import sys

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

    c.send('Thank for connection'.encode())
    c.close()
