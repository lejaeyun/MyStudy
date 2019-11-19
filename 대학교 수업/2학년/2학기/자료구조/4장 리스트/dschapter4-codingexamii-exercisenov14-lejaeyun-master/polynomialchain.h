#pragma once
#pragma once
/*
2nd Edition å - 2007
*/
using namespace std;
#include <iostream>
#include<string>
#include <assert.h>

template<class T> 
class Term {
public:
	//All members of Term are public by default
	T coef; //coefficient
	T exp; //exponent
	Term() { coef = 0; exp = 0; }
	Term(T c, T e) :coef(c), exp(e) {}
	Term Set(int c, int e) { coef = c; exp = e; return *this; };
	void EnterTerm() { cout << endl << "coef: "; cin >> coef; cout << endl << "exp: "; cin >> exp; };
};

template<class T> class Chain; //forward declaration
template<class T> class Term;
template<class T> class ChainIterator;


template<class T>
class ChainNode {
	friend class Chain<T>;
	friend class ChainIterator<T>;
public:
	ChainNode() {}
	ChainNode(const T&);
private:
	T data;
	ChainNode<T>* link;
};

template<class T> 
class Chain {
public:
	Chain() { first = 0; };
	void displayAll();
	void Delete(void); //delete the first element after first
	int Length();
	void Insert(T, int);
	double evaluate(int);
	void Add(const T& element); //add a new node after first
	void Invert();
	void Concatenate(Chain<T> b);
	void InsertBack(const T& element);
	friend istream& operator>>(istream& os, Chain<T>& p) 
	{
		Term<int> e;
		e.EnterTerm();
		p.Add(e);
		return os;
	}

	friend ostream& operator<<(ostream& os, Chain<T>& p){
		p.displayAll();
		return os;
	};

	template<class T>
	friend Chain<T>* operator+(const Chain<T>& a, const Chain<T>& b) {
		Term<int> temp, * p, * q;
		Chain<T>* c = new Chain<T>;

		ChainIterator<T> Aiter(a.first);
		ChainIterator<T> Biter(b.first);

		p = Aiter.First();
		q = Biter.First();

		int x = 0;
		while (Aiter.NotNull()) {
			temp.Set(p->coef, p->exp);
			c->Add(temp);
			p = Aiter.Next();
		}
		while (Biter.NotNull()) {
			temp.Set(q->coef, q->exp);
			c->Add(temp);
			q = Biter.Next();
		}
		return c;
	}

	template<class T>
	friend Chain<T>* operator*(const Chain<T>& a, const Chain<T>& b) {
		Term<int> temp, * p, * q, *sq;
		Chain<T>* c = new Chain<T>;

		ChainIterator<T> Aiter(a.first);
		ChainIterator<T> Biter(b.first);

		p = Aiter.First();
		q = Biter.First();
		sq = q;

		int x = 0;
		while (Aiter.NotNull()) {
			while (Biter.NotNull()) {
				temp.Set(p->coef * q->coef, q->exp + p->exp);
				c->Add(temp);
				q = Biter.Next();
			}
			q = sq;
			p = Aiter.Next();
		}
		return c;
	}

	ChainIterator<T> begin() const { return ChainIterator<T>(first); }
	ChainIterator<T> end() const { return ChainIterator<T>(nullptr); }
private:
	ChainNode<T>* first;
};

template<class T> class ChainIterator {
private:
	//const Chain<T>* list; //refers to an existing list
	ChainNode<T>* current; //points to a node in list
public:
	//ChainIterator<T>(const Chain<T> &l) :Chain(l), current(l.first) {};
	ChainIterator() {}
	ChainIterator(ChainNode<T>* node) :current(node) {}
	//dereferencing operators
	T& operator *() const { return current->data; }
	T* operator->()const { return &current->data; }
	bool operator && (ChainIterator<T> iter)const {
		return current != NULL && iter.current != NULL;
	}
	bool isEmpty() const { return current == NULL; }
	//increment
	ChainIterator& operator ++(); //preincrement
	ChainIterator<T> operator ++(int); //post increment
	bool NotNull(); //check the current element in list is non-null
	bool NextNotNull(); //check the next element in list is non-null

	T* First() { //return a pointer to the first element of list
		if (current) return &current->data;
		else return 0;
	}
	T* Next();//return a pointer to the next element of list
};


template <typename valType>
inline ostream& operator<< (ostream& os, const Term<valType>& term) {
	if (term.coef != 1 && term.coef != 0)
		os << term.coef;
	os  << "x^" << term.exp;
	return os;
}
template <class T>
ChainNode<T>::ChainNode(const T& element) {
	data = element;
	link = 0;
}


template <class T>
double Chain<T>::evaluate(int n)
{
	double result = 0;
	T* p;
	ChainIterator<T> Aiter(first);
	p = Aiter.First();
	while (Aiter.NotNull()) {
		double x = 1;
		for (int i = 0; i < p->exp; i++)
		{
			x = x * n;
		}
		result = result + p->coef * x;
		p = Aiter.Next();
	}
	return result;
}

