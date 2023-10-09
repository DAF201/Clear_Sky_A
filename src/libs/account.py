from json import dump, load
from time import sleep
from src.libs.external_tools import rand_dll
account_module = {
    # save some space, no specific meaning
    'new_account_schema':
    {
        'secret': '',
        'email': '',
        'shared_token': ''
    },
    'registed_accounts': {},
    # http auth need this
    'id_secret_combo': {},
    'update_required': 0
}


with open('./DB/ac.json', 'r')as ac:
    account_module['registed_accounts'] = load(ac)


for key in account_module['registed_accounts'].keys():
    account_module['id_secret_combo'][key] = account_module['registed_accounts'][key]['secret']

# print(account_module['id_secret_combo'])


def register_new_account(id, secret, email='email@email.email', shared_token=''):
    temp = account_module['new_account_schema']
    temp['secret'] = secret
    temp['email'] = email
    if shared_token == '':
        temp['shared_token'] = (rand_dll.random_str(8)).decode()
    else:
        temp['shared_token'] = shared_token
    account_module['registed_accounts'][id] = temp
    with open('./DB/ac.json', 'w')as DB:
        dump(account_module['registed_accounts'], DB)
    account_module['id_secret_combo'][id] = account_module['registed_accounts'][id]['secret']


def accounts_update_tool():
    # TODO:auto update
    return
    while (account_module['ACCOUNT_UPDATER_EXEC']):
        print('testing')
        sleep(5)
