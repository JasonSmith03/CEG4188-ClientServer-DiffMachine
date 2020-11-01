#Authors: Jason Smith, Bradley Rose
#November 1, 2020
#Server application for query messaging

import socket
import threading
import sys

#Global variables
BUFF_SIZE = 2048
HOST = socket.gethostname()
PORT = 55555
CLIENTSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def getMessage():
    '''
        Get the user to type in a querry message and send it to the server
    '''
    while True: 
        #connect user to server and send username
        email = raw_input("Enter email: ")
        CLIENTSOCKET.send(email)

        #Receive welcome statement from server
        serverResponse = CLIENTSOCKET.recv(BUFF_SIZE)
        print(serverResponse)

def main():
    CLIENTSOCKET.connect((HOST, PORT))
    thread = threading.Thread(target=getMessage,)
    thread.start()

if __name__ == "__main__":
    main()