template <class T>
void Chain<T>::Insert(T k, int n)
{
	ChainNode<T>* newnode = new ChainNode<T>(k);
	ChainNode<T>* tmp = first;
	for (int i = 0; i < n-1; i++) {
		tmp = tmp->link;
	}
	if (n == 0) {
		first = newnode;
		newnode->link = tmp;
	}
	else {
		newnode->link = tmp->link;
		tmp->link = newnode;
	}
		
}

template <class T>
void Chain<T>::Delete(void) //delete the first element after first
{
	ChainNode<T>* current, * next;
	next = first->link;
	if (first != nullptr) //non-empty list
	{
		ChainNode<T>* temp = first;
		first = next;
		delete temp;
	}
	else cout << "Empty List: Not deleted" << endl;
}
template <class T>
void Chain<T>::Add(const T& e) //add a new node after first
{
	/*
	Term<int>* p, * q, temp;
	ChainIterator<Term<int>> Aiter(first);
	p = Aiter.First();

	int x = 0;
	while (Aiter.NotNull()) {
		switch (compare(p->exp, e.exp)) {
		case '=':
			p->coef = p->coef + e.coef;
			return;
		case '<':
			Insert(e, x);
			return;
		case '>':
			p = Aiter.Next();
		}
		x = x + 1;
	}
	poly.Attach(e);
	*/

	//처음 노드
	ChainNode<T>* newnode;
	newnode = new ChainNode<T>(e);
	if (!first) //insert into empty list
	{
		first = newnode;
		return;
	}
	//중간 노드 insert
	T* p;
	int x = 0;
	ChainNode<T>* curr = first;
	while (curr->link != NULL) {
		p = &curr->data;
		curr = curr->link;
		switch (compare(p->exp, e.exp)) {
			case '=':
				p->coef = p->coef + e.coef;
				return;
			case '<':
				cout << curr->data.exp;
				Insert(e, x);
				return;
		}
		x = x + 1;
	}
	//노드가 1개 있을때
	p = &curr->data;
	switch (compare(p->exp, e.exp)) {
		cout << curr->data.exp;
	case '=':
		p->coef = p->coef + e.coef;
		return;
	case '<':
		cout << curr->data.exp;
		Insert(e, x);
		return;
	}

	//마지막 노드에 추가
	p = &curr->data;
	if (first->link == NULL) {
		switch (compare(p->exp, e.exp)) {
			case '=':
				p->coef = p->coef + e.coef;
				return;
			case '<':
				newnode->link = first;
				first = newnode;
				return;
		}
	}
	curr->link = newnode;

}

template <class T>
void Chain<T>::Invert() {
	ChainNode<T>* p = first, * q = 0; //q trails p
	while (p) {
		ChainNode<T>* r = q; q = p; //r trails q
		p = p->link; //p moves to next node
		q->link = r; //link q to preceding node
	}
	first = q;
}

template <class T>
void Chain<T>::Concatenate(Chain<T> b) {
	if (!first) { first = b.first; return; }
	if (b.first) {
		for (ChainNode<T>* p = first; p->link; p = p->link) {
			p->link = b.first;
		}
	}
}
template <class T>
void Chain<T>::InsertBack(const T& element) {

	ChainNode<T>* newnode = new ChainNode<T>(element);
	if (!first) //insert into empty list
	{
		first = newnode;
		return;
	}

	ChainNode<T>* curr = first;
	while (curr->link != NULL) {
		curr = curr->link;
	}
	curr->link = newnode;
}

template <class T>
void Chain<T>::displayAll() {
	if (!first) return;
	ChainNode<T>* curr = first;
	int chk = 0;
	while (curr != NULL) {
		if (chk) cout << " + ";
		cout << curr->data;
		curr = curr->link;
		chk++;
	}
	cout << endl;
}
template <class T>
ChainIterator<T>& ChainIterator<T>::operator ++() //preincrement
{
	current = current->link;
	return *this;
}
template <class T>
ChainIterator<T> ChainIterator<T>::operator ++(int) //post increment
{
	ChainIterator<T> old = *this;
	current = current->link;
	return old;
}
template <class T>
bool ChainIterator<T>::NotNull() { //check the current element in list is non-null
	if (current) return 1;
	else return 0;
}
template <class T>
bool ChainIterator<T>::NextNotNull() { //check the next element in list is non-null
	if (current && current->link) return 1;
	else return 0;
}
template <class T>
T* ChainIterator<T>::Next() {//return a pointer to the next element of list
	if (current) {
		current = current->link;
		return &current->data;
	}
	else return 0;
}

char compare(int a, int b)
{
	if (a == b) return '=';
	if (a < b) return '<';
	return '>';
}