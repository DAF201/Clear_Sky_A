#ifndef STRINGS_HPP
#define STRINGS_HPP
#include "dll.hpp"
#include <regex>
#include <string>
DLL int regex_count(char *str, char *pattern)
{
    std::string source = std::string(str);
    std::string target = std::string(pattern);
    std::regex words_regex(target);
    return std::distance(std::sregex_iterator(source.begin(), source.end(), words_regex), std::sregex_iterator());
}

DLL int regex_exist(char *str, char *pattern)
{
    std::string source = std::string(str);
    std::smatch res;
    std::regex target(pattern);
    if (std::regex_search(source, res, target))
    {
        return 1;
    }
    return 0;
}

DLL char *regex_search(char *str, char *pattern)
{
    std::string source = std::string(str);
    std::smatch res;
    std::regex target(pattern);
    if (std::regex_search(source, res, target))
    {
        return (char *)(res[0].str()).c_str();
    }
    char *e = (char *)malloc(1);
    e[0] = '\0';
    return e;
}

DLL int regex_match(char *str, char *pattern)
{
    std::string source = std::string(str);
    std::regex target(source);
    return (int)regex_match(source, target);
}

DLL char *str_replace(char *str, char *pattern, char *new_str)
{
    std::string source = std::string(str);
    std::string target = std::string(new_str);
    std::regex original(pattern);
    return (char *)std::regex_replace(source, original, target).c_str();
}

DLL char *str_slice(char *str, char *delimeter)
{
}

#endif