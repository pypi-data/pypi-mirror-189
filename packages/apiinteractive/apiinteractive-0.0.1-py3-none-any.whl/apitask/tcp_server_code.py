"""
This module is the TCP Server and the Client as well
"""
import sys
import socket
import threading
import socketserver
returned_data = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """A Threaded TCP Request Handler Class"""

    def handle(self):
        """Handle Method for Request Handler Class"""

        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """A Threaded TCP Server Class"""

def client(ip_address, port, message):
    """
    This function is the client for the TCP Server

    Args:
        ip: is a value of type string mentioning the ip network
        port: is number of type int specifying the port number
        message: is the value of type string mentioning the message/data to be sent to server

    Returns:
        There is no implicit return, we are saving 
        every response in the returned_data list
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip_address, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        returned_data.append(response)

def start_server_tcp(list_cmd):
    """This function starts the TCP Server

    Args:
        list_cmd is a list of commands which are to executed
        by the server, each element must be of type string

    Return:
        returns a list of saved responses
    """
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip_address, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        for cmd in list_cmd:
            client(ip_address,port,cmd)
        server.shutdown()
        return returned_data

if __name__ == "__main__":
    start_server_tcp(sys.argv[1])
