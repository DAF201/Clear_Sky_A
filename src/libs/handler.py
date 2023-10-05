from tornado.web import RequestHandler
from src.libs.account import account_model, register_new_account
from glob import glob
from tornado_http_auth import auth_required, DigestAuthMixin
from src.libs.external_tools import math_dll
from re import match

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


class account(DigestAuthMixin, RequestHandler):
    @auth_required(realm='Protected', auth_func=account_model['id_secret_combo'].get)
    def get(self):
        auth_data = self.request.headers.get(
            'Authorization').split(None, 1)[-1]
        user_name = match('username=\"\w{2,16}\"', auth_data).group(0)
        print(user_name)
        self.write('success')


class API(RequestHandler):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
        self.API_handlers = {
            '/API?register': self.register,
            'API?account': self.account
        }

    def get(self):
        self.finish()

    def post(self):
        self.API_handlers[self.request.uri]()

    def register(self):
        user_name = self.request.arguments['clearsky_id'][0].decode()
        secret = self.request.arguments['clearsky_secret'][0].decode()
        if len(user_name) not in range(3, 16) or len(secret) not in range(6, 16) or (user_name in account_model['registed_accounts'].keys()):
            self.write(STATIC_FILES['about_blank.html'])
        else:
            register_new_account(user_name, secret)
            self.write(STATIC_FILES['register_okay.html'])

    def account(self):
        pass


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
