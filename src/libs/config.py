DLL_PATH = './dlls'
LIB_PATH = './src/libs'
STATIC_FILES_PATH = './src/static'
DB_PATH = './DB'


TODAYS_TOKEN = ''
if TODAYS_TOKEN == '':
    with open(DB_PATH+'/secret', 'r')as secret:
        TODAYS_TOKEN = secret.read()
    print('today\'s token :' + TODAYS_TOKEN)
