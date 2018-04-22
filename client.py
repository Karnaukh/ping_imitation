import struct
import socket
import time
import sys


def ping(addr):
    sock = socket.socket()
    sock.connect((addr, 8888))

    seq_num = 0
    stub = 0

    while seq_num < 4:
        seq_num += 1
        out_packet = struct.pack("!HHd",  stub, seq_num, time.time())

        sock.send(out_packet)
        in_packet = sock.recv(1024)
        (stub, seq, ping_time) = struct.unpack("!HHd", in_packet)

        print("Packet", seq)
        print((time.time() - ping_time) * 1000, "ms")
        time.sleep(1)


if __name__ == '__main__':
    ping(sys.argv[1])
