from src.libs.handler import *
# how to handle each request, maybe move create account and modify account to API too in the future
ROUTE_PATH = [
    (r'/', root),
    (r'/create_account', create_account),
    (r'/account_modify', account_modify),
    (r'/API', API),
    (r'/static(.*)', STATIC),
    (r'/favicon', FAVICON)
]
