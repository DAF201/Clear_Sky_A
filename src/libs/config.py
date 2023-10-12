DLL_PATH = '/dlls'
LIB_PATH = '/src/libs'
STATIC_FILES_PATH = '/src/static/'

HOST = '0.0.0.0'
PORT = 80

SOCKET_HOST = '0.0.0.0'
SOCKET_PORT = 920

TODAYS_TOKEN = ''
if TODAYS_TOKEN == '':
    with open('./DB/secret', 'r')as secret:
        TODAYS_TOKEN = secret.read()
    print('today\'s token :' + TODAYS_TOKEN)
