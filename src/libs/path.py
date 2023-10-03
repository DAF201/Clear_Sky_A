from src.libs.handler import *
PATH = [
    (r'/', root),
    (r'/login', login),
    (r'/create_account', create_account),
    (r'/account', account),
    (r'/API', API),
    (r'/static(.*)', STATIC),
    (r'/favicon', FAVICON)
]
