# Patrick Stumbaugh

# background info I found on end of message for sockets from:
# https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be
# the code is similar to my other "connect_socket.py" file, which I modified to include a loop until no bytes are left to be read


import socket  # for socket
import sys  # for user to quit

# create socket and set server info
serverName = 'gaia.cs.umass.edu'
serverPort = 80
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect and send GET message to server:
clientSocket.connect((serverName, serverPort))
sentence = 'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
clientSocket.send(sentence.encode())  # send the message

fullMessage = ''  # initialise fulleMessage string

while True:  # see if there are any bytes to print still
    # receive the message
    modifiedSentence = clientSocket.recv(1024)
    # check if any bytes are left, if so, add to fullMessage and loop around, else break
    if len(modifiedSentence) <= 0:
        break
    # add part of our message to the full message
    fullMessage += modifiedSentence.decode('UTF-8')

print('[RECV] - length: %s' % (len(fullMessage)))  # length of message
print
print(fullMessage)  # message

# close the socket connection
clientSocket.close()
