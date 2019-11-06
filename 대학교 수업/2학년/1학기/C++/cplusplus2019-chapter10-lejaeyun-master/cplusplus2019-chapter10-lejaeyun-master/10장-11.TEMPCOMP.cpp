// 10장-11.TEMPCOMP.CPP   10.4.1 타입 호환성 문제
#include <iostream>
using namespace std;
template <class T> class Single{
    T data;

public:
    Single ()
    { }

    void Set (T el){
        data = el;
    }
    T Get (){
        return data;
    }
} ;

void main(){
    Single <int> oneInt;
    oneInt.Set (5);
    Single <float> oneFloat;
    oneFloat.Set (4.9);
    Single <int> secondInt;
    secondInt.Set (8);

    oneInt = secondInt;
    //oneInt = oneFloat; //다른 type
	system("pause");
}