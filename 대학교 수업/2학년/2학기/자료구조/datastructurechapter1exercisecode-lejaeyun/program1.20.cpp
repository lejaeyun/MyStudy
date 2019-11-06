//program 1.20: simplified version of program 1.19
#include <iostream>
int count = 0;
void Sum(float* a, const int n)
{
	for (int i = 0; i < n; i++)
		count += 2;
	count += 3;
}
