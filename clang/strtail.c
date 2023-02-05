// strtail.c

// Exit if malloc returns NULL
void ExitIfNull(void *ptr, const char *path, int line)
{
    if (ptr) { return; }   // Return if it's good
    if (path && line) {
        fprintf(stderr, "%s:%d malloc error\n", path, line);
    }
    PrintVBoxException();  // Print API errors if any
    Exit(EXIT_FAILURE);
}

// Allocate memory for new character string 
char * NewString(int size)
{
    if (size < 1) {
        fprintf(stderr, "%s:%d size < 1 not allowed", __FILE__, __LINE__);
        Exit(EXIT_FAILURE);
    }
    char *string = malloc(sizeof(char) * size);
    ExitIfNull(string, __FILE__, __LINE__);
    // REMINDER: Caller must free allocated memory
    return string;
}

// Return last n characters of a string
char * strTail(char *str, int n)
{
    if (!str) { return NULL; }

    int end = strlen(str);   // First, how long is the string 
    if (n > end) {    // If n is longer than the string, then chop it to be the same
        n = end;      // length as the string, effectively making this a malloc'd strcpy
    }
    if (n < 1) { return NULL; }   // Just in case

    // For why we're not casting malloc() see John Bode's 2011 great response:
    // https://stackoverflow.com/questions/7652293/how-do-i-dynamically-allocate-an-array-of-strings-in-c
    // It's not required with modern, (post 1989), C compilers; and can actually hinder debugging.
    // If you're doing C++ then it IS REQUIRED. 

    // Dynamically allocate the space for our target
    char *tail = NewString(n);

    // Walk and copy the last n characters
    int start = end - n;
    int i = 0, j = start;
    for (; j < end; i++, j++) { tail[i] = str[j]; }
    tail[i] = '\0';   // Lest we forget to terminate our substring
    return tail;
}

