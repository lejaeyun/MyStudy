//program 1.25: Fibonacci numbers
#include <iostream>
using namespace std;
void Fibonacci(int rows);
int main(void) {
	int Fibo[1000];
	const int maxIndex = 1000;
	for (int i = 0; i < maxIndex; i++)
	{
		Fibo[i] = 1;
		if ( i > 2 )
			Fibo[i] = Fibonacci(Fibo, i);
	}

	cout << endl;
}

void Fibonacci(int rows)
{
	if (rows <= 1) return 1;
	else
	{
		return Fibonacci(rows - 1) + Fibonacci(rows - 2);
	}
}
//void Fibonacci(int a[], int rows)
//{ recurive algorithm으로 구현} -> 재귀함수