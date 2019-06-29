//https://www.acmicpc.net/problem/1003
#include <stdio.h> 

int main(void)
{
	int T, N,b=1,c;
	int a[50]= {0,1};
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		
		scanf("%d", &N);
		for (int j = 2; j <= N; j++)
		{
			a[j] = a[j-1]+a[j-2];
		}
		if (N == 0)
		{
			b = 1;
			c = 0;
		}
		else
		{
			b = a[N-1];
			c = a[N];
		}
			
		
		printf("%d %d\n", b, c);
	}
	return 0;
}