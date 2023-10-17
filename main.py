import tornado.web
import tornado.ioloop
import tornado.httpserver
from threading import Thread
from ctypes import *
from subprocess import Popen
from src.libs.tools import helper_tool
from src.libs.path import ROUTE_PATH
# cmd_lib = cdll.LoadLibrary(r'./dlls/cmd.dll')

# socket server
Popen("python ./src/libs/TCP_socket_server.py", shell=True)

accounts_update = Thread(target=helper_tool)
accounts_update.daemon = True
accounts_update.start()

app = tornado.web.Application(ROUTE_PATH)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(80)

tornado.ioloop.IOLoop.instance().start()
