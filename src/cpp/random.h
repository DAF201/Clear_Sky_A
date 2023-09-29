#ifndef RANDOM_HPP
#define RANDOM_HPP
#include "dll.h"
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>

static char char_int_dict[] = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c',
    'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
    'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r',
    'R', 's', 'S', 't', 'T', 'u', 'U', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'};

static char full_dict[] = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c',
    'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
    'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r',
    'R', 's', 'S', 't', 'T', 'u', 'U', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z',
    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+',
    '=', '{', '}', '|', '\\', '<', ',', '>', '.', '?', '/'};
static char *__USER = "user_";

DLL char *random_str(int length)
{
    char *buffer = (char *)malloc(length);
    srand(time(NULL));
    for (int i = 0; i < length; i++)
    {
        buffer[i] = char_int_dict[rand() % sizeof(char_int_dict)];
    }
    return buffer;
}
struct image
{
    int height;
    int width;
    int channels;
    int *data;
};

DLL struct image rand_image(int height, int width, int type)
{
    struct image new_img;
    srand(time(NULL));
    switch (type)
    {
    case 0: // gray scale
        type = 1;
        new_img.channels = 1;
        break;
    case 1: // normal image
        type = 3;
        new_img.channels = 3;
        break;
    case 2: // 4 channel image that might be clear
        type = 4;
        new_img.channels = 4;
        break;
    }
    new_img.data = (int *)malloc((height * width) * sizeof(int) * type);
    for (int i = 0; i < ((height * width) * type); i++)
    {
        new_img.data[i] = rand() % 255;
    }
    new_img.height = height;
    new_img.width = width;
    return new_img;
}

DLL char *rand_username()
{
    char *username = (char *)malloc(12 * (sizeof(char)));
    memcpy(username, __USER, 5);
    srand(time(NULL));
    for (int i = 5; i < 11; i++)
    {
        username[i] = char_int_dict[rand() % sizeof(char_int_dict)];
    }
    username[11] = '\0';
    return username;
}

DLL char *rand_password()
{
}
#endif