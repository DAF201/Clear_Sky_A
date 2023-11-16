from _socket import _RetAddress
from socketserver import _RequestType, BaseRequestHandler, BaseServer, ThreadingMixIn, TCPServer
from ctypes import *
from src.libs.protocol import clearsky_protocol

LOCAL_HOST = '127.0.0.1'
TCP_SOCKET_PORT = 920


class ThreadedTCPRequestHandler(BaseRequestHandler):

    def __init__(self, request: _RequestType, client_address: _RetAddress, server: BaseServer) -> None:
        super().__init__(request, client_address, server)
        self.decoder = clearsky_protocol()

    def handle(self):
        self.request.send(b'connected')
        while (True):
            data = self.request.recv(1024)
            if data == b'':
                return
            print(data)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


ThreadedTCPServer((LOCAL_HOST, TCP_SOCKET_PORT),
                  ThreadedTCPRequestHandler).serve_forever()
