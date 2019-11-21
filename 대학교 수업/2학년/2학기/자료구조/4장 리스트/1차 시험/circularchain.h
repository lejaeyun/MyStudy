#pragma once
/*
1. head node가 있는 circular list 구현
*/
#pragma once

#include <iostream>
using namespace std;

template<class T> class CircularChain; //forward declaration
template<class T> class CircularChainIterator;
template<class T>
class ChainNode {
	friend class CircularChain<T>;
	friend class CircularChainIterator<T>;
public:
	ChainNode() {}
	ChainNode(T);
private:
	T data;
	ChainNode<T>* link;
};

template<class T>
class CircularChain {
	friend class CircularChainIterator<T>;
public:
	CircularChain();
	~CircularChain();
	void Delete(void);
	void Attach(T&);
	int Length();
	void retlast();
	void Invert();
	void Concatenate(CircularChain<T> b);
	void Add(const T& element); //add a new node after last
	void InsertFront(const T& e);
	ChainNode<T>* GetNode();
	void RetNode(ChainNode<T>& x);
	void Merge(CircularChain<T>& b);

	template <class T>
	friend ostream& operator<<(ostream& os, CircularChain<T>& l)
	{
		return os;
	};

	template <class T>
	friend CircularChain<T> operator+(CircularChain<T> a, CircularChain<T> b) {
		CircularChain c; 
		{
			CircularChainIterator<T> li(a); //li is associated with list l
			if (li.NotNull()) {
				c.Add(*li.First());
				while (li.NextNotNull())
					c.Add(*li.Next());
			}
		}
		
		{
			CircularChainIterator<T> li(b); //li is associated with list l
			if (li.NotNull()) {
				c.Add(*li.First());
				while (li.NextNotNull())
					c.Add(*li.Next());
			}
		}
		return c;
	};
	T findMax();
private:
	static ChainNode<T>* av;
	ChainNode<T>* last; //point to the last node
};

template<class T>
class CircularChainIterator {
public:
	CircularChainIterator(const CircularChain<T>& l) :list(l), current(l.last) {};
	//dereferencing operators
	T& operator *() const 
	{ return current->data; }
	T* operator->()const 
	{ return &current->data; }
	//increment
	CircularChainIterator<T>& operator ++(); //preincrement
	CircularChainIterator<T> operator ++(int); //post increment
	bool NotNull(); //check the current element in list is non-null
	bool NextNotNull();//check the next element in list is non-null

	T* First();     //return a pointer to the first element of list
	T* Next();  //return a pointer to the next element of list

private:
	const CircularChain<T>& list;
	ChainNode<T>* current;
};
template<class T>
ChainNode<T>::ChainNode(T element = 0)
{
	data = element;
	link = 0;
}
template <class T>
CircularChain<T>::CircularChain() {
		ChainNode<T>* newnode = new ChainNode<T>(-1);
		newnode->link = newnode;
		last = newnode;
}
template <class T>
CircularChain<T>::~CircularChain() {
	if (last)
	{
		ChainNode<T>* second = last->link;
		last->link = av;
		av = second;
		last = 0;
	}
}
template <class T>
void CircularChain<T>::Attach(T& k)
{
	ChainNode<T>* newnode = new ChainNode<T>(k);
	if (last == 0) last = last = newnode;
	else {
		newnode->link = last->link;
		last->link = newnode;
		last = newnode;
	}
}

template <class T>
void CircularChain<T>::retlast()
{
	return last;
}

template <class T>
void CircularChain<T>::Delete(void) //delete the last element after last
{
	ChainNode<T>* next;
	next = last->link;
	if (!last) //non-empty list
	{
		ChainNode<T>* temp = last;
		last = next;
		delete temp;
	}
	cout << "Empty List: Not deleted" << endl;
}

template <class T>
void CircularChain<T>::Add(const T& element) //add a new node after last
{
	ChainNode<T>* newnode = new ChainNode<T>(element);
	newnode->link = 0;
	if (!last) //insert into empty list
	{
		last = newnode;
		return;
	}
	//insert a new node after last
	newnode->link = last;
	last = newnode;
}

template <class T>
void CircularChain<T>::InsertFront(const T& e)
{ //insert the element e at the 'front' of the circular list *this
  // last points to the last node in the list
	ChainNode<T>* newNode = new ChainNode<T>(e);
	if (last) { //nonempty list
		newNode->link = last->link;
		last->link = newNode;
	}
	else {//empty list
		last = newNode;
		newNode->link = newNode;
	}

}

template <class T>
ChainNode<T>* CircularChain<T>::GetNode()
{ //provide a node for use
	ChainNode<T>* x;
	if (av) { x = av, av = av->link; }
	else x = new ChainNode<t>;
	return x;
}
template <class T>
void CircularChain<T>::RetNode(ChainNode<T>& x)
{ //free the node pointed to by x
	x->link = av;
	av = x;
	x = 0;
}
template<class T>
void CircularChain<T>::Invert() {
	ChainNode<T>* p = last, * q = 0; //q trails p
	while (p) {
		ChainNode<T>* r = q; q = p; //r trails q
		p = p->link; //p moves to next node
		q->link = r; //link q to preceding node
	}
	last = q;
}

template<class T>
void  CircularChain<T>::Concatenate(CircularChain<T> b) {
	ChainNode<T>* p;
	if (!last) { last = b.last; return; }
	if (b.last) {
		// No loop body in this for loop. It just moves the pointer 'p' to the end of the A chain.
		for (p = last; p->link; p = p->link);

		p->link = b.last;
	}
}


template <class T>
ChainNode<T>* CircularChain<T>::av = 0;
//ChainNode<T> CircularChain<T>::av = 0;//오류 발생

// pre-increment
template<class T>
CircularChainIterator<T>& CircularChainIterator<T>::  operator ++()
{
	current = current->link;
	return *this;
}

//post increment
template<class T>
CircularChainIterator<T> CircularChainIterator<T>:: operator ++(int)
{
	CircularChainiterator<T> old = *this;
	current = current->link;
	return old;
}

//check the current element in list is non-null
template<class T>
bool  CircularChainIterator<T>::NotNull() {
	if (current) return 1;
	else return 0;
}

//check the next element in list is non-null
template<class T>
bool   CircularChainIterator<T>::NextNotNull() {
	if (current && current->link) return 1;
	else return 0;
}

//return a pointer to the first element of list
template<class T>
T* CircularChainIterator<T>::First() {
	if (list.last) return &list.last->data;
	else return 0;
}

//return a pointer to the next element of list
template<class T>
T* CircularChainIterator<T>::Next() {
	if (current) {
		current = current->link;
		return &current->data;
	}
	else return 0;
}