// 9Àå-3.virtdest.cpp   9.6 virtual ¼Ò¸êÀÚ
#include <iostream>
using namespace std;
class BaseClass{
public:
    BaseClass (){
        cout << "Base class constructor called" << endl;
    }
    virtual ~BaseClass (){ //virtual destructor
        cout << "Base class destructor called" << endl;
    }
};
class Derived : public BaseClass{
public:
    Derived (){
        cout << "Derived class constructor called" << endl;
    }
    ~Derived (){
        cout << "Derived class destructor called" << endl;
    }
};
void main (){
    BaseClass * pbase;
    cout << "Building a new BaseClass object..." << endl;
    pbase = new BaseClass;
    cout << "Deleting the object..." << endl;
    delete pbase;
    cout << endl << "Building a new Derived class object..."     << endl;
    pbase = new Derived;
    cout << "Deleting the object..." << endl;
    delete pbase;
	system("pause");
}