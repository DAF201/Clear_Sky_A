import json
from time import sleep
account_model = {
    'new_account_schema':
    {
        "secret": "",
        "cookie": "",
        "repo": {},
        "alies": {},
        "email": {},
        "inbox": {},
        "reqeust": {}
    },
    'alies_schema': {},
    'registed_accounts': {},
    'online_accounts': {}
}


account_update_queue = []

ACCOUNT_UPDATER_EXEC = 1

with open('./DB/ac.json', 'r')as ac:
    registed_accounts = json.load(ac)


def register_new_account(id, secret):
    temp = account_model["new_account_schema"]
    temp['secret'] = secret
    registed_accounts[id] = temp
    with open('./DB/ac.json', 'w')as DB:
        json.dump(registed_accounts, DB)


def accounts_update_tool():
    while (ACCOUNT_UPDATER_EXEC):
        print('testing')
        sleep(5)
