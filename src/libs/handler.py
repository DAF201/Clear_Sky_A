from tornado.web import RequestHandler
from src.libs.account import account_module, register_new_account
from glob import glob
from tornado_http_auth import auth_required, DigestAuthMixin
from json import dumps
from src.libs.config import TODAYS_TOKEN

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

    def post(self):
        self.write('method not allowed')


class create_account(RequestHandler):
    def get(self):
        self.write(STATIC_FILES['register.html'])

    def post(self):
        self.write(STATIC_FILES['home.html'])


class API(DigestAuthMixin, RequestHandler):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
        self.API_handlers = {
            'post': {
                '/API?account_register': self.account_register
            },
            'get': {
                '/API?account': self.account,
                '/API?account_info': self.account_info,
                '/API?account_logout': self.account_logout
            }
        }

    def get(self):
        self.API_handlers['get'][self.request.uri]()

    def post(self):
        self.API_handlers['post'][self.request.uri]()

    def account_register(self):
        user_name = self.request.arguments['clearsky_id'][0].decode()
        secret = self.request.arguments['clearsky_secret'][0].decode()
        token = self.request.arguments['clearsky_token'][0].decode()
        if token != TODAYS_TOKEN:
            self.write('SERVER TOKEN FAILED')
            return
        if len(user_name) not in range(2, 16) or len(secret) not in range(4, 16) or (user_name in account_module['registed_accounts'].keys()):
            self.write(STATIC_FILES['about_blank.html'])
        else:
            register_new_account(user_name, secret)
            self.write(STATIC_FILES['register_okay.html'])

    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def account(self):
        self.write(STATIC_FILES['account.html'])

    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def account_info(self):
        self.write(dumps(account_module['registed_accounts'][self.request.headers.get(
            'Authorization').split(',')[0].split(' ')[1].replace('username=', '').replace('\"', '')]))

    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def account_logout(self):
        self.send_error(401)


class account_modify(DigestAuthMixin, RequestHandler):

    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def post(self):
        user_name = self.request.headers.get('Authorization').split(',')[0].split(' ')[
            1].replace('username=', '').replace('\"', '')
        account_module['registed_accounts'][user_name]['email'] = self.request.arguments['email'][0].decode()
        account_module['registed_accounts'][user_name]['secret'] = self.request.arguments['secret'][0].decode()
        account_module['registed_accounts'][user_name]['shared_token'] = self.request.arguments['shared_token'][0].decode()
        account_module['id_secret_combo'][user_name] = self.request.arguments['secret'][0].decode()
        account_module['update_required'] = 1
        self.write(STATIC_FILES['okay.html'])


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
        self.write(' ')


class FAVICON(RequestHandler):
    def get(self, *arg):
        self.write(STATIC_FILES['favico.ico'])
