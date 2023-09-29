import json

new_account = {
    "secret": "",
    "cookie": "",
    "repo": {},
    "alies": {},
    "email": {},
    "inbox": {},
    "reqeust": {}
}

accounts = {}

with open('./DB/ac.json', 'r')as ac:
    accounts = json.load(ac)


class account:
    def __init__(self, id, info) -> None:
        self.id = id
        self.info = info

    def change_secret(self, secret) -> None:
        self.info['secret'] = secret

    def new_cookie(self) -> str:
        pass
