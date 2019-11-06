//program 1.5 Throwing an exception of type Char*
#include <iostream>
using namespace std;

int DivZero(int a, int b, int c)
{
	if (a <= 0 || b <= 0 || c <= 0)
		throw "All parameters should be > 0";
	return a + b * c + b / c;
}


// 1.4 basics of C++
//½Ç½À1
//program 1.6 Catching an exception of type char*
int main()
{
	try { cout << DivZero(2, 0, 4) << endl; }
	catch (const char* e)
	{
		cout << "The parameters to DivZero were 2, 0, and 4" << endl;
		cout << "An exception has been thrown" << endl;
		cout << e << endl;
		system("pause");
		return 1;
	}
	return 0;
}
