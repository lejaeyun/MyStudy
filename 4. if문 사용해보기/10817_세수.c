#include <stdio.h> 

int main(void)
{
	int a,b,c;

	scanf("%d %d %d",&a, &b, &c);
	int d[3] = { a,b,c };
	for (int i = 0; i < 3; i++)
	{
		for (int j = i + 1; j < 3; j++)
		{
			if (d[i] > d[j])
			{
				int tmp = d[i];
				d[i] = d[j];
				d[j] = tmp;
			}
		}
	}
	printf("%d\n", d[1]);
	return 0;
}
