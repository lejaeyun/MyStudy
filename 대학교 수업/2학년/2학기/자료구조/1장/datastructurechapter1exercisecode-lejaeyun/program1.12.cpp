//실습4
//program 1.12, recursive permutation generator
// 배열 원소를 3, 4, 5개 등으로 증가시켜서 실행 실습

#include <iostream>
#include <stdlib.h>
#include "1.12.h"

using namespace std;

void main()
{
	cout << "programe1.5 12" << endl;
	char a[5];
	char input;
	for (int i = 0; i < 3; i++)
	{
		cout << "The next item = ";
		cin >> input;
		a[i] = input;
		cout << endl;
	}

	Permutations(a, 0, 3);

	system("pause");
}
