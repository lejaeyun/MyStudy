// 10-6.STACK3.CPP  10.4.3 template을 이용한 Container class 표현
#include "10-5.Polymorphism_Stack.h"

template <class T>
void Stack <T>::Push(T elem){
    //if(T == int){}
    data[nElements] = elem;
    nElements++;
}

template <class T>
T Stack <T>::Pop(){
    nElements--;
    return data[nElements];
}

template <class T>
int Stack <T>::Number(){
    return nElements;
}

template <class T>
int Stack <T>::Empty(){
    return (nElements==0);
}
