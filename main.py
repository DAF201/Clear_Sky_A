from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from threading import Thread
from ctypes import *
from subprocess import Popen
from src.libs.tools import helper_tool
from src.libs.path import ROUTE_PATH
from src.libs.module_loader import MODULES

# all the processes stored here for future usage
processes = {}

# socket server
processes['clearsky_socket'] = Popen(
    'python ./src/libs/TCP_socket_server.py')

# state machine thread
helper_tools = Thread(target=helper_tool)
helper_tools.daemon = True
helper_tools.start()

app = Application(ROUTE_PATH)
http_server = HTTPServer(app)
http_server.listen(80)

# load all the modules and run them
for module in MODULES:
    try:
        processes[module['id']] = Popen(
            'python %smain.py' % (module['path']))
        if processes[module['id']]:
            print('module ' + module['id'] + ' loaded')
    except Exception:
        print('failed to load module: %s' % (module['id']))

IOLoop.instance().start()
