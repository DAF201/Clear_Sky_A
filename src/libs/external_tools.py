from ctypes import *

math_dll = cdll.LoadLibrary("./dlls/math.dll")
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


base64_dll = cdll.LoadLibrary("./dlls/base64.dll")
base64_encode_str = base64_dll.b64_bin_encode
base64_encode_str.restype = c_char_p
base64_decode_str = base64_dll.b64_str_decode
base64_decode_str.restype = c_char_p
# char* b64_str_encode(char* source)
# char* b64_str_decode(char* b64_data)
# char* b64_bin_encode(unsigned char const* data, size_t len)
# void b64_bin_decode(char* file_path, char* b64_data)


file_dll = cdll.LoadLibrary("./dlls/file.dll")
file_write = file_dll.file_write
file_write.restype = c_int
file_read = file_dll.file_read
file_read.restype = c_char_p
# int file_write(char *filename, int size, unsigned char *data)
# unsigned char *file_read(char *filename)
# char *hexify(unsigned char *data, int size)
