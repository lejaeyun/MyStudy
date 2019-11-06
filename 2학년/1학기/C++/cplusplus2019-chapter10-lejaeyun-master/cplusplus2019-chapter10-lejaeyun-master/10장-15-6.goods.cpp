//10장-15-6.Goods.cpp [PRATA2005] 10.4.3 template을 이용한 Container class 표현
//friend function template - the bound template friends
#include <iostream>
using namespace std;
template <typename T> void showCounter();
template <typename T> void display(T &);
template <typename T>
class Goods
{
private:
	T item;
	static int counter;
public:
	Goods(const T & i) : item(i) {counter++;}
	~Goods() {counter--; }
	friend void showCounter<T>();
	friend void display<>(Goods<T> &); 
};

template <typename T>
int Goods<T>::counter = 0;
//template friend function definition
template <typename T>
void showCounter()
{
	cout << "int counter: " << Goods<T>::counter << "; ";
	//cout << "double counter: " << Goods<double>::counter << endl;
}
template <typename T>
void display(Goods<T> & g)
{
	cout <<"Goods<int>: " << g.item << endl;
}
/*
template <typename T>
void display(Goods<T> & g)
{
	cout <<"Goods<double>: " << g.item << endl;
}
*/
int main()
{
	showCounter<int>();
	Goods<int> gi1(10);
	showCounter<int>();
	Goods<int> gi2(20);
	showCounter<int>();
	Goods<double> gd(10.5);
	showCounter<double>();
	display(gi1);
	display(gd);
	system("pause");
	return 0;
}