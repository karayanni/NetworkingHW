from socket import *


if __name__ == '__main__':
    serverPort = 8080
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(10)
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()

    connectionSocket.settimeout(10000)

    message = connectionSocket.recv(2048).decode()
    while not message[-1] == '\n':
        temp = connectionSocket.recv(2048).decode()
        message += temp

    if len(message) == 10015:
        print(f'NICE: received a message of length: {len(message)} \n \n the message: {message}')
    else:
        print(f'Failed sending big message, check ur code..')

    connectionSocket.send(f'received a message of length: {len(message)}\n'.encode())

    try:
        message = connectionSocket.recv(2048).decode()
        if message != '':
            print(f'received fucked up message: {message}, should receive empty message...')
        else:
            print("success! server received 0 bytes - close request.")
    except Exception as exc:
        print("server timed out = check that the proxy closes the conenction")
