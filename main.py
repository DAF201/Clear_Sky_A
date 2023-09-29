import tornado.web
import tornado.ioloop
import tornado.httpserver
from src.libs.path import PATH
from ctypes import *
import threading
from subprocess import Popen
cmd_lib = cdll.LoadLibrary(r'./dlls/cmd.dll')

# cmd_lib.cmd(b"python ./src/libs/socket_server.py")

Popen("python ./src/libs/socket_server.py")

app = tornado.web.Application(PATH)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(80)

tornado.ioloop.IOLoop.instance().start()
