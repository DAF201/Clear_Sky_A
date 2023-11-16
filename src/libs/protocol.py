from re import search

PROTOCOL_CLEARSKY = {'head': b'^<clearsky>.*<clearsky>$',
                     'ver': b'<clearsky_ver>.*<clearsky_ver>',
                     'sub_prot': b'<clearsky_sub><.*>.*<.*><clearsky_sub>',
                     'sub_prot_type': b'<clearsky_sub_type>.*<clearsky_sub_type>',
                     'auth': b'<clearsky_auth><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><clearsky_auth>',
                     'token': b'<clearsky_token>.*<clearsky_token>',
                     'data': b'<clearsky_data>.*<clearsky_data>',
                     'is_command': b'<clearsky_command>',
                     'is_file': b'<clearsky_file>',
                     'file_name': b'<clearsky_file_name>',
                     'has_sub_port': b'<clearsky_sub>',
                     }


class clearsky_protocol:
    def __init__(self, modules) -> None:
        self.m_protocol = PROTOCOL_CLEARSKY
        self.modules = modules

    def has_sub_protocol(self, data):
        return True if search(self.m_protocol['has_sub_port'], data) else False

    def get_sub_protocol_type(self, data) -> bytes:
        if self.has_sub_protocol(data):
            try:
                return search(self.m_protocol['sub_prot_type'], data).group(0)[19, -19]
            except:
                return b''
        return b''

    def extract_sub_protocol(self, data):
        if self.has_sub_protocol(data):
            try:
                return search(self.m_protocol['sub_prot'], data).group(0)[14, -14]
            except:
                return b''
        return b''

    def is_command(self, data):
        return True if search(self.m_protocol['is_command'], data) else False

    def extract_command(self, data):
        if self.is_command(data):
            try:
                return search(self.m_protocol['data'], data).group(0)[15, -15]
            except:
                return b''
        return b''

    def is_file(self, data):
        return True if search(self.m_protocol['is_file'], data) else False

    def get_file_name(self, data):
        if self.is_file(data):
            try:
                return search(self.m_protocol['file_name'], data).group(0)[20, -20]
            except:
                return b''
        return b''

    def extract_file(self, data):
        if self.is_file():
            try:
                return search(self.m_protocol['data'], data).group(0)[15, -15]
            except:
                return b''
        return b''

    def extract_version(self, data):
        try:
            return search(self.m_protocol['ver'], data).group(0)[14, -14]
        except:
            return b''
