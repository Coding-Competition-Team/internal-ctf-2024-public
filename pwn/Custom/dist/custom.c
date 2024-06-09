#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int savedCanary;

void win(){
    system("/bin/sh");
}

int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    srand(time(NULL));
    char name[60];
    long canary = rand();

    savedCanary = canary;
    printf("Hello, what is your name?\n> ");
    gets(name);
    printf("Hello %s\n", name);
    if(canary != savedCanary){
        printf("Buffer overflow!!!");
        exit(0);
    }
}