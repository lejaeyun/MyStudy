#pragma once


/*
class Polynomial
*/
template<class T> class Polynomial {
public:
	Polynomial() {}
	Polynomial(Chain<Term<T> >* terms) :poly(terms) {}
	Polynomial<T> operator+(const Polynomial<T>& b) const;
	void add(T coef, T exponent);
	void addAll(Polynomial<T>* poly);
	void display();
	/*
	T Evaluate(T&) const;//f(x)에 대하여 x에 대한 값을 구한다
	polynomial<T> Multiply(Polynomial<T>&); //f(x) * g(x)
	Polynomial(const Polynomial& p); //copy constructor
	friend istream& operator>>(istream&, Polynomial&);//polynomial 입력
	friend ostream& operator<<(ostream&, Polynomial&);//polynomial 출력
	const Polynomial& operator=(const Polynomial&) const;
	~Polynomial();
	Polynomial operator-(const Polynomial&)const;
	*/
private:
	Chain<Term<T> > poly;
};

template<class T>
void Polynomial<T>::add(T coef, T exponent) {
	Term<T>* newTerm = new Term<T>(coef, exponent);
	this->poly.Add(*newTerm);
}

template<class T> void Polynomial<T>::addAll(Polynomial<T>* b) {
	ChainIterator<Term<T>> iterB = b->poly.begin();

	while (iterB.NotNull()) {
		Term<T> dataB = *iterB;
		add(dataB.coef, dataB.exp);
		iterB.Next();
	}
}

template<class T> void Polynomial<T>::display() {
	poly.displayAll();
}

template<class T>
Polynomial<T> Polynomial<T>::operator+(const Polynomial<T>& b) const {
	Term<T> temp;
	ChainIterator<Term<T>> ai = poly.begin(), bi = b.poly.begin();
	Polynomial<T> c;

	while (ai && bi) {//current nodes are not null

		if (ai->exp == bi->exp) {
			int sum = ai->coef + bi->coef;
			if (sum) c.poly.InsertBack(temp.Set(sum, ai->exp));
			ai++, bi++; //advance to next term
		}
		else if (ai->exp < bi->exp) {
			c.poly.InsertBack(temp.Set(bi->coef, bi->exp));
			bi++;//next term of b
		}
	}

	while (!ai.isEmpty()) {//copy rest of a
		c.poly.InsertBack(temp.Set(ai->coef, ai->exp));
		ai++;
	}
	while (!bi.isEmpty()) {//copy rest of b
		c.poly.InsertBack(temp.Set(bi->coef, bi->exp));
		bi++;
	}
	return c;
}
