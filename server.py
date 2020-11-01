#Authors: Jason Smith, Bradley Rose
#November 1, 2020
#Server application for query messaging

import socket
import threading
import sys

#Global Variables
PORT = 55555
HOST = socket.gethostname()
BUFF_SIZE = 2048
SERVERSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def querryResponse(clientHost):
    ''' 
        Returns data from the database to the client upon receiving querry message
    '''
    while True:
        querry = clientHost.recv(BUFF_SIZE)
        print("Querry: {}\n".format(querry))
        with open("database.txt", 'r') as f:
            for i in f:
                if(querry in i):
                    data = i
                    break
                else:
                    data = "Not in database."
            
        clientHost.send(data)


def main():
    #initalize server
    try: 
        SERVERSOCKET.bind((HOST, PORT)) 
    except socket.error as e:
        print(e)
    SERVERSOCKET.listen(5) 
    print("server is ready and listenting on {} : {}\n".format(HOST, PORT))

    while True:
        #accept connection requests from client(s)
        clientHost, clientPort = SERVERSOCKET.accept() # returns (host, port)

        thread = threading.Thread(target=querryResponse, args=(clientHost,))
        thread.start()


if __name__ == "__main__":
    main()