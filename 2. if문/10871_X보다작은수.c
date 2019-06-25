#include <stdio.h> 

int main(void)
{
	int T,a = 0,b = 0;

	scanf("%d %d",&T, &a);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &b);
		if (b < a)
		{
			printf("%d ", b);
		}
	}
	printf("\n");
	return 0;
}
