DLL_PATH = './dlls'
LIB_PATH = './src/libs'
STATIC_FILES_PATH = './src/static'
DB_PATH = './DB'

# reserved for future
REMOTE_DB_HOST = ''
REMOTE_DB_PORT = 3306
REMOTE_DB_USER = ''
REMOTE_DB_PASSWORD = ''

# init
TODAYS_TOKEN = ''
if TODAYS_TOKEN == '':
    with open(DB_PATH+'/secret', 'r')as secret:
        TODAYS_TOKEN = secret.read()
    print('today\'s token :' + TODAYS_TOKEN)
