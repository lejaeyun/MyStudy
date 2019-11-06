//program 2.2 Implementation of operations on Rectangle
// rectangle.cpp file
#include "Rectangle.h"

Rectangle::Rectangle() {}
Rectangle::~Rectangle() {}
//program 2.4 Constructor for Rectangle

Rectangle::Rectangle(int x, int y, int h, int w)
{
	xLow = x;
	yLow = y;
	height = h;
	width = w;
}
//program 2.5: default constructor for Rectangle

Rectangle::Rectangle(int x = 0, int y = 0, int h = 0, int w = 0) : xLow(x), yLow(y), height(h), width(w)
{}
int Rectangle::GetHeight() { return height; }
int Rectangle::GetWidth() { return width; }

//program 2.6 operator == for Rectangle

bool Rectangle::operator==(const Rectangle& s)
{
	if (this == &s) return true;
	if ((xLow == s.xLow) && (yLow == s.yLow) && (height == s.height) && (width == s.width)) return true;
	else return false;
}
//program 2.7 operator << for rectangle

ostream& operator<<(ostream& os, Rectangle& r)
{
	os << "Position is: " << r.xLow << "";
	os << r.yLow << endl;
	os << "Height is: " << r.height << endl;
	os << "Width is: " << r.width << endl;
	return os;
}
