#ifndef MATH_HPP
#define MATH_HPP
#include "dll.hpp"
#include <cmath>
#include <random>
DLL int prime(int input)
{
    if (input == 2 || input == 3)
    {
        return 1;
    }
    if (input % 6 != 1 && input % 6 != 5)
    {
        return 0;
    }
    for (int i = 5; i < ((int)pow(input, 0.5)) + 1; i++)
    {
        if (input % i == 0 || input % (i + 2) == 0)
        {
            return 0;
        }
    }
    return 1;
}
DLL int factor(int input)
{
    if (prime(input))
    {
        return input;
    }
    int upper_bound = (int)pow(input, 0.5) + 1;
    if (upper_bound < (0.5 * input))
    {
        while (input % upper_bound != 0)
        {
            upper_bound -= 1;
        }
    }
    else
    {
        while (input % upper_bound != 0)
        {
            upper_bound += 1;
        }
    }
    return upper_bound;
}

DLL int hash_int(int input)
{
    srand(input);
    return (rand() * rand()) / rand();
}

DLL int hash_str(char *input)
{
    int res = 0;
    int i = 0;
    while (input[i] != '\0')
    {
        srand(input[i]);
        if (1 % 2 == 0)
        {
            res *= rand();
        }
        else
        {
            res /= rand();
        }
        i++;
    }
    return res;
}
#endif