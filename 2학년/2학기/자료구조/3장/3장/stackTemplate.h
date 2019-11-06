#pragma once
#include <iostream>
#include <memory>


using namespace std;

struct items {
	int x, y, dir;
};

struct offsets {
	int a, b;
};

const int DefaultSize = 10000;
enum Boolean { FALSE, TRUE };

template <class T>
class Stack {

public:
	Stack(int MaxStackSize = DefaultSize);
	Boolean IsFull();
	void Add(const T& item);
	Boolean IsEmpty();
	T* Delete(T&);
	void Push(const T& x);
	T& Top() const;
	void Pop();

	void StackEmpty() { cout << "empty" << endl; };
	void StackFull() { cout << "full" << endl; };
	
	template <class T>
	friend ostream& operator<<(ostream& os, const Stack<T>& s);

	friend ostream& operator<<(ostream& os, items& item);

private:
	int top; //current element index, begin with 0
	T* stack;
	int MaxSize;//capacity of the stack
};


template <class T>
Stack<T>::Stack(int MaxStackSize) : MaxSize(MaxStackSize)
{
	stack = new T[MaxSize];
	top = -1;
}

template <class T>
inline T& Stack<T>::Top() const
{
	if (IsEmpty()) 
		throw "Stack is empty";
	if (top >= 0)
		return stack[top];
	else
		throw "Stack is empty";
}

template <class T>
void Stack<T>::Push(const T& x)
{
	if (top == capacity - 1)
	{
		ChangeSizeID(stack, capacity, 2 * capacity);
		capacity *= 2;
	}
	stack[++top] = x;
	//cout<<"top = "<<top<<"    x = "<<x<<endl;
}
template <class T>
void Stack<T>::Pop()
{
	if (IsEmpty()) throw "Stack is empty. Cannot delete.";
	stack[top--].~T();
}

template <class T>
void ChangeSizeID(T*& a, const int oldSize, const int newSize)
{
	if (newSize < 0) throw "New length must be >= 0";

	T* temp = new T[newSize];
	int number = oldSize;
	if (oldSize > newSize) number = newSize;
	//copy(a, a + number, temp);
	memcpy(temp, a, number);
	delete[] a;
	a = temp;
}
template <class T>
inline Boolean  Stack<T>::IsFull()
{
	if (top == MaxSize - 1) return TRUE;
	else return FALSE;
}

template <class T>
inline Boolean Stack<T>::IsEmpty()
{
	if (top == -1) return TRUE;
	else return FALSE;
}


template <class T>
ostream& operator<<(ostream& os, const Stack<T>& s)
{
	os << "top = " << s.top << endl;
	os << "stack elements: from the bottom to the top: " << endl;
	for (int i = 0; i <= s.top; i++)
		os << i << ":" << s.stack[i] << endl;
	return os;
}


ostream& operator<<(ostream& os, items& item)
{
	return os << item.x << "," << item.y << "," << item.dir;
}

