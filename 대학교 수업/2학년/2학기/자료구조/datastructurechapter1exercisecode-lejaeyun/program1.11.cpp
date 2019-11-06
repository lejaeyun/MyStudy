//실습3
//program 1.11: Recursive implementation of binary search
//program 1.10 대신에 1.11를 사용하는 실습
//BinarySearch()를 호출하는 코드로서 selection sort() 함수를 테스트하는 프로그램을 사용하여 실습
#include <iostream>
#include "1.8.h"
#include <stdlib.h>
#include "1.10.h"

using namespace std;

int BinarySearch(int *a, const int x, const int left, const int right)
{
	if (left <= right)
	{
		int middle = (left + right) / 2;
		if (x < a[middle]) return BinarySearch(a, x, left, middle - 1);
		else if (x > a[middle]) return BinarySearch(a, x, middle + 1, right);
		return middle;
	}
	return -1;
}


void main()
{
	int a[5];
	int input;
	int item; //search items
	int index;
	for (int i = 0; i < 5; i++)
	{
		cout << "The next item = ";
		cin >> input;
		a[i] = input;
		cout << endl;
	}
	for (int i = 0; i < 5; i++)
		cout << "a[" << i << "] = " << a[i] << endl;

	SelectionSort(a, 5);
	for (int i = 0; i < 5; i++)
		cout << "a[" << i << "] = " << a[i] << endl;
	cin >> item;
	index = BinarySearch(a, item, 5);
	cout << "index = " << index << endl;

	system("pause");
}
