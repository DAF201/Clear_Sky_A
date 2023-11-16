from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from threading import Thread
from ctypes import *
from subprocess import Popen
from src.libs.tools import helper_tool
from src.libs.path import ROUTE_PATH
from src.libs.module_loader import MODULES

processes = {}

# socket server
processes['clearsky_socket'] = Popen(
    'python ./src/libs/TCP_socket_server.py')

accounts_update = Thread(target=helper_tool)
accounts_update.daemon = True
accounts_update.start()

app = Application(ROUTE_PATH)
http_server = HTTPServer(app)
http_server.listen(80)

for module in MODULES:
    try:
        processes[module['id']] = Popen(
            'python %smain.py' % (module['path']))
        if processes[module['id']]:
            print('module ' + module['id'] + ' loaded')
    except:
        print('failed to load module: %s' % (module['id']))

IOLoop.instance().start()
