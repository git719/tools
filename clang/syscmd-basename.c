// syscmd-basename.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if WIN32 
    char PATH_SEPARATOR = '\\';
#else
    char PATH_SEPARATOR = '/';
#endif

char * baseName(char *filePath)
{
    int length = strlen(filePath) - 1;
    char *basename = &filePath[length];
    while (*basename != PATH_SEPARATOR && length >= 0) {
        --basename;
        --length;
    }
    return ++basename;
}


int main (void)
{
    //char cmd[512];
    char imgFile[] = "~/.vm/ubuntu1804.ova";
    char imgFile2[] = "ubuntu1804.ova";
    //sprintf(cmd, "tar tf %s > /dev/null 2>&1", imgFile);
    //int rc = system(cmd);
    //printf("$? = %d\n", rc) ;

    printf("%c\n", PATH_SEPARATOR);

    char *base = baseName(imgFile);
    printf("[%s]\n[%s]\n\n", imgFile, base);

    char *base2 = baseName(imgFile2);
    printf("[%s]\n[%s]\n", imgFile2, base2);

    return 0;
}
