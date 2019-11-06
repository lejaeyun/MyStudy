// 10장-9.STA3-USE.CPP  10.4 template class
#include <iostream>
#include "10장-8.STACK3.CPP" // Visual Studio에서 template 사용시에 cpp를 먼저 include하거나 header를 사용하지 않아야 함
using namespace std;

void main(){
    Stack <int> intStack;
    intStack.Push (500);
    intStack.Push (1992);
    intStack.Push (33);
    intStack.Push (1024);

    while (! intStack.Empty ()){
            cout << intStack.Pop () << endl;
	}
	system("pause");
}