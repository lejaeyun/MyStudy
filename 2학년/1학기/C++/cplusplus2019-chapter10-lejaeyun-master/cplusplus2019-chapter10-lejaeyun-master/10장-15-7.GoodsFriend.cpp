//10장-15-7.GoodsFriend.cpp [PRATA2005] 10.4.3 template을 이용한 Container class 표현
#include <iostream>
using namespace std;

template <typename T> void showCounter();
template <typename T> void display(T &);

template <typename TT>
class Goods
{
private:
	TT item;
	static int counter;
public:
	Goods(const TT & i) : item(i) {counter++;}
	~Goods() { counter--; }
	friend void showCounter<TT>();
	friend void display<>(Goods<TT> &);
};

template <typename T>
int Goods<T>::counter = 0;

template <typename T>
void showCounter()
{
	cout <<"template showCounter():" << Goods<T>::counter << endl;
}

template <typename T>
void display(T & x)
{
	cout << x.item << endl;
}

int main()
{
	showCounter<int>();
	Goods<int> gi1(10);
	Goods<int> gi2(20);
	Goods<double> gd(10.5);
	display(gi1); 
	display(gi2); 
	display(gd);
	showCounter<int>();
	showCounter<double>();
	system("pause");
	return 0;
}