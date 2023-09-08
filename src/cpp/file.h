#ifndef FILE_HPP
#define FILE_HPP
#include "dll.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
DLL int file_write(char *filename, int size, unsigned char *data)
{
    FILE *fout = fopen("test1.mp4", "wb");
    unsigned char *buffer = (unsigned char *)malloc(size);
    memcpy(buffer, data, size);
    int res = fwrite(buffer, size, 1, fout);
    fclose(fout);
    return res;
}
DLL unsigned char *file_read(char *filename)
{
}
#endif
