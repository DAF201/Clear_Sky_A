from re import search

PROTOCOL_CLEARSKY = {'head': b'^<clearsky>.*<clearsky>$',
                     'ver': b'<clearsky_ver>.*<clearsky_ver>',
                     'sub_prot': b'<clearsky_sub><.*>.*<.*><clearsky_sub>',
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
            return sub.group(0).decode()[14, -14]
        return 'clearsky'

    def auth(self, data) -> bool:
        auth = search(PROTOCOL_CLEARSKY['auth'], data)
        if auth:
            auth_data = auth.group(0)
            id = search(b'<id>.*<id>', auth_data)
            secret = search(b'<secret>.*<secret>', auth_data)
            if not (id and secret):
                return False
            id = id.group(0).decode()[4, -4]
            secret = secret.group(0).decode()[8, -8]
        return False
