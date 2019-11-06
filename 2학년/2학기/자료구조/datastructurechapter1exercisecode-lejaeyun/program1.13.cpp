//Program 1.13: Compute the product of the elements a[0:n-1]
//STL을 호출하는 main()을 개인별로 homework로 실행
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int Product(int* a, int n)
{
	int initVal = 1;
	return accumulate(a, a + n, initVal, multiplies<int>());
}

int main()
{
	return 0;
}
