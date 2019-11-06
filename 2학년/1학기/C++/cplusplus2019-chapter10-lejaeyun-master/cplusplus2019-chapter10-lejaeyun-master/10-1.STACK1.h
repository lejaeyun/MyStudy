// 10-1.STACK1.H   10.2 macro로 genericity를 표현
#include<iostream>
#define TYPE int
class Stack{
    TYPE data [50];
    int nElements;
public:
    Stack () : nElements (0) { }
    void Push (TYPE elem);
    TYPE Pop ();
    int Number ();
    int Empty ();
} ;

