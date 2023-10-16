
LOGIN = b'^<clearsky><head><ver>v\d\.\d\.\d<ver><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><head><clearsky>$'

LOGOUT = b'^<clearsky><tail><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><tail><clearsky>$'

# TODO:

# someone login, start a new session
SESSION_START = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>id=.*&secret=.*(&<fore>token=.*&package=.*<fore>)?<auth><com>.*<com><data>.*<data><msg>.*<msg>$'

# auth status, return a temporay token when success for further auth
SESSION_AUTH_SUCCESS = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>status=%d&code=%d&temp_token=%s<auth>$'
SESSION_AUTH_FAILED = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>status=%d&code=%s<auth>$'

# start a package, recving package, check auth and package size
RECV_PACKAGE_START = b''
# bod of the package, need to check auth and number of current package for resending if lost
RECV_PACKAGE_BODY = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>temp_token=.*<auth><package><num><num><data>.*<data><package>$'
# end of packages, check recieved packages for resending
RECV_PACKAGE_END = b''
# error occured while recving package
RECV_PCK_ERROR = b''

# response to a command request
RESP_SUCCESS = b''
RESP_FAIL = b''

# heart beat package to kick out AFKing devices after login
HEARTBEAT_PACKAGE = b'^<prot>prot=HEARTBEAT_PKG&version=\d.\d.\d<prot><auth>temp_token=.*<auth>$'

# end of session to terminate the the other side
SESSION_END = b''
