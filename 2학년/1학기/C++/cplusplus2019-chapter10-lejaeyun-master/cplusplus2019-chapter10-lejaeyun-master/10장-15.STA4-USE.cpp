// 10¿Â-15.STA4-USE.CPP  10.4.2 template argument
#include "10¿Â-14.STACK4.cpp"
#include <iostream>
using namespace std;
void main (){
    Stack <int> intStack;
    Stack <double, 4> miniStack;
	intStack.Push(10);
	miniStack.Push(1.234);
	intStack.Pop();
	miniStack.Pop();
	system("pause");
}