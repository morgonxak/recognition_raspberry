import socket
import json

sock = socket.socket()
sock.bind(('', 9000))
sock.listen(1)
flag = True

while True:
    conn, addr = sock.accept()

    print('connected:', addr)

    data = conn.recv(0)
    if not data:
        continue
    data = data.decode()
    data = json.loads(data)
    print(len(data))
    print(data)

    if flag:
        conn.send(b'1')
        flag = not flag
    else:
        conn.send(b'0')
        flag = not flag

    conn.close()
    #conn.send(data.upper())

conn.close()