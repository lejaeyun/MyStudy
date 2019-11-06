// 10-3.STA1-USE.CPP   10.2 macro로 genericity를 표현
#include <iostream>
#include "10-1.STACK1.h" //macro 사용
using namespace std;

void main (){
    Stack intStack;
    intStack.Push (500);
    intStack.Push (1992);
    intStack.Push (33);
    intStack.Push (1024);
	cout<<"Number of stack = "<<intStack.Number()<<endl;
    while (! intStack.Empty ())
        cout << intStack.Pop () << endl;
	if (intStack.Empty()) cout<<"Stack is Empty"<<endl;
	system("pause");
} 