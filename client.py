import config
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

def main():
    sock.listen(1)
    conn, addr = sock.accept()
    pass


if __name__ == '__main__':
    main()