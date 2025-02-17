from server_socket import ServerSocket

class Server(object):
    # server core
    def __init__(self):
        self.server_socket = ServerSocket()

    def startup(self):
        """ get client connection """
        socket, addr = self.server_socket.accept()

        """ receive data from client """
        recv_data = socket.recv(512)
        print(recv_data.decode('UTF-8'))

        """ send data to client """
        socket.send("success!".encode('UTF-8'))

        """ close client connection """
        socket.close()

if __name__ == '__main__':
    Server().startup()