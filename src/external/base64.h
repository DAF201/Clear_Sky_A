//
//  base64 encoding and decoding with C++.
//  Version: 2.rc.08 (release candidate)
//

#ifndef BASE64_H_C0CE2A47_D10E_42C9_A27C_C883944E704A
#define BASE64_H_C0CE2A47_D10E_42C9_A27C_C883944E704A

#include <string>
#include <cstring>
#if __cplusplus >= 201703L
#include <string_view>
#endif // __cplusplus >= 201703L

std::string base64_encode(std::string const& s, bool url = false);
std::string base64_encode_pem(std::string const& s);
std::string base64_encode_mime(std::string const& s);

std::string base64_decode(std::string const& s, bool remove_linebreaks = false);
std::string base64_encode(unsigned char const*, size_t len, bool url = false);

#if __cplusplus >= 201703L
//
// Interface with std::string_view rather than const std::string&
// Requires C++17
// Provided by Yannic Bonenberger (https://github.com/Yannic)
//
std::string base64_encode(std::string_view s, bool url = false);
std::string base64_encode_pem(std::string_view s);
std::string base64_encode_mime(std::string_view s);

std::string base64_decode(std::string_view s, bool remove_linebreaks = false);
#endif // __cplusplus >= 201703L

#include "base64_file.h"
#include <iostream>
extern "C" __declspec(dllexport) char* b64_str_encode(char* source) {
	std::string res = base64_encode(std::string(source));
	char* buffer = new char[res.size() + 1];
	strcpy_s(buffer, res.length() + 1, res.c_str());
	return buffer;
}

extern "C" __declspec(dllexport) char* b64_str_decode(char* b64_data) {
	std::string res = base64_decode(std::string(b64_data));
	char* buffer = new char[res.size() + 1];
	strcpy_s(buffer, res.length() + 1, res.c_str());
	return buffer;
}
extern "C" __declspec(dllexport) char* b64_bin_encode(unsigned char const* data, size_t len) {
	std::string res=base64_encode(data, len);
	char* buffer = new char[res.size() + 1];
	strcpy_s(buffer, res.length() + 1, res.c_str());
	return buffer;
}
extern "C" __declspec(dllexport) void b64_bin_decode(char* file_path, char* b64_data) {
	std::string path = std::string(file_path);
	std::string data = std::string(b64_data);
	Base64::decodeToFile(path, data);
}
#endif /* BASE64_H_C0CE2A47_D10E_42C9_A27C_C883944E704A */

