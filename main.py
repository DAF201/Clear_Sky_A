import tornado.web
import tornado.ioloop
import tornado.httpserver
from src.libs.path import PATH
app = tornado.web.Application(PATH)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(80)
tornado.ioloop.IOLoop.instance().start()
