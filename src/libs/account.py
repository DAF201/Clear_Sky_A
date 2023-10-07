import json
from time import sleep
account_module = {
    # save some space, no specific meaning
    'new_account_schema':
    {
        'secret': '',
        'repo': {},
        'email': {},
        'inbox': {},
        'reqeust': {}
    },
    'repo_schema': {
        'name': '',
        'path': '',
        'current_version': '',
        'alies': {
            'alies_name': []
        }
    },
    'registed_accounts': {},
    'account_update_queue': [],
    'ACCOUNT_UPDATER_EXEC': 1,
    # http author need this
    'id_secret_combo': {}
}


account_update_queue = []


with open('./DB/ac.json', 'r')as ac:
    account_module['registed_accounts'] = json.load(ac)


for key in account_module['registed_accounts'].keys():
    account_module['id_secret_combo'][key] = account_module['registed_accounts'][key]['secret']

# print(account_module['id_secret_combo'])


def register_new_account(id, secret):
    temp = account_module['new_account_schema']
    temp['secret'] = secret
    account_module['registed_accounts'][id] = temp
    with open('./DB/ac.json', 'w')as DB:
        json.dump(account_module['registed_accounts'], DB)


def accounts_update_tool():
    # TODO:auto update
    return
    while (account_module['ACCOUNT_UPDATER_EXEC']):
        print('testing')
        sleep(5)
