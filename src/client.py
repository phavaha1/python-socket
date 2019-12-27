import socket


s = socket.socket()
port = 12345

s.connect(('vnlab-master3.com', port))

print(s.recv(20))

s.close()
