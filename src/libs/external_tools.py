from ctypes import *

math_dll = cdll.LoadLibrary(r'./dlls/math.dll')
is_prime = math_dll.prime
is_prime.restype = c_int
factor = math_dll.factor
factor.restype = c_int
hash_int = math_dll.hash_int
hash_int.restype = c_int
hash_str = math_dll.hash_str
hash_str.restype = c_int
# int prime(int input)
# int factor(int input)
# int hash_int(int input)
# int hash_str(char *input)


file_dll = cdll.LoadLibrary(r'./dlls/file.dll')
file_write = file_dll.file_write
file_write.restype = c_int
file_read = file_dll.file_read
file_read.restype = c_char_p
# int file_write(char *filename, int size, unsigned char *data)
# unsigned char *file_read(char *filename)
# char *hexify(unsigned char *data, int size)

rand_dll = cdll.LoadLibrary(r'./dlls/rand.dll')
rand_dll.rand_username.restype = c_char_p
rand_dll.random_str.restype = c_char_p
rand_dll.todays_token.restype = c_int
rand_dll.hash_str.restype = c_int
# DLL char *rand_username()
# DLL int todays_token()
# DLL int hash_str(char *input, int len)
# DLL int random_str()
