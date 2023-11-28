#ifndef FILE_HPP
#define FILE_HPP
#include "dll.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

DLL int file_write(char *filename, int size, unsigned char *data)
{
    FILE *file = fopen((const char *)filename, "wb");
    unsigned char *buffer = (unsigned char *)malloc(size);
    memcpy(buffer, data, size);
    int res = fwrite(buffer, size, 1, file);
    fclose(file);
    return res;
}

DLL unsigned char *file_read(char *filename)
{
    FILE *file = fopen((const char *)filename, "rb");
    fseek(file, 0, SEEK_END);
    int size = ftell(file);
    fseek(file, 0, SEEK_SET);
    unsigned char *buffer = (unsigned char *)malloc(size);
    int res = fread(buffer, size, 1, file);
    fclose(file);
    return buffer;
}

DLL int file_size(char *filename)
{
    FILE *file = fopen((const char *)filename, "rb");
    fseek(file, 0, SEEK_END);
    int size = ftell(file);
    fclose(file);
    return size;
}

// dont use
DLL long long file_time(char *filename, int type)
{
    struct stat file_info;

    switch (type)
    {
    case 0:
    {
        return file_info.st_ctime;
    }
    case 1:
    {
        return file_info.st_mtime;
    }
    case 2:
    {
        return file_info.st_atime;
    }
    default:
    {
        return -1;
    }
    }
}

DLL char *hexify(unsigned char *data, int size)
{
    char *buffer = (char *)malloc(2 * size);
    for (int i = 0; i < size; i++)
    {
        sprintf(&buffer[i * 2], "%02X", data[i]);
    }
    return buffer;
}

#endif
