import socket
from response_protocol import *

class SocketWrapper(object):
    def __init__(self, socket: socket.socket):
        self.socket = socket

    def recv_data(self):
        return self.socket.recv(RECV_BUFFER_SIZE).decode('UTF-8')

    def send_data(self, message):
        return self.socket.send(message.encode('UTF-8'))