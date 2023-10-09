import tornado.web
import tornado.ioloop
import tornado.httpserver
from src.libs.path import PATH
from ctypes import *
import threading
from subprocess import Popen
from src.libs.account import accounts_update_tool

cmd_lib = cdll.LoadLibrary(r'./dlls/cmd.dll')

# cmd_lib.cmd(b"python ./src/libs/socket_server.py")

# socket server
# Popen("python ./src/libs/socket_server.py")

accounts_update = threading.Thread(target=accounts_update_tool)
accounts_update.daemon = True
accounts_update.start()

app = tornado.web.Application(PATH)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(80)

tornado.ioloop.IOLoop.instance().start()
