from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
from ctypes import *
try:
    from src.libs.protocol import clearsky_protocol
except:
    from protocol import clearsky_protocol
try:
    from src.libs.module_loader import MODULES_ADDRESS
except:
    from module_loader import MODULES_ADDRESS

from socket import socket, SOCK_STREAM, AF_INET

LOCAL_HOST = '127.0.0.1'
EXTERNAL_HOST = '0.0.0.0'
TCP_SOCKET_PORT = 920

# clearsky protocol decoder instance
decoder = clearsky_protocol()


class ThreadedTCPRequestHandler(BaseRequestHandler):

    def handle(self):
        self.request.settimeout(5)
        # send the auth required to notify connected
        self.request.send(b'<clearsky>auth_required<clearsky>')
        auth = self.request.recv(1024)

        # check auth
        if decoder.auth(auth):
            self.request.send(b'<clearsky>okay<clearsky>')
        else:
            return

        # connect
        while (True):
            data = self.request.recv(1024)

            if data in (b'', b'<clearsky>exit<clearsky>'):
                return

            # get sub_protocol type
            target = decoder.type(data)

            # not yet accessable
            if target == 'clearsky':
                return

            # get the host and port of the sub_protocol target
            if MODULES_ADDRESS[target]:
                try:
                    # create socket
                    s = socket(AF_INET, SOCK_STREAM)
                    s.connect((MODULES_ADDRESS[target]))
                    s.settimeout(3)

                    # try get data from requrest
                    data = decoder.sub_prot(data)

                    if data:
                        # send data to target sub_protocol machine
                        s.send(data)

                    # send data back to client
                    self.request.send(b'<clearsky>'+s.recv(1024)+b'<clearsky>')

                except Exception as e:
                    print(e)
                    self.request.send(b'<clearsky>failed<clearsky>')


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    # multi-thread
    pass


ThreadedTCPServer(('0.0.0.0', TCP_SOCKET_PORT),
                  ThreadedTCPRequestHandler).serve_forever()
