from tornado.web import RequestHandler
from src.libs.account import account_module, register_new_account
from glob import glob
from tornado_http_auth import auth_required, DigestAuthMixin
from json import dumps
from src.libs.config import TODAYS_TOKEN, STATIC_FILES_PATH

# load all files in static directory
STATIC_FILES = {}

# load all to memeory to speed up
for file_name in glob(STATIC_FILES_PATH+'/*.*'):
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

        # handle different params using the same URL
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

        # user name not in 2-16 characters or secret not in 4-16 or already registed
        if (user_name in account_module['registed_accounts'].keys()) or len(user_name) not in range(2, 16) or len(secret) not in range(4, 16):
            self.write(STATIC_FILES['about_blank.html'])
        else:
            # email not enabled yet
            register_new_account(user_name, secret)
            self.write(STATIC_FILES['register_okay.html'])

    # require auth to see the account page
    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def account(self):
        self.write(STATIC_FILES['account.html'])

    # an API for frontend to get account info
    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def account_info(self):
        self.write(dumps(account_module['registed_accounts'][self.request.headers.get(
            'Authorization').split(',')[0].split(' ')[1].replace('username=', '').replace('\"', '')]))

    # overwrite the saved auth by sendback a 401
    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def account_logout(self):
        self.send_error(401)


class account_modify(DigestAuthMixin, RequestHandler):
    # midify account, may be I should move this to API also?
    @auth_required(realm='Protected', auth_func=account_module['id_secret_combo'].get)
    def post(self):
        # update info
        user_name = self.request.headers.get('Authorization').split(',')[0].split(' ')[
            1].replace('username=', '').replace('\"', '')
        account_module['registed_accounts'][user_name]['email'] = self.request.arguments['email'][0].decode()
        account_module['registed_accounts'][user_name]['secret'] = self.request.arguments['secret'][0].decode()
        account_module['registed_accounts'][user_name]['shared_token'] = self.request.arguments['shared_token'][0].decode()
        account_module['id_secret_combo'][user_name] = self.request.arguments['secret'][0].decode()

        # make as update needed
        if not account_module['update_required']:
            account_module['update_required'] = 1

        self.write(STATIC_FILES['okay.html'])


class STATIC(RequestHandler):
    # for front end to get get JS and CSS, maybe should be moved to API
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
    # frontend get FAVICON
    def get(self, *arg):
        self.write(STATIC_FILES['favico.ico'])
