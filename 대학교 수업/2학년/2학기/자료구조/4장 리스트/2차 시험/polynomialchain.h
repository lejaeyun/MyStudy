
using namespace std;
#include <iostream>
#include<string>
#include <assert.h>

template<class T> class Term {
public:
	//All members of Term are public by default
	T coef; //coefficient
	T exp; //exponent
	Term() { coef = 0; exp = 0; }
	Term(T c, T e) :coef(c), exp(e) {}
	Term Set(int c, int e) { coef = c; exp = e; return *this; };
	void EnterTerm() { cout << endl << "coef: "; cin >> coef; cout << endl << "exp: "; cin >> exp; };
};

template<class T> class CircularDoublyChain; //forward declaration
template<class T> class CircularDoublyChainIterator;


template<class T>
class DoublyChainNode {
	friend class CircularDoublyChain<T>;
	friend class CircularDoublyChainIterator<T>;
public:
	DoublyChainNode() {}
	DoublyChainNode(const T&);
private:
	T data;
	DoublyChainNode<T>* llink, * rlink;
};

template<class T> class CircularDoublyChain {
public:
	CircularDoublyChain() { last = 0; };
	void displayav() {};
	void Delete(void); //delete the first element after first
	int Length();
	void Invert();
	void Add(const T& e);
	void Insert(T k, int n);
	void Concatenate(CircularDoublyChain<T> b);
	void InsertBack(const T& element);
	DoublyChainNode<T>* GetNode();
	void RetNode(DoublyChainNode<T>& x);
	//void Merge(CircularDoublyChain<T>& b);
	friend istream& operator>>(istream&, CircularDoublyChain&);
	friend ostream& operator<<(ostream&os, CircularDoublyChain& a)
	{
	};
	CircularDoublyChainIterator<T> begin() const { return CircularDoublyChainIterator<T>(last); }
	CircularDoublyChainIterator<T> end() const { return CircularDoublyChainIterator<T>(nullptr); }
private:	
	int n; //number of items
	static DoublyChainNode<T>* av;
	DoublyChainNode<T>* last; //point to the last node
};

