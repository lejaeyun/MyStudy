#include <iostream>
#include <stdlib.h>
#include "1.21.h"
#define MAX 5
using namespace std;


void main()
{
	float a[MAX];
	float input, result;
	for (int i = 0; i < MAX; i++)
	{
		cout << "The next item = ";
		cin >> input;
		a[i] = input;
		cout << endl;
	}

	result = Rsum(a, MAX);
	cout << "result = " << result << endl;
	cout << "count = " << count0 << endl;

	system("pause");
}
