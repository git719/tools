// endswith.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

// Return true if both strings have same ending
bool endsWith(const char *str1, const char *str2)
{
    int l1 = strlen(str1); 
    int l2 = strlen(str2); 

    if (l2 > l1) { return false; }

    while (l2 >= 0) {
       if (str1[l1] != str2[l2]) { return false; } 
       --l1; --l2;
    }
    return true;
}

int main (void)
{
    char ip[] = "10.10.3.15";
    char end[] = ".15";
    printf("%s\n", ip);
    printf("%s\n", end);
    if (endsWith(ip, end)) {
        printf("Yes, same ending\n");
    }
    else {
        printf("Not same ending\n");
    }
    return 0;
}