template<class T> class CircularDoublyChainIterator {
private:
	const CircularDoublyChain<T>* list; //refers to an existing list
	DoublyChainNode<T>* current; //points to a node in list
public:
	//CircularDoublyChainIterator<T>(const CircularDoublyChain<T> &l) :CircularDoublyChain(l), current(l.first) {};
	CircularDoublyChainIterator() {}
	CircularDoublyChainIterator(DoublyChainNode<T>* node) :current(node) {}
	//dereferencing operators
	T& operator *() const { return current->data; }
	T* operator->()const { return &current->data; }
	bool operator && (CircularDoublyChainIterator<T> iter)const {
		return current != NULL && iter.current != NULL;
	}
	bool isEmpty() const { return current == NULL; }
	//increment
	CircularDoublyChainIterator& operator ++(); //preincrement
	CircularDoublyChainIterator<T> operator ++(int); //post increment
	bool NotNull(); //check the current element in list is non-null
	bool NextNotNull(); //check the next element in list is non-null
	T* First() { //return a pointer to the first element of list
		if (current) return &current->data;
		else return 0;
	}
	T* Next();//return a pointer to the next element of list
};
/*
class Polynomial
*/
template<class T> class Polynomial {
public:
	Polynomial();
	Polynomial(CircularDoublyChain<Term<T> >* terms) :poly(terms) {}
	void add(T coef, T exponent);
	void addAll(Polynomial<T>* poly);
	void Delete() {};
	void Displayav() { poly.displayav(); };
	T Evaluate(T&) const;//f(x)에 대하여 x에 대한 값을 구한다
	Polynomial<T> Multiply(Polynomial<T>&); //f(x) * g(x)
	Polynomial<T>(const Polynomial& p); //copy constructor
	void Add(const T& e) {};
	void Insert(T k, int n) {};


	template<class T>
	friend Polynomial<T>* operator+(const Polynomial<T>& a, const Polynomial<T>& b) {
		Term<int> temp, * p, * q;
		Polynomial<T>* c = new Polynomial<T>;

		CircularDoublyChainIterator<Term<T>> Aiter = a.poly.begin(), Biter = b.poly.begin();

		p = Aiter.First();
		q = Biter.First();

		int x = 0;
		while (Aiter.NotNull() && Biter.NotNull()) {
			switch (compare(p->exp, q->exp)) {
			case '=':
				x = p->coef + q->coef;
				temp.Set(x, q->exp);
				c->poly.InsertBack(temp);
				p = Aiter.Next();
				q = Biter.Next();
				break;
			case '<':
				temp.Set(q->coef, q->exp);
				c->poly.InsertBack(temp);
				q = Biter.Next();
				break;
			case '>':
				temp.Set(p->coef, p->exp);
				c->poly.InsertBack(temp);
				p = Aiter.Next();
			}
		}
		while (Aiter.NotNull()) {
			temp.Set(p->coef, p->exp);
			c->poly.InsertBack(temp);
			p = Aiter.Next();
		}
		while (Biter.NotNull()) {
			temp.Set(q->coef, q->exp);
			c->poly.InsertBack(temp);
			q = Biter.Next();
		}
		return c;
	}

	template<class T>
	friend Polynomial<T>* operator*(const Polynomial<T>& a, const Polynomial<T>& b) {
		Term<int> temp, * p, * q, * sq;
		Polynomial<T>* c = new Polynomial<T>;

		CircularDoublyChainIterator<Term<T>> Aiter = a.poly.begin(), Biter = b.poly.begin();

		p = Aiter.First();
		q = Biter.First();
		sq = q;

		int x = 0;
		while (Aiter.NotNull()) {
			while (Biter.NotNull()) {
				temp.Set(p->coef * q->coef, q->exp + p->exp);
				c->poly.InsertBack(temp);
				q = Biter.Next();
			}
			q = sq;
			p = Aiter.Next();
		}
		return c;
	}

	friend istream& operator>>(istream& os, Polynomial<T>& a)
	{
		Term<int> e;
		e.EnterTerm();
		a.poly.InsertBack(e);
		return os;
	}

	template<class T>
	friend ostream& operator<<(ostream& os, Polynomial<T>& a) {
		Term<T>  * p;
		CircularDoublyChainIterator<Term<T>> Aiter = a.poly.begin();
		p = Aiter.First();
		int chk = 0;
		while (Aiter.NotNull()) {
			chk = 0;
			os << *p;
			if (p->exp == -1)
				chk = 1;
			p = Aiter.Next();
			if (Aiter.NextNotNull())
				if (chk == 0)
					os << " + ";
		}
		os << endl;
		return os;
	};//polynomial 출력

	const Polynomial& operator=(const Polynomial&) const {};
	~Polynomial() {};
	Polynomial operator-(const Polynomial&)const {};

private:
	CircularDoublyChain<Term<T> > poly;
};

template <typename T>
inline ostream& operator<< (ostream& os, const Term<T>& term) {
	if (term.coef != 0 && term.exp != -1)
		os << term.coef << "x^" << term.exp;
	return os;
}

template <class T>
Polynomial<T>::Polynomial() {
	Term<T> temp(0,-1);
	poly.InsertBack(temp);
}

template <class T>
DoublyChainNode<T>::DoublyChainNode(const T& element) {
	data = element;
	rlink = NULL;
	llink = NULL;
}


