from ctypes import *

math_dll = cdll.LoadLibrary("/dlls/math.dll")

# find the closest two factors(but only return one)
factor = math_dll.factor
factor.argtypes = c_int
factor.restype = c_int

# hash a int to int
hash_int = math_dll.hash_int
hash_int.argtypes = c_int
hash_int.restype = c_int

# hash a string to int
hash_str = math_dll.hash_str
hash_str.argtypes = c_char_p
hash_str.restype = c_int

