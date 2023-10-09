from src.libs.account import accounts_update_tool
from src.libs.config import TODAYS_TOKEN
from time import sleep
from datetime import datetime
from src.libs.external_tools import rand_dll


LAST_GENERATION = datetime.now()


def server_secret_generate_tool():
    if (datetime.now() - LAST_GENERATION).days > 1:
        new_token = rand_dll.todays_token()
        print('today\'s token :'+new_token)
        with open('./DB/secret', 'w')as secret:
            secret.write(str(new_token))
        global TODAYS_TOKEN
        TODAYS_TOKEN = new_token


def helper_tool():
    PARSE = 0
    while (1):
        match(PARSE):
            case 0:
                accounts_update_tool()
                PARSE += 1
            case 1:
                server_secret_generate_tool()
                PARSE += 1
            case _:
                PARSE = 0
        sleep(1)
