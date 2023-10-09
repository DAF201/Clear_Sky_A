from src.libs.handler import *
PATH = [
    (r'/', root),
    (r'/create_account', create_account),
    (r'/account_modify', account_modify),
    (r'/API', API),
    (r'/static(.*)', STATIC),
    (r'/favicon', FAVICON)
]
