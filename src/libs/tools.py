from src.libs.account import accounts_update_tool
from src.libs.config import TODAYS_TOKEN, DB_PATH
from time import sleep
from datetime import datetime
from src.libs.external_tools import rand_dll

# record when was last time the server token being generated
LAST_TOKEN_GENERATION_TIME = datetime.now()


def server_secret_generate_tool():
    global LAST_TOKEN_GENERATION_TIME
    # generate a new one every 24h
    if (datetime.now() - LAST_TOKEN_GENERATION_TIME).days > 1:
        # generate a new token based on last one
        new_token = rand_dll.todays_token()
        # update
        print('today\'s token :'+str(new_token))
        with open(DB_PATH+'/secret', 'w')as secret:
            secret.write(str(new_token))
        global TODAYS_TOKEN
        TODAYS_TOKEN = new_token
        LAST_TOKEN_GENERATION_TIME = datetime.now()


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
            # add more tool functions to here if needed
            case _:
                PARSE = 0
        sleep(1)


def bytes_to_bin(data):
    return bin(int.from_bytes(data, 'little'))[2:].zfill(8)
