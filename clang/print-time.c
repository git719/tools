// print-time.c

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    time_t now;  // time_t is arithmetic time type
    time(&now);  // Get current system time in time_t value
    
    // localtime converts a time_t value to calendar time and
    // returns a pointer to a tm structure with its members
    // filled with the corresponding values
    struct tm *local = localtime(&now);
    
    // Use strftime to display formatted time 
    char timeStr[32];
    strftime(timeStr, sizeof(timeStr), "%Y-%m-%d %H:%M", local);

    printf("%s\n", timeStr);

    return 0;
}
