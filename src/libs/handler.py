from tornado.web import RequestHandler


class root(RequestHandler):
    def get(self):
        self.write('HOME')

    def post(self):
        self.write('NOTHING HERE')


class root_login(RequestHandler):
    def get(self):
        self.write('login page')

    def post(self):
        self.write('set cookie for login')

