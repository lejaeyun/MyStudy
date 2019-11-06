//FiboSeries.cpp: Fibonacci numbers
#include <iostream>
#include <chrono>  // for high_resolution_clock
using namespace std;
int Fibonacci(int[], int);
int main(void) {
	int Fibo[32000];
	const int maxIndex = 1000;
	for (int i = 1; i <= 10; i++) {
		auto start = chrono::high_resolution_clock::now();
		for (int j = 0; j <= i * maxIndex; j++) {
			Fibo[j] = 0;
		}

		Fibonacci(Fibo, maxIndex);
		for (int j = 0; j <= maxIndex; j++) {
			printf("%d %d\n", Fibo[j], j);
		}
		cout << Fibo << endl;
		auto finish = chrono::high_resolution_clock::now();
		chrono::duration<double> elapsed = finish - start;
		cout << "Row and Col size = " << i << ". Elapsed time: " << elapsed.count() << " s\n";
	}
	system("pause");
	return 1;
}

int Fibonacci(int a[], int rows)
{
	if (rows <= 1) {
		a[rows] = 1;
		return 1;
	}
	else if (a[rows] != 0) {
		return a[rows];
	}
	else
	{
		//{ recurive algorithm으로 구현}
		// a[i+2] = a[i+1] +a[i] + a[i-1]
		a[rows] = Fibonacci(a, rows - 1) + Fibonacci(a, rows - 2);
		return a[rows];
	}
}