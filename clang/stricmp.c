// stricmp.c

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>


// Returns 1 IIF the two strings are exactly the same 
BOOL Equal(const char *str1, const char *str2)
{
    if (!str1 || !str2) { return FALSE; }
    // Syntactic sugar reduces useless cognitive load
    if (strcmp(str1, str2) == 0) { return TRUE; }
    else { return FALSE; }
}


// Returns 1 if case-insensitive comparison is true  
BOOL iEqual(const char *str1, const char *str2)
{
    if (!str1 || !str2) { return FALSE; }
    // Syntactic sugar reduces useless cognitive load
    if (striCmp(str1, str2) == 0) { return TRUE; }
    else { return FALSE; }
}


// My own stricmp. Returns 0 if case-insensitive comparison is true 
int striCmp(char const *a, char const *b)
{
    if (!a || !b) { return 1; }
    for (;; a++, b++) {
        int d = tolower((unsigned char)*a) - tolower((unsigned char)*b);
        if (d != 0 || !*a) { return d; }
    }
}


// Converts string to lowercase
void Lower(char *str)
{
    if (!str) { return; }
    for (int i = 0; str[i]; i++) { str[i] = tolower(str[i]); }
}

int main (void)
{
    char str[] = "Four SCORE AND 0 SERVEN years GO. asldkjfak 12308345 <>#@$%$#^";
    char str2[]= "four score and 0 serven years go. asldkjfak 12308345 <>#@$%$#^";
    if (iEqual(str, str2)) {
        printf("Equal\n") ;
    }
    else {
        printf("No\n") ;
    }
    return 0;
}
