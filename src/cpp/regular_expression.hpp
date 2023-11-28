#ifndef STRINGS_HPP
#define STRINGS_HPP
#include "dll.hpp"
#include <regex>
#include <string>
#include <vector>

// count how many times a pattern appeared
DLL int regex_count(char *str, char *pattern)
{
    std::string source = std::string(str);
    std::string target = std::string(pattern);
    std::regex words_regex(target);
    return std::distance(std::sregex_iterator(source.begin(), source.end(), words_regex), std::sregex_iterator());
}

// check if a pattern exist
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

// search for a pattern, return first appearance
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

// return if the whole string match
DLL int regex_match(char *str, char *pattern)
{
    std::string source = std::string(str);
    std::regex target(source);
    return (int)regex_match(source, target);
}

// raeplace the pattern with something
DLL char *str_replace(char *str, char *pattern, char *new_str)
{
    std::string source = std::string(str);
    std::string target = std::string(new_str);
    std::regex original(pattern);
    return (char *)std::regex_replace(source, original, target).c_str();
}

#endif