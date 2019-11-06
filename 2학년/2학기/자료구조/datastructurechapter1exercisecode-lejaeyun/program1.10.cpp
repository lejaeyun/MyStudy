//program 1.10: C++ function for binary search
//BinarySearch()를 호출하는 코드로서 selection sort() 함수를 테스트하는 프로그램을 사용하여 실습
#include <iostream>

int BinarySearch(int* a, const int x, const int n)
{
	int left = 0, right = n - 1;
	while (left <= right)
	{
		int middle = (left + right) / 2;
		if (x < a[middle]) right = middle - 1;
		else if (x > a[middle]) left = middle + 1;
		else return middle;
	}
	return -1;
}
