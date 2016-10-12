#include<iostream>


int main(int argc, char* argv[]) {
	if(argc==2)
	std::cout<<"Hello World,  You are " << argv[1]<<" !\n";
	else
	std::cout<<"No Command Line Arguements!\n";
	return 0;
}
