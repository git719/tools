// strsplit.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

// Split string per given delimiter and return array of strings
char** strSplit(char *String, char DELIMITER, int *Count)  // Option1
//int strsplit(char *String, char DELIMITER, int *Count, char ***StrList)  // Option2
{
    // TWO IMPLEMENTATION OPTION
    // 1. This method, that returns the list directly, when called with:
    //    char **List = strSplit(String, LiteralDelimiter, &Count);
    //    or
    // 2. Alternate method, that returns the list in StrList when called w/:
    //    char **List = NULL;
    //    strSplit(String, LiteralDelimiter, &Count, &List);
    // See corresponding 'return' comments below also.

    *Count = 1;
    char *tmp = String;
    while (*tmp) { if (*tmp == DELIMITER) { ++*Count; } ++tmp; }

    // Allocate memory for the base array of strings, type (char **)
    char **List = malloc(*Count * sizeof(char **));
    if (List == NULL) {
        fprintf(stderr, "%s:%d malloc error", __FILE__, __LINE__);
        exit(1);
    }

    // Build each individual string element in the base arry list
    char Element[32] = "";   // Assume elements will never exceed 32 chars width
    int e = 0, i = 0;
    while (*String) {           // Walk each char in string
        if (i > 32) {
            fprintf(stderr, "%s:%d index boundary error", __FILE__, __LINE__);
            exit(1);
        }
        Element[i] = *String;       // Build current element
        if (*String == DELIMITER) {
            Element[i] = '\0';	 // Terminate this element

            // Allocate memory for this element substring, type (char *)
            List[e] = malloc((i+1) * sizeof(char *));  // Note that i = strlen(Element)
            if (List[e] == NULL) {
                fprintf(stderr, "%s:%d malloc error", __FILE__, __LINE__);
                exit(1);
	        }
            strcpy(List[e], Element);  // Add element to base array
            ++e;                 // Let's do next element
            i = -1;              // Restart index for next element
	    }
	    ++String;     // Next character in string
        ++i;       // Next character in current element
    }
  
    // Build remaining element
    Element[i] = '\0';
    List[e] = malloc((i+1) * sizeof(char));
    if (List[e] == NULL) {
        fprintf(stderr, "%s:%d malloc error", __FILE__, __LINE__);
        exit(1);
    }
    strcpy(List[e], Element);  // Add element to base array

    // Option2 return:
    //   *StrList = List;
    //   return 0;     // Means function ran fine
    // Note how dereferencing with one (1) asterisk does a return-by-address!

    // Option1 return:
    return List;     // Return list directly
}

int main (void)
{
    char *Rule = "Rule 1,1,,2222,,22";
    int Count = 0;
    char **List = strSplit(Rule, ',', &Count);  // REMINDER: Free each elements and array
    printf("Rule = [%s]\n", Rule);
    printf("Split by comma (',')\n");   
    for (int i = 0; i < Count; i++) {
        printf("Element %d = [%s]\n", i, List[i]);
    } 

    for (int i = 0; i < Count; i++) { free(List[i]); }
    free(List);

    exit(1); 
}
