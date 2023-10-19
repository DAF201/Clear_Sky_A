
LOGIN = b'^<clearsky><head><ver>v\d\.\d\.\d<ver><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><head><clearsky>$'

LOGOUT = b'^<clearsky><tail><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><tail><clearsky>$'

# TODO:

# someone login, start a new session
# protcol:type&version
# auth:id&secret
# using_foreign_token(optional):token&package(to access a package belongs to another user)
SESSION_START = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>id=.*&secret=.*(&<fore>token=.*&package=.*<fore>)?$'

# auth status, return a temporay token when success for further auth
# protcol:type&version
# auth:status_code&temp_token(when auth success)
SESSION_AUTH_SUCCESS = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>status_code=%d&temp_token=%s<auth>$'
SESSION_AUTH_FAILED = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>status_code=%s<auth>$'

# start a package, recving package, check auth and package size
RECV_PACKAGE_HEAD = b''
# bod of the package, need to check auth and number of current package for resending if lost
RECV_PACKAGE_BODY = b'^<prot>prot=.*&version=\d.\d.\d<prot><auth>temp_token=.*<auth><package><num><num><data>.*<data><package>$'
# end of packages, check recieved packages for resending
RECV_PACKAGE_TERM = b''
# error occured while recving package
RECV_PCK_ERROR = b''

# response to a command request
RESP_SUCCESS = b''
RESP_FAIL = b''

# heart beat package to kick out AFKing devices after login
HEARTBEAT_PACKAGE = b'^<prot>prot=HEARTBEAT_PKG&version=\d.\d.\d<prot><auth>temp_token=.*<auth>$'

# end of session to terminate the the other side
SESSION_END = b''
