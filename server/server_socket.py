import socket as sc
from config import *

class ServerSocket(sc.socket):
    def __init__(self):
        # IPv4 TCP type
        super(ServerSocket, self).__init__(sc.AF_INET, sc.SOCK_STREAM)

        # bind address and port
        self.bind((SERVER_IP, SERVER_PORT))

        # listen model
        self.listen(MAX_CONNECTIONS)