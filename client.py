import socket
import threading

# AF_INET -> iPv4, AF_INET6 -> iPv6, AF - Address Family
# Type of transport layer -> UDP, TCP
def create_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    s.sendall(b"hello world")


for i in range(500):
    t= threading.Thread(target=create_connection())
    t.start()


    # data = s.recv(1024)
    # print(data)
