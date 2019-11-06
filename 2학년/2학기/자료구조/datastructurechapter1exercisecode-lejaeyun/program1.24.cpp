//program 1.24: simplified program with counting only
#include <iostream>
using namespace std;

int count = 0;
void Add(int** a, int** b, int** c, int m, int n)
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
			count += 2;
		count += 2;
	}
	count++;
}
