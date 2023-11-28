from re import search
try:
    from src.libs.account import verify
except:
    from account import verify

# command and file are not yet used
PROTOCOL_CLEARSKY = {'head': b'^<clearsky>.*<clearsky>$',
                     'ver': b'<clearsky_ver>.*<clearsky_ver>',
                     'sub_prot': b'<clearsky_sub>(.|\n)*<.*>.*<.*>(.|\n)*clearsky_sub>',
                     'sub_prot_type': b'<clearsky_sub_type>.*<clearsky_sub_type>',
                     'auth': b'<clearsky_auth><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><clearsky_auth>',
                     'command': b'<clearsky_command>.*<clearsky_command>',
                     'file': b'<clearsky_file><file_name>.*<file_name><file_size>.*<file_size><clearsky_file>'
                     }


class clearsky_protocol:
    @classmethod
    def type(self, data) -> str:
        sub = search(PROTOCOL_CLEARSKY['sub_prot_type'], data)
        if sub:
            return sub.group(0).decode().replace('<clearsky_sub_type>', '')
        return 'clearsky'

    @classmethod
    def auth(self, data) -> bool:
        auth = search(PROTOCOL_CLEARSKY['auth'], data)
        if auth:
            auth_data = auth.group(0)
            id = search(b'<id>.*<id>', auth_data)
            secret = search(b'<secret>.*<secret>', auth_data)
            if not (id and secret):
                return False
            id = id.group(0).decode().replace('<id>', '')
            secret = secret.group(0).decode().replace('<secret>', '')
            return verify(id, secret)
        return False

    @classmethod
    def sub_prot(self, data):
        sub_prot_data = search(PROTOCOL_CLEARSKY['sub_prot'], data)
        if sub_prot_data:
            return sub_prot_data.group(0).replace(b'<clearsky_sub>', b'').replace(b'\n', b'').replace(b'\t', b'')
        return None
