# Patrick Stumbaugh

# code adapted from class textbook: chapter 2.7

import socket  # for socket
import sys  # for user to quit

# what we'll be sending back to client
data = "HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# create socket and set server info
serverName = 'http_server'
serverPort = 7777
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind port number to server socket
serverSocket.bind(('', serverPort))

print
print('Connected at : 127.0.0.1:7777')
print

requestFlag = False  # flag to end request

# wait for requests
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # accept a request
    connectionSocket, addr = serverSocket.accept()
    # receive the request
    sentence = connectionSocket.recv(1024).decode()

    requestFlag = True  # change flag to true

    # print the request
    print('RECEIVED: ')
    print(sentence)
    print
    # print what we're sending to client
    print('SENDING: ')
    print(data)
    print

    # encode data and send back to client
    connectionSocket.send(data.encode())
    connectionSocket.close()  # close socket
    if requestFlag == True:
        break
