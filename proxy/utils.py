from socket import *


def read_message(open_socket: socket):
    """
    reads and decodes the next message from a socket until the first \n
    :param open_socket: the socket from which we want tor read
    :return: the complete message decoded
    """
    message = open_socket.recv(4096).decode()
    while not message[-1] == '\n':
        temp_message = open_socket.recv(2048).decode()
        message += temp_message

    print("received message: " + message)
    return message


def init_outgoing_socket(server_ip: str, fake_ip: str):
    """
    initializes the socket connect to the server with the specified configs.
    :param server_ip: the server IP address
    :param fake_ip: the IP to bind to our outgoing socket
    :return: the newly established socket if success
    """
    socket_to_server = socket(AF_INET, SOCK_STREAM)

    # port is hardcoded 8080
    socket_to_server.bind((fake_ip, 0))
    socket_to_server.connect((server_ip, 8080))
    # as requested we should bind the outbound connection to the fake IP

    return socket_to_server
