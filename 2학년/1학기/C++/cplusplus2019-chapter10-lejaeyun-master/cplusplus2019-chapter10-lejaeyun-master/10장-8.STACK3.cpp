// 10¿Â-8.STACK3.CPP   10.4 template class
#include "10¿Â-7.STACK3.h"
template <class T>
void Stack <T> :: Push (T elem){
    data [nElements] = elem;
    nElements ++;
}

template <class T>
T Stack <T> :: Pop (){
    nElements --;
    return data [nElements];
}

template <class T>
int Stack <T> :: Number (){
    return nElements;
}

template <class T>
int Stack <T> :: Empty (){
    return (nElements == 0);
}