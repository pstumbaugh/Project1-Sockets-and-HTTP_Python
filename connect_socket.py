# Patrick Stumbaugh

# code adapted from:
# https://www.geeksforgeeks.org/socket-programming-python/


import socket  # for socket
import sys  # for user to quit

# create socket and set server info
serverName = 'gaia.cs.umass.edu'
serverPort = 80
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect and send GET message to server:
clientSocket.connect((serverName, serverPort))
sentence = 'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
clientSocket.send(sentence.encode())  # send the message

modifiedSentence = clientSocket.recv(1024)  # receive the message

# print results from server
print
print('[RECV] - length: %s' % (len(modifiedSentence)))  # length of message
print(modifiedSentence.decode('UTF-8'))  # message

# close the socket connection
clientSocket.close()
