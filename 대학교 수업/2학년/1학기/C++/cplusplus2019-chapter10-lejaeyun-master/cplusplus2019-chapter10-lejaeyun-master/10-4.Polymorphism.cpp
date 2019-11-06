// 10-4.Polymorphism.cpp  10.3 상속과 polymorphism을 사용하여 genericity 표현
#include <iostream>
using namespace std;

class GenericObject
{};
class Stack{
    GenericObject* data[50];
    int nElements;
public:
    Stack():
    nElements(0)
    {}
    void Push(GenericObject* item);
    GenericObject* Pop();
    int Number();
    int Empty();
};

void Stack::Push(GenericObject* item){
    data[nElements] = item;
    nElements++;
}
GenericObject* Stack::Pop(){
    nElements--;
    return data[nElements];
}
int Stack::Number(){
    return nElements;
}
int Stack::Empty(){
    return (nElements==0);
}

class IntObject : public GenericObject{
public:
    int data;
    IntObject(int num):
    data(num)
    {}
};

class doubleObject : public GenericObject{
public:
    double data;
    doubleObject(double num):
    data(num)
    {}
};

class floatObject : public GenericObject{
public:
    float data;
    floatObject(float num):
    data(num)
    {}
};

void main(){
    //* 주석 1
    Stack genericStack_1;

    genericStack_1.Push(new IntObject(500));
    genericStack_1.Push(new IntObject(1992));
    genericStack_1.Push(new IntObject(33));
    genericStack_1.Push(new IntObject(1024));

    cout<<"-----int type stack"<<endl;
    while(! genericStack_1.Empty()){
        cout<< ((IntObject*)genericStack_1.Pop())->data << endl;
    }
    //*/

    //* 주석 2
    Stack genericStack_2;
    genericStack_2.Push(new doubleObject(500.812));
    genericStack_2.Push(new doubleObject(1992.835));
    genericStack_2.Push(new doubleObject(33.877));
    genericStack_2.Push(new doubleObject(1024.809));

    cout<<endl<<"-----double type stack"<<endl;
    while(! genericStack_2.Empty()){
        cout << ((doubleObject*)genericStack_2.Pop())->data << endl;
    }
   // */

    //* 주석 3
    Stack genericStack_3;
    genericStack_3.Push(new floatObject(500.887));
    genericStack_3.Push(new floatObject(1992.811));
    genericStack_3.Push(new floatObject(33.899));
	genericStack_3.Push(new IntObject(1024)); //type check가 수행되지 않음
    genericStack_3.Push(new floatObject(1024.851));

    cout<<endl<<"-----float type stack"<<endl;
    while(! genericStack_3.Empty()){
        cout << ((floatObject*)genericStack_3.Pop())->data << endl;
    }
    //*/

    /* 주석 4
    cout<<endl<<"-----float type stack"<<endl;
    while(! genericStack_3.Empty()){
       cout << genericStack_3.Pop()->data << endl; //cout<<GenericObject;이 정의되지 않았음
    }
    */
    system("pause");
}