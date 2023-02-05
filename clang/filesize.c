// filesize.c

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#include <time.h>
#include <sys/stat.h>
#include <sys/types.h>

// Returns file size or -1 if file not found
long int fileSize(char filePath[]) 
{ 
    FILE* fp = fopen(filePath, "r"); 
    if (fp == NULL) { return -1; } 
  
    fseek(fp, 0L, SEEK_END); 
    long int res = ftell(fp); 
    fclose(fp); 
    return res; 
}


void getFileCreationTime(char *path) {
    struct stat attr;
    stat(path, &attr);
    printf("Last modified time: %s", ctime(&attr.st_mtime));
}


int main (void)
{
    char filePath[] = "/Users/lcapella/.vm/centos7-1908.ova";
    long int size = fileSize(filePath);
    if (size != -1) { 
        printf("size = %luB\n", size) ;
        printf("size = %luKB\n", size/1024) ;
        printf("size = %luMB\n", size/(1024*1024)) ;
        printf("size = %luGB\n", size/(1024*1024*1024)) ;
    }
    getFileCreationTime(filePath);
    
    return 0;
}
