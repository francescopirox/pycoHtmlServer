# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys
import logging

PORT=8000
ADDRESS="localhost"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def init():
    #TODO load_config()
    logging.basicConfig(level=logging.INFO)
    logging.info("PycoHttpServer started!")

def main():
    init()
    ca = ConnectionHandler()
    print_hi('PyCharm')

    while True:
        connection, client_address=ca.accept()
        print(connection)
        print(client_address)
        #TODO refactor in a function callback

class ConnectionHandler:

    def __init__(self,port=PORT):
        super().__init__()
        self.port=port
        try:
            self.sock=sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((ADDRESS,PORT))
            self.sock.listen(1)
            logging.debug("TCP SOCKET START")
        except Exception as e:
            logging.error("TCP SOCKET NOT STARTED",repr(e))

    def __del__(self):
        self.sock.close()
        logging.debug("TCP SOCKET STOP")


    def accept(self):
        connection, client_address = self.sock.accept()
        return connection, client_address



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
