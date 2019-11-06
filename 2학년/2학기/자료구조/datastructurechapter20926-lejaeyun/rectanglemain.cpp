//program 2.3 C++ code fragment for Rectangle main.cpp
// rectanglemain.cpp
// 디버깅하고 완성시키는 실습-개인실습 대상
#include <iostream>
#include "Rectangle.h"

using namespace std;

void main()
{
	Rectangle r(10, 20, 5, 6), s(3, 4, 5, 6);
	Rectangle* t = &s;

	if (r.GetHeight() * r.GetWidth() > t->GetHeight() * t->GetWidth())
		cout << r;
	else
		cout << s;
	cout << " has the greater area" << endl;
	getchar();
}
