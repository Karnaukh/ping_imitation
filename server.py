import socket

sock = socket.socket()
sock.bind(('', 8888))
sock.listen(10)
conn, addr = sock.accept()

while True:

    out_packet = conn.recv(1024)
    # false delay
    i = 0
    while i < 10000:
        i = i + 1
    ###################
    if not out_packet:
        break
    conn.send(out_packet)

conn.close()
