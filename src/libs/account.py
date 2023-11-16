from json import load

# for socket_server to import account_module without causing path error
DLL_loaded = 0

account_module = {
    # save some space, no specific meaning
    'new_account_schema':
    {
        'secret': '',
        'email': '',
        'shared_token': ''
    },
    'temp_token_schema': {
        'id': '',  # user if of the temp token owner
        'repo': '',  # which repo is this token for
        'access': 'rwd',  # what access does this token provide
        'shell': False  # can this token be used to compile exe on server shell
    },
    'registed_accounts': {},
    # http auth need this
    'id_secret_combo': {},
    'temp_tokens': {},
    'update_required': 0,
    'update_alive': 1
}

# load on start
with open('./DB/ac.json', 'r')as ac:
    account_module['registed_accounts'] = load(ac)

# create combo for http auth
for key in account_module['registed_accounts'].keys():
    account_module['id_secret_combo'][key] = account_module['registed_accounts'][key]['secret']

# for new account register, require the token to register new account


def register_new_account(id, secret, email='email@email.email', shared_token=''):
    global DLL_loaded
    # check if DLL loaded, this will cause path error if placed at the begining
    if DLL_loaded == 0:
        from src.libs.external_tools import rand_dll
        DLL_loaded = 1

    temp = account_module['new_account_schema']
    temp['secret'] = secret
    # may change in the future, but right now doesn't look really important so just left with default example email
    temp['email'] = email

    # generate shared token for others to access
    if shared_token == '':
        temp['shared_token'] = (rand_dll.random_str(8)).decode()
    else:
        temp['shared_token'] = shared_token

    account_module['registed_accounts'][id] = temp
    account_module['update_required'] = 1
    account_module['id_secret_combo'][id] = account_module['registed_accounts'][id]['secret']
