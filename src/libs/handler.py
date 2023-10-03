from tornado.web import RequestHandler
from src.libs.account import *
from glob import glob

STATIC_FILES = {}
for file_name in glob('./src/static/*.*'):
    try:
        with open(file_name, 'r')as file:
            STATIC_FILES[file_name.split('\\')[1]] = file.read()
    except:
        with open(file_name, 'rb')as file:
            STATIC_FILES[file_name.split('\\')[1]] = file.read()


class root(RequestHandler):
    def get(self):
        self.write(STATIC_FILES['home.html'])


class login(RequestHandler):
    def get(self):
        self.write('login page')

    def post(self):
        self.write('set cookie for login')


class create_account(RequestHandler):
    def get(self):
        self.write(STATIC_FILES['register.html'])

    def post(self):
        self.write(STATIC_FILES['home.html'])


class account(RequestHandler):
    pass


class API(RequestHandler):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
        self.API_handlers = {'/API?register': self.register}

    def get(self):
        pass

    def post(self):
        self.API_handlers[self.request.uri]()

    def register(self):
        if (self.request.arguments['clearsky_id']
                [0].decode() in account_model['registed_accounts'].keys()):
            self.write(STATIC_FILES['about_blank.html'])
        else:
            register_new_account(self.request.arguments['clearsky_id'][0].decode(
            ), self.request.arguments['clearsky_secret'][0].decode())

            self.write(STATIC_FILES['register_okay.html'])


class STATIC(RequestHandler):
    def get(self, *args):
        if 'script' in self.request.arguments.keys() and self.request.arguments['script'][0].endswith(b'.js'):
            self.write(
                STATIC_FILES[self.request.arguments['script'][0].decode()])
            return
        if 'style' in self.request.arguments.keys() and self.request.arguments['style'][0].endswith(b'.css'):
            self.write(
                STATIC_FILES[self.request.arguments['style'][0].decode()])
            return
        self.write(" ")


class FAVICON(RequestHandler):
    def get(self, *arg):
        self.write(STATIC_FILES['favico.ico'])
