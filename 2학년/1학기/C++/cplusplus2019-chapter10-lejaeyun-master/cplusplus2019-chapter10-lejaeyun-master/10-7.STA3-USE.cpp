#include "10-6.STACK3.CPP" ////Visual Studio는 template 사용시에 .cpp를 include하고 방법 사용-편법
// 10-7.STA3-USE.CPP   10.4.3 template을 이용한 Container class 표현
//#include "10-6.STACK3.h" //Visual Studio는 template 사용시에 header file의  include시에 오류 발생하게 함
//Visual Studio는 template 사용시에 header file을 사용하지 않아야 link 에러가 해결
#include <iostream>
#include <string>
using namespace std;

void main(){
    Stack <int> intStack;

    intStack.Push(50);
    intStack.Push(19);
    intStack.Push(3);
    intStack.Push(10);
    intStack.Push('aa');

    cout<<"-----int type stack"<<endl;
    while(! intStack.Empty()){
        cout<< intStack.Pop() << endl;
    }

    Stack <double> doubleStack;

    doubleStack.Push(500.8);
    doubleStack.Push(1992.8);
    doubleStack.Push(33.8);
    doubleStack.Push(1024.8);
	doubleStack.Push(500);

    cout<<"-----double type stack"<<endl;
    while(! doubleStack.Empty()){
        cout<< doubleStack.Pop() << endl;
    }

    Stack <string> stringStack;

    stringStack.Push("500");
    stringStack.Push("1992");
    stringStack.Push("33");
    stringStack.Push("1024");

    cout<<"-----string type stack"<<endl;
    while(! stringStack.Empty()){
        cout << stringStack.Pop() << endl;
    }
	system("pause");
}