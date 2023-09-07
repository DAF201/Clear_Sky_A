from tornado.web import RequestHandler


class root(RequestHandler):
    def get(self):
        self.write('HOME')

    def post(self):
        self.write('NOTHING HERE')
