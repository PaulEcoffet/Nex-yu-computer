import socket

class Server:
    """Server which will receive the broadcast sent by
    the application"""
    
    def __init__(self):
        """Init the server"""
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.bind('', );
        

