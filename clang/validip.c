
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/stat.h>

#define FALSE 0


// Check if IP address string is valid
int ValidIpStr(char *ipString)
{
    struct sockaddr_in destination;
    int rc = inet_pton(AF_INET, ipString, &(destination.sin_addr));
    if (rc < 0) {
        fprintf(stderr, "%s:%d inet_pton error", __FILE__, __LINE__);
        exit(1);
    }
    return rc;
}


int main (void)
{
    char *ip = "1.2.4.5";
    printf("IP=[%s]\n", ip);
    if (ValidIpStr(ip) == FALSE) {
        printf("Invalid\n");
    }
    else {
        printf("Valid\n");
    }
    exit(0);
}
