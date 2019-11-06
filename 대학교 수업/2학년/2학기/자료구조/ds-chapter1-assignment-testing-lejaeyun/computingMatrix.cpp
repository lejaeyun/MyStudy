#include <iostream>
#include "matrix.h"
#include <chrono>  // for high_resolution_clock
using namespace std;

void print(int **tab, int rows, int cols)
{
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cout << (**tab + i * cols + j) << " ";
		}
		cout << endl;
	}
}

int main(void) {
	// Multiply(int **a, int **b, int **c, int n)
	int rowSize = 0;

	for (int i = 1; i <= 100; i++) {
		// Record start time
		auto start = chrono::high_resolution_clock::now();
		rowSize = i;
		//Declare variable and get the heap space
		int ** matric1 = new int *[rowSize];
		for (int k = 0; k < rowSize; k++) {
			matric1[k] = new int[rowSize];
			for (int j = 0; j < rowSize; j++) {
				matric1[k][j] = j;
			}
		}
		//Declare variable and get the heap space
		int ** matric2 = new int *[rowSize];
		for (int k = 0; k < rowSize; k++) {
			matric2[k] = new int[rowSize];
			for (int j = 0; j < rowSize; j++) {
				matric2[k][j] = j;
			}
		}
		//Declare variable and get the heap space
		int ** matric3 = new int *[rowSize];
		for (int k = 0; k < rowSize; k++) {
			matric3[k] = new int[rowSize];
		}
		Multiply(matric1, matric2, matric3, rowSize);
		print(matric3, rowSize, rowSize);
		//release memory
		for (int i = 0; i < rowSize; i++)
			delete[] matric1[i];
		delete[]matric1;
		for (int i = 0; i < rowSize; i++)
			delete[] matric2[i];
		delete[]matric2;
		for (int i = 0; i < rowSize; i++)
			delete[] matric3[i];
		delete[]matric3;
		// Record end time
		auto finish = chrono::high_resolution_clock::now();

		chrono::duration<double> elapsed = finish - start;
		cout << "Row and Col size = "<<rowSize << ". Elapsed time: " << elapsed.count() << " s\n";
	}
	system("pause");
	return 1;
}
