#include <stdio.h> 

int main(void)
{
	int T;
	
	scanf("%d", &T);
	
	if ( 90<=T && T <= 100)
		printf("A");
	else if (80<=T && T <= 99)
		printf("B");
	else if (70<=T && T <= 79)
		printf("C");
	else if (60<=T && T <= 69)
		printf("D");
	else
		printf("F");
	return 0;
}
