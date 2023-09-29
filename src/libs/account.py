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
registed_accounts = {}
oneline_accounts = {}

with open('./DB/ac.json', 'r')as ac:
    registed_accounts = json.load(ac)
