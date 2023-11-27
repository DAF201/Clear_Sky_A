from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
from ctypes import *
try:
    from src.libs.protocol import clearsky_protocol
except:
    from protocol import clearsky_protocol
try:
    from src.libs.module_loader import MODULES_LIST
except:
    from module_loader import MODULES_LIST

from socket import socket, SOCK_STREAM, AF_INET

LOCAL_HOST = '127.0.0.1'
EXTERNAL_HOST = '0.0.0.0'
TCP_SOCKET_PORT = 920

decoder = clearsky_protocol()


class ThreadedTCPRequestHandler(BaseRequestHandler):

    def handle(self):
        self.request.send(b'<clearsky>auth_required<clearsky>')
        auth = self.request.recv(1024)

        if decoder.auth(auth):
            self.request.send(b'<clearsky>okay<clearsky>')
        else:
            return

        while (True):
            data = self.request.recv(1024)

            if data == b'' or data == b'<clearsky>exit<clearsky>':
                return

            target = decoder.type(data)
            if target == 'clearsky':
                return

            if MODULES_LIST[target]:
                try:
                    s = socket(AF_INET, SOCK_STREAM)
                    s.connect((MODULES_LIST[target]))
                    s.settimeout(3)
                    data = decoder.sub_prot(data)
                    if data:
                        s.send(data)
                    self.request.send(b'<clearsky>'+s.recv(1024)+b'<clearsky>')
                except:
                    self.request.send(b'<clearsky>failed<clearsky>')


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


ThreadedTCPServer(('0.0.0.0', TCP_SOCKET_PORT),
                  ThreadedTCPRequestHandler).serve_forever()
