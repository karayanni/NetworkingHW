from socket import *
from utils import read_message, init_outgoing_socket


def start_proxy(listen_port: int, fake_ip: str, server_ip: str):
    listening_socket = socket(AddressFamily.AF_INET, SOCK_STREAM)

    # listen for connections on the provided port (backlog up to 100 requests)
    listening_socket.bind(('', listen_port))
    listening_socket.listen(100)

    while True:
        try:
            current_client_socket = None
            current_socket_to_server = None

            current_client_socket, addr = listening_socket.accept()
            current_socket_to_server = init_outgoing_socket(server_ip, fake_ip)

            # todo: add the condition to check
            while True:
                # we read the message and save it locally until getting \n
                try:
                    message = read_message(current_client_socket)
                    current_socket_to_server.send(message.encode())

                    response = read_message(current_socket_to_server)
                    current_client_socket.send(response.encode())

                except Exception as exc:
                    current_client_socket.close()
                    current_socket_to_server.close()
                    print("closing connections since one party disconnected")
                    break

        except Exception as exc:
            if current_client_socket is not None:
                current_client_socket.close()
            if current_socket_to_server is not None:
                current_socket_to_server.close()
            print("closing connection with client since server isn't available")
            continue
