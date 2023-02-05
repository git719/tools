#include <arpa/inet.h>
#include <ctype.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>

#define FALSE 0
#define TRUE 1

// Check if IP address string is valid
int ValidIpStr(char *ipString)
{
    struct sockaddr_in destination;
    int rc = inet_pton(AF_INET, ipString, &(destination.sin_addr));
    if (rc < 0) {
        fprintf(stderr, "%s:%d inet_pton error", __FILE__, __LINE__);
        exit(1);
    }
    return rc;  // 0 = FALSE = Invalid and 1 = TRUE = Valid
}


// Returns TRUE if IP is reachable over SSH port 22
int sshAccess(char *ip)
{
    if (ValidIpStr(ip) == FALSE) { return FALSE; }

    // Create socket
    int socket_desc;
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc < 0) {
        fprintf(stderr, "%s:%d socket create error\n", __FILE__, __LINE__);
        return FALSE;
    }

    // Use non-blocking socket, to save time
    int rc;
#ifdef _WIN32
    rc = ioctlsocket(socket_desc, FIONBIO, 0);
#else
    rc = fcntl(socket_desc, F_SETFL, O_NONBLOCK);
#endif
    if (rc < 0) {
        fprintf(stderr, "%s:%d fcntl error\n", __FILE__, __LINE__);
        return FALSE;
    }

    // Prepare address destination
    struct sockaddr_in addrdst;
    addrdst.sin_family = AF_INET;              // IPV4
    addrdst.sin_addr.s_addr = inet_addr(ip);   // IP address
    addrdst.sin_port = htons(22);              // SSH port

    // DEBUG
    time_t now;
    struct tm *ts;  // Time string 
    now = time(NULL); ts = localtime(&now);
    fprintf(stderr, "%02d:%02d:%02d Trying %s:22\n",
        ts->tm_hour, ts->tm_min, ts->tm_sec, ip);

    // Try connection
    connect(socket_desc, (struct sockaddr *)&addrdst, sizeof(addrdst));

    fd_set fdset;
    struct timeval tv;
    FD_ZERO(&fdset);
    FD_SET(socket_desc, &fdset);
    tv.tv_sec = 2;                 // 10 second timeout
    tv.tv_usec = 0;

    if (select(socket_desc + 1, NULL, &fdset, NULL, &tv) == 1) {
        int so_error;
        socklen_t len = sizeof so_error;
        getsockopt(socket_desc, SOL_SOCKET, SO_ERROR, &so_error, &len);
        if (so_error == 0) {
            close(socket_desc);

            // DEBUG
            now = time(NULL); ts = localtime(&now);
            fprintf(stderr, "%02d:%02d:%02d It is GOOD\n",
                ts->tm_hour, ts->tm_min, ts->tm_sec);
            
            return TRUE;          // It is reachable
        }
    }

    close(socket_desc);

    // DEBUG
    now = time(NULL); ts = localtime(&now);
    fprintf(stderr, "%02d:%02d:%02d It is BAD\n",
        ts->tm_hour, ts->tm_min, ts->tm_sec);

    return FALSE;         // It is NOT reachable
}


int main (void)
{
    char ip[] = "10.10.3.15";
    if (sshAccess(ip) == FALSE) {
        printf("BAD\n");
    }
    else {
        printf("GOOD\n");
    }
    return 0;
}
