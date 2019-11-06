#pragma once

//program 1.28: program to time program 1.27
#include <iostream>
#include <time.h>
using namespace std;
int SequentialSearch(int *a, int k, int n)
{
	for (int i = 0; i < 1001; i++)
		if (a[i] == k) return i;
	return 0;
}
void TimeSearch()
{
	int a[1001], n[20];
	for (int j = 1; j <= 1000; j++)
		a[j] = j;
	for (int j = 0; j < 10; j++)
	{
		n[j] = 10 * j;
		n[j + 10] = 100 * (j + 1);
	}
	cout << "  n time" << endl;
	for (int j = 0; j < 20; j++)
	{
		long start, stop;
		start = time(NULL);
		cout << start << endl;
		int k = SequentialSearch(a, n[j], 0);
		stop = time(NULL);
		cout << stop << endl;
		long runTime = stop - start;
		cout << " " << n[j] << " " << runTime << endl;
	}
	cout << "Times are in hundredths of a second" << endl;
}

int main(void)
{
	cout << "testing of TimeSearch()";
	TimeSearch();
	getchar();
	return 0;
}

