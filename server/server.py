from server_socket import ServerSocket
from socket_wrapper import SocketWrapper

class Server(object):
    # server core
    def __init__(self):
        self.server_socket = ServerSocket()

    def startup(self):
        """ get client connection """
        socket, addr = self.server_socket.accept()

        """ receive data from client """
        client_socket = SocketWrapper(socket)
        print(client_socket.recv_data())

        """ send data to client """
        client_socket.send_data("i am server")
        
        """ close client connection """
        socket.close()

if __name__ == '__main__':
    Server().startup()