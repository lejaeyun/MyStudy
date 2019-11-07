//Program 1.18: resursive function for sum
#include <iostream>

float Rsum(float* a, const int n)
{
	if (n <= 0) return 0;
	else return (Rsum(a, n - 1) + a[n - 1]);
}
