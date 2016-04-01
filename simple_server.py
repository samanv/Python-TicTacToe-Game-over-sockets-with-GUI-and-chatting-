import socket
from _thread import *
import asyncore

__author__ = "saman v"


class GameServer:

    def __init__(self):

        # Game parameters
        board = [None] * 9
        turn = 1

        # TCP parameters specifying
        self.tcp_ip = socket.gethostname()
        self.tcp_port = 9999
        self.buffer_size = 2048

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.bind((self.tcp_ip, self.tcp_port))
        except:
            print("socket error, Please try again! ")

        self.s.listen(5)
        print('Waiting for a connection...')

    def messaging(self, conn):

        while True:
            data = conn.recv(self.buffer_size)
            if not data:
                break

            print("This data from client:", data)

    def thread_run(self):
        while True:
            conn, addr = self.s.accept()
            print('connected to: ' + addr[0] + " : " + str(addr[1]))
            start_new_thread(self.messaging, (conn,))



def main():
    gameserver = GameServer()
    gameserver.thread_run()

if __name__ == '__main__':
    main()

