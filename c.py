import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
while 1:
    txt = input("client: ")
    s.sendall(txt.encode())
    if(txt == 'koniec'):
        break
    data = s.recv(1024)
    print('Received', data.decode())
s.close()