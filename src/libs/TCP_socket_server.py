from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
# when seprately debugging
try:
    from src.libs.network import LOCAL_HOST, TCP_SOCKET_PORT, TCP_PACKAGE_GLOBAL_MAX_LENGTH
except:
    from network import LOCAL_HOST, TCP_SOCKET_PORT, TCP_PACKAGE_GLOBAL_MAX_LENGTH
from ctypes import *


class ThreadedTCPRequestHandler(BaseRequestHandler):
    def handle(self):
        print(self.client_address[0])
        while (True):
            data = self.request.recv(TCP_PACKAGE_GLOBAL_MAX_LENGTH)
            if data:
                print(bin(int.from_bytes(data, 'little'))[2:].zfill(8))
            else:
                break

        # test = open('test.mp4', 'ab')
        # while (True):
        #     data = self.request.recv(TCP_PACKAGE_GLOBAL_MAX_LENGTH)
        #     if data:
        #         print(bin(int.from_bytes(data, 'little'))[2:].zfill(8))
        #         self.request.sendall(b"okay")
        #     else:
        #         break
        # test.close()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


sock_server = ThreadedTCPServer(
    (LOCAL_HOST, TCP_SOCKET_PORT), ThreadedTCPRequestHandler)

sock_server.serve_forever()
