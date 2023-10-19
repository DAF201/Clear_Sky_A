# I dont really want to include 10.*.*.* and 172.16.*.*  cause I never see anyone use those
VALID_IP = b'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
LOCAL_IP = b'^192.168.(([0-9]{1})|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|[250,251,252,253,254,255]).(([0-9]{1})|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(250|251|252|253|254|255))$'
LOCAL_HOST = '0.0.0.0'
HTTP_PORT = 80

TCP_SOCKET_PORT = 920

# standard should be somewhere around 1500, but probabaly I will need to lower that a little bit for safety
TCP_PACKAGE_GLOBAL_MAX_LENGTH = 1024

# not sure if this work for all or just my device
TCP_PACKAGE_LOCAL_MAX_LENGTH = 2147483647

# 508
UDP_PACKAGE_GLOBAL_MAX_LENGTH = 500

# have not test yet
UDP_PACKAGE_LOCAL_MAX_LENGTH = 2147483647

PACKAGE_CONTAINER = {}
