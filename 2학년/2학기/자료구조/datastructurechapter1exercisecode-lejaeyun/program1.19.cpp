//Program 1.19: program 1.17 with count statements added
//실행하여 실행되는 문장수를 테스트하는 프로그램 작성 
//count하는 프로그램과 time check하는 프로그램
#include <iostream>
int count = 0;

float Sum(float* a, const int n)
{
	float s = 0;
	count++;
	for (int i = 0; i < n; i++)
	{
		count++;
		s += a[i];
		count++;
	}
	count++;
	count++;
	return s;
}
