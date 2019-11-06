//실습2
//program 1.8: Selection sort: 실습
//하나의 .cpp로 실행, 분리하여 각 function을 .h로 만들어 실행 실습
// selection sort를 quick sort로 실습하는 것이 필요
#include <iostream>
#include <stdlib.h>
#include "1.8.h"
using namespace std;


using namespace std;

void main()
{
	int a[5];
	int input;

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

	system("pause");
}
