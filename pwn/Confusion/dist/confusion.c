#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char adminUsername[] = "ilovepwn";
long adminPIN = 3735928559;

int main(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	char username[8];
	long long PIN = 0;

	// Oops, I accidentally switched the username and password!
	printf("Enter in your username!\n");
	scanf("%8s", &PIN);
	// correct: scanf("%8s", &username);

	printf("Enter in your PIN!\n");
	scanf("%ld", &username);
	// correct: scanf("%ld", &PIN);

	printf("You entered:\nUsername: %s\nPassword: %ld\n", username, PIN);

	if(strcmp(username, adminUsername) == 0 && PIN == adminPIN){
		printf("Wow it's the admin!\n");
		system("/bin/sh");
	}else{
		printf("Who are you???\n");
	}
}