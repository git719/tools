// iplib.c

// Some are used in https://github.com/lencap/vmc, but keeping around other
// unused ones for posterity.

#include "vmc.h"
#include <ctype.h>
#include <arpa/inet.h>

// Find next usable, unique IP in /24 subnet
char * nextUniqueIP(char *ip)
{
    // Allocate mem for our next unique IP address string
    char *nextGoodIP = NULL;
    nextGoodIP = (char *)malloc(sizeof(char)*32);
    if (nextGoodIP == NULL) {
        fprintf(stderr, "%s:%d malloc error", __FILE__, __LINE__);
        Exit(EXIT_FAILURE);
    }

    // Get /24 network substring of IP
    char *net = getIPNet(ip);

    int fourthInt = 0;       // 4th octet integer value
    char *fourth = NULL;     // 4th octet string value
    strcpy(nextGoodIP, ip);  // Start with given IP 
    while (usedIP(nextGoodIP, "")) {
        fourth = strrchr(nextGoodIP, '.');  // Get 4th octet substring
        ++fourth;
        fourthInt = atoi(fourth) + 1;       // Increment to next IP in subnet
        if (fourthInt > 254) { fourthInt = 2; }        // Boundary check
        sprintf(nextGoodIP, "%s.%u", net, fourthInt);  // Convert it to string
    }

    FreeUTF8(net);    // Release net memory
    return nextGoodIP;
}


// Check if IP octet is NOT valid
int invalidOct(char *octet) 
{
    // Two quick, obvious checks
    if (*octet == '\0') { return 1; }
    if (strlen(octet) > 3) { return 1; }

    // Walk each char to see if it's a digit
    char *tmp = octet;      // Temp pointer to walk string
    while (*tmp) {
        if (!isdigit(*tmp++)) { return 1; }  // Non-digit makes it invalid
    }
    // Note: If we walked the octed string by incrementing its pointer
    // instead of a temp one, we would end up with an empty string and
    // below atoi call wouldn't work corretly.

    // Finally, confirm the octet's value is between 0 and 255
    int num = atoi(octet);  // Convert ASCII to int
    if (num < 0 || num > 255) { return 1; }
    return 0;   // Return FALSE, since by now the octet must be VALID
}


// Check if IP address string is NOT valid
int invalidIP(char *ip)
{
    struct sockaddr_in sa;
    int result = inet_pton(AF_INET, ip, &(sa.sin_addr));
    return !(result != 0);  // Inverted to make this an INvalidity check

    // Still proud of this way :-)
    // // Check each character in the string
    // char octet[4];
    // int i = 0, dotCount = 0;
    // while (*ip) {                 // Until string ends
    //     octet[i] = *ip;           // Build up this octet
    //     if (*ip == '.') {         // If this char is a dot
    //         octet[i] = '\0';      // Terminate this octet
    //         dotCount++;
    //         if (invalidOct(octet)) { return 1; }  // If bad octet
    //         i = -1;               // Restart octet index
    //     }
    //     ++i; ++ip;     // Do next character
    // }
    // // Evaluate the last octet
    // octet[i] = '\0';   // Terminate last octet
    // if (invalidOct(octet)) { return 1; }
    // if (dotCount != 3) { return 1; }  // IP address must have only 3 dots
    // return 0;
}


// Return /24 network part (first 3 octets) of given IP string
char * getIPNet(char *ip)
{
    char *net = NULL;
    net = (char *)malloc(sizeof(char)*strlen(ip));
    if (net == NULL) {
        fprintf(stderr, "%s:%d malloc error", __FILE__, __LINE__);
        Exit(EXIT_FAILURE);
    }

    // Some special checks
    if (invalidIP(ip)) {
        net[0] = '\0';
        return net;      // Return null string
    }

    // Walk every char backwards, and break when we find first '.'
    strcpy(net, ip);
    while ( *(net + strlen(net) - 1) != '.' ) {
        *(net + strlen(net) - 1) = '\0';  // Keep shortenting the string
    }
    *(net + strlen(net) - 1) = '\0';  // Shorten last find

    return net;
}


// Check if IP is already in use. Skip given vmName
BOOL usedIP(char *ip, char *vmName)
{
    // Get a list of all VMs
    ULONG vmCount = 0;
    IMachine **vmList = NULL;
    getVMList(&vmCount, &vmList);

    // Now parse every VM object in array
    ULONG i;
    BOOL taken = FALSE;
    for (i = 0; i < vmCount; ++i) {
        IMachine *vm = vmList[i];

        // Skip if not accessible
        BOOL accessible = FALSE;
        IMachine_GetAccessible(vm, &accessible);
        if (!accessible) { continue; }

        // Skip given vmName
        char *name = getVMName(vm);
        if (strcmp(name, vmName) == 0) {
            FreeUTF8(name);        
            continue;
        }
        // Return TRUE if this IP has already been assigned to this VM
        char *tmpIP = getVMProp(vm, "/vm/ip");
        if (strcmp(tmpIP, ip) == 0) {
            FreeUTF8(tmpIP);        
            taken = TRUE;
            break;
        }
    }
    // Release objects in the array
    for (i = 0; i < vmCount; ++i) {
        IMachine *vm = vmList[i];
        if (vm) { IMachine_Release(vm); }
    }
    g_pVBoxFuncs->pfnArrayOutFree(vmList);
    
    if (taken) { return TRUE; }

    // Also check if IP is active, perhaps in use by something other than one our
    // VMs. Send 1 packet and wait 300 milliseconds for a reply. A non-zero
    // value return means the IP is NOT alive, and probably not used
    int rc;
    char cmd[256];
    sprintf(cmd, "ping -c 1 -W 300 %s >/dev/null 2>&1", ip);
    rc = system(cmd);
    if (rc == -1) {
        fprintf(stderr, "Error running: %s\n", cmd);
        Exit(EXIT_FAILURE);
    }
    if (rc == 0) { return TRUE; }

    return FALSE;
}
