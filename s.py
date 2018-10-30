import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if(data.decode() == 'koniec'):
        break
    print('Received', data.decode())
    txt = input("server: ")
    conn.sendall(txt.encode())
conn.close()