template <class T>
T Polynomial<T>::Evaluate(T &n) const
{
	Term<T>* p;
	T result = 0;
	CircularDoublyChainIterator<Term<T>> Aiter = poly.begin();
	p = Aiter.First();
	while (Aiter.NotNull()) {
		T x = 1;
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
void CircularDoublyChain<T>::Insert(T k, int n)
{
	DoublyChainNode<T>* newnode = new DoublyChainNode<T>(k);
	DoublyChainNode<T>* tmp = first;
	for (int i = 0; i < n - 1; i++) {
		tmp = tmp->llink;
	}
	if (n == 0) {
		first = newnode;
		newnode->rlink = tmp;
	}
	else {
		newnode->link = tmp->link;
		tmp->link = newnode;
	}

}


template <class T>
void CircularDoublyChain<T>::Add(const T& e) //add a new node after first
{
	/*
	//처음 노드
	DoublyChainNode<T>* newnode;
	newnode = new DoublyChainNode<T>(e);
	if (!last) //insert into empty list
	{
		last = newnode;
		return;
	}
	//중간 노드 insert
	T* p;
	int x = 0;
	DoublyChainNode<T>* curr = last;
	while (curr->rlink != NULL) {
		p = &curr->data;
		curr = curr->rlink;
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
	curr->link = newnode;*/
}

char compare(int a, int b)
{
	if (a == b) return '=';
	if (a < b) return '<';
	return '>';
}

template <class T>
void CircularDoublyChain<T>::Delete(void) //delete the first element after first
{
	DoublyChainNode<T>* current, * next;
	next = first->link;
	if (first != nullptr) //non-empty list
	{
		DoublyChainNode<T>* temp = first;
		first = next;
		delete temp;
	}
	else cout << "Empty List: Not deleted" << endl;
}

template <class T>
void CircularDoublyChain<T>::Invert() {
	DoublyChainNode<T>* p = first, * q = 0; //q trails p
	while (p) {
		DoublyChainNode<T>* r = q; q = p; //r trails q
		p = p->link; //p moves to next node
		q->link = r; //link q to preceding node
	}
	first = q;
}
template <class T>
void CircularDoublyChain<T>::Concatenate(CircularDoublyChain<T> b) {
	if (!first) { first = b.first; return; }
	if (b.first) {
		for (DoublyChainNode<T>* p = first; p->link; p = p->link) {
			p->link = b.first;
		}
	}
}

template <class T>
void CircularDoublyChain<T>::InsertBack(const T& element) {
	DoublyChainNode<T>* newnode = new DoublyChainNode<T>(element);
	if (!last) //insert into empty list
	{
		last = newnode;
		return;
	}
	DoublyChainNode<T>* curr = last;
	newnode->llink = curr;
	curr->rlink = newnode;
	last = newnode;
}

template <class T>
DoublyChainNode<T>* CircularDoublyChain<T>::GetNode()
{ //provide a node for use
	DoublyChainNode<T>* x;
	if (av) { x = av, av = av->link; }
	else x = new DoublyChainNode<t>;
	return x;
}

template <class T>
void CircularDoublyChain<T>::RetNode(DoublyChainNode<T>& x)
{ //free the node pointed to by x
	x->link = av;
	av = x;
	x = 0;
}

template <class T>
DoublyChainNode<T>* CircularDoublyChain<T>::av = 0;
//DoublyChainNode<T> CircularDoublyChain<T>::av = 0;//오류 발생
template <class T>
CircularDoublyChainIterator<T>& CircularDoublyChainIterator<T>::operator ++() //preincrement
{
	current = current->llink;
	return *this;
}
template <class T>
CircularDoublyChainIterator<T> CircularDoublyChainIterator<T>::operator ++(int) //post increment
{
	CircularDoublyChainIterator<T> old = *this;
	current = current->llink;
	return old;
}
template <class T>
bool CircularDoublyChainIterator<T>::NotNull() { //check the current element in list is non-null
	if (current) return 1;
	else return 0;
}
template <class T>
bool CircularDoublyChainIterator<T>::NextNotNull() { //check the next element in list is non-null
	if (current && current->llink) return 1;
	else return 0;
}
template <class T>
T* CircularDoublyChainIterator<T>::Next() {//return a pointer to the next element of list
	if (current) {
		current = current->llink;
		return &current->data;
	}
	else return 0;
}
template<class T>
void Polynomial<T>::add(T coef, T exponent) {
	Term<T>* newTerm = new Term<T>(coef, exponent);
	this->poly.Add(*newTerm);
}

template<class T> void Polynomial<T>::addAll(Polynomial<T>* b) {
	CircularDoublyChainIterator<Term<T>> iterB = b->poly.begin();

	while (iterB.NotNull()) {
		Term<T> dataB = *iterB;
		add(dataB.coef, dataB.exp);
		iterB.Next();
	}
}