from tornado.web import RequestHandler
from os import getcwd
STATIC_HTML = getcwd()+"/src/static/%s"


class root(RequestHandler):
    def get(self):
        self.render(STATIC_HTML % "home.html")

    def post(self):
        self.write('NOTHING HERE')


class login(RequestHandler):
    def get(self):
        self.write('login page')

    def post(self):
        self.write('set cookie for login')


class create_account(RequestHandler):
    pass


class account(RequestHandler):
    pass
