#include <stdio.h>
 
int strcmp(const char *s1, const char *s2) {
    printf("[Hook strcmp]\n");
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    return 0;
}

int strncmp(const char *s1, const char *s2, size_t n) {
    printf("[Hook strncmp]\n");
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    return 0;
}
