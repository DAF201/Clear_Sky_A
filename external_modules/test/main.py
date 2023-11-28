import socket
from os.path import abspath, basename
from os import chdir
from re import search

chdir(abspath(__file__).replace(basename(__file__), ''))

print('test: test_module starting on 127.0.0.1:919')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 919))
s.listen(1)
while (True):
    c, a = s.accept()
    data = c.recv(1024)

    if search(b'<test>(.|\n)*<test_data>.*<test_data>(.|\n)*<test>', data):
        c.send(b'<test>data received: %b<test>' %
               (search(b'<test_data>.*<test_data>', data).group(0)))
