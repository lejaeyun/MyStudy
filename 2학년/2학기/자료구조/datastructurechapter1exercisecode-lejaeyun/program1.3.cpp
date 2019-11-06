// program 1.3 File I/O in C++
#include <iostream>
#include <fstream>
using namespace std;

void main()
{

	ofstream outFile("my.out", ios::out);
	if (!outFile)
	{
		cerr << "cannot open my.out" << endl;
		return;
	}

	int n = 50;
	float f = 20.3;

	outFile << "n: " << n << endl;
	outFile << "f: " << f << endl;

	cout << "succeed to write the data to the file my.out" << endl;

	system("pause");
}
