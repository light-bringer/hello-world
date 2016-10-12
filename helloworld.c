#include<stdio.h>

int main(int argc, char* argv[]) {
	if(argc==2)
	printf("Hello World,  You are %s !\n", argv[1]);
	else
	printf("No Command Line Arguements!\n");
	return 0;
}
