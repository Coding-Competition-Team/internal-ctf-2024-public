#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char savedCanary[8];

void win(){
    system("/bin/sh");
}

int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    // Getting my canary from /dev/urandom
    FILE *f = fopen("/dev/urandom", "r");
    fgets(savedCanary, 8, f);
    fclose(f);

    char canary[8];
    char buffer[60];

    strcpy(canary, savedCanary);

    printf("Hello, what is your name?\n> ");
    gets(buffer);
    printf("Hello %s\n", buffer);

    if(strcmp(canary, savedCanary)){
        printf("Buffer overflow!!!\n");
        exit(0);
    }
}