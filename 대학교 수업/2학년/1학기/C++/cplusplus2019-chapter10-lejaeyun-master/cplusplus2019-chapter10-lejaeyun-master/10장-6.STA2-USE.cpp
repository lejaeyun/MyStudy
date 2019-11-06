// 10장-6.STA2-USE.CPP 10.3 상속과 polymorphism을 사용하여 genericity 표현
#include <iostream>
#include "10장-4.STACK2.h"
using namespace std;

class IntObject : public GenericObject{
public:
    int data;
    IntObject (int num) :
    data (num)
    { }
};

void main (){
    Stack genericStack;
    genericStack.Push (new IntObject (500));
    genericStack.Push (new IntObject (1992));
    genericStack.Push (new IntObject (33));
    genericStack.Push (new IntObject (1024));
	cout<<"Number of stack = "<<genericStack.Number()<<endl;

    while (! genericStack.Empty ())
        cout << ((IntObject *) genericStack.Pop()) -> data << endl;

	if (genericStack.Empty()) cout<<"Stack is Empty"<<endl;
	system("pause");
}