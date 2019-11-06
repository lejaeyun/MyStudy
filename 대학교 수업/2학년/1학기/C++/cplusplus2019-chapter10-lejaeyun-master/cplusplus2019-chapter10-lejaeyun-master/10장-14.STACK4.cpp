// 10¿Â-14.STACK4.CPP  10.4.2 template argument
#include "10¿Â-13.STACK4.h"

template <class T, int nEl>
void Stack <T, nEl> :: Push (T elem){
    data [nElements] = elem;
	cout << "STack<T>::Push() -> elem = " << elem << endl;
    nElements ++;
}

template <class T, int nEl>
T Stack <T, nEl> :: Pop (){
    nElements --;
    return data [nElements];
}

template <class T, int nEl>
int Stack <T, nEl> :: Number (){
    return nElements;
}

template <class T, int nEl>
int Stack <T, nEl> :: Empty (){
    return (nElements == 0);
}

template <class T, int nEl>
int Stack <T, nEl> :: Full (){
    return (nElements == nEl);
}