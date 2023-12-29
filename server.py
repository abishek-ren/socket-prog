import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen()


def handleConnection(conn_socket, address):
    print(conn_socket)
    print(address)
    time.sleep(1)


while True:
    conn_socket, address = s.accept()
    thread = threading.Thread(target=handleConnection, args=(conn_socket, address))
    thread.start()
    print("number of Thread objects currently alive" + str(threading.active_count()))
