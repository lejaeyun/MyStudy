//10장-15-8.Product.cpp [PRATA2005] 10.4.3 template을 이용한 Container class 표현
#include <iostream>
using namespace std;

template <typename T>
class product
{
private:
	T item;
public:
	product(const T & i) : item(i) {}
	template <typename C, typename D> friend void show(C &, D &);
};
template <typename C, typename D> void show(C & c, D & d)
{
	cout << c.item << ", " << d.item << endl;
}

int main()
{
	product<int> p1(10);
	product<int> p2(20);
	product<double> pd(10.5);
	cout << "p1, p2: ";
	show(p1, p2);
	cout << "pd, p2: ";
	show(pd, p2);
	system("pause");
	return 0;
}