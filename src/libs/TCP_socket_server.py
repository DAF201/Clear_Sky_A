from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
from ctypes import *
try:
    from src.libs.protocol import clearsky_protocol
except:
    from protocol import clearsky_protocol
LOCAL_HOST = '127.0.0.1'
TCP_SOCKET_PORT = 920


class ThreadedTCPRequestHandler(BaseRequestHandler):

    def __init__(self, request, client_address, server) -> None:
        super().__init__(request, client_address, server)
        self.decoder = clearsky_protocol()

    def handle(self):
        self.request.send(int.to_bytes(200))
        message = self.request.recv(1024)
        
        while (True):
            data = self.request.recv(1024)
            if data == b'':
                return
            print(data)

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


ThreadedTCPServer((LOCAL_HOST, TCP_SOCKET_PORT),
                  ThreadedTCPRequestHandler).serve_forever()
