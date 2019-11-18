// Program 4.24 – Adding two polynomials, page 206
//Polynomial addition

#include "polynomialchain.h"
using namespace std;



int main(void) {
	char select;
	Term<int>* tempTerm;
	ChainNode<Term<int>> cn;
	Chain<Term<int>> f, g, k, *ck;
	Chain<Term<int>>* h = new Chain<Term<int>>;
	ChainIterator<Term<int>> iter;
	int c, e;

	cout << endl << "Select command: a: Add_f, b: Add_g, c: Add_h, p: h + f * g, d: DisplayAll, e: Eval, q: exit" << endl;
	cin >> select;
	while (select != 'q')
	{
		switch (select)
		{
		case 'a':
			cout << "Add a new polynomial: " << endl;
			cin >> f;
			break;
		case 'b':
			cout << "Add a new polynomial: " << endl;
			cin >> g;
			break;
		case 'c':
			cout << "Add a new polynomial: " << endl;
			cin >> *h;
			break;
		case 'p': //a+b
			cout << "h = f + g: " << endl;
			{
				Chain<Term<int>>* t;
				t = f * g;
				cout << "t : " << *t;
				h = *t + *h;
				cout << "h : " << *h ;
			}
			break;
		case 'd':
			cout << "display all: " << endl;
			f.displayAll();
			g.displayAll();
			h->displayAll();
			break;
		case 'e':
			cout << "evaluete: " << endl;
			int resultf = f.evaluate(coef, exp);//iterator 사용
			cout << "resultf : " << resultf;
			int resultg = g.evaluate(coef, exp);
			cout << "resultg : " << resultf;
			int resulth = h->evaluate(coef, exp);
			cout << "resulth : " << resultf;
			break;
		default:
			cout << "WRONG INPUT  " << endl;
			cout << "Re-Enter" << endl;
		}
		cout << endl << "Select command: a: Add_f, b: Add_g, c: Add_h, p: h + f * g, d: DisplayAll, e: Eval, q: exit" << endl;
		cin >> select;
	}
	system("pause");
	return 0;
}
