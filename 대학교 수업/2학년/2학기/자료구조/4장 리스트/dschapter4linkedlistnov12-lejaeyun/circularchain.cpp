/*
학번: 201624548
이름: 이재윤
github id: lejaeyun@naver.com
*/

/* 
1. head node가 있는 circular chain에 대한 iterator class를 사용
2. CircularChain a, b, c, d, e, f
   d = a + b;
   e = c + d;
   e = e + f;
3. CircularChain은 임의 정수 값을 입력받아 sorted 상태로 list를 만든다
4. a + b는 merge이며 sort되며, 같은 값이 있으면 더한다
5. f = (), 즉 empty list이다
6. iterator class를 사용하여 sum()을 구한다
7. d,e는 삭제되면 노드들을 Available space lists에 반납한다.
*/
#include "circularchain.h"
template <class T>
int Show(const CircularChain<T>& l); 
template <class T>
int sum(const CircularChain<T>& l);

int main(void) {
	char select;
	ChainNode<int> nd;
	CircularChain<int> a, b,c,d,e,f;
	int value;
	do {
		cout << endl << "Select command:1: Add to list a,2: Add to list b, 3: c 입력, 4: d = a + b, 5: e = d + c, 6: e = e + f, 7: sum, 8:print available list q: quit" << endl;
		cin >> select;
		switch (select)
		{
		case '1':
			cout << "Add a new value: ";
			cin >> value;
			break;
		case '2':
			cout << "Add a new value: ";
			cin >> value;
			b.Add(value);
			break;
		case '3':
			cout << "Add a new value: ";
			cin >> value;
			c.Add(value);
			break;
		case '4':
			d = a + b;
			break;
		case '5': //print all elements by using iterator class
			e = d + c;
			break;
		case '6':
			e = e + f;
			break;
		case '7':
			cout << "Sum a: ";
			cout << sum(a) << endl;
			cout << "Sum b: ";
			cout << sum(b) << endl;
			cout << "Sum c: ";
			cout << sum(c) << endl;
			cout << "Sum d: ";
			cout << sum(d) << endl;
			cout << "Sum e: ";
			cout << sum(e) << endl;
			break;
		case '8':
			cout << "available list :";
			break;
		case 'q':
			break;
		default:
			cout << "WRONG INPUT  " << endl;
			cout << "Re-Enter" << endl;
		}
	} while (select != 'q');
	system("pause");
	return 0;
}

/* template function */
template <class T>
int Show(const CircularChain<T>& l) {
	CircularChainIterator<T> li(l); //li is associated with list l
	if (!li.NotNull()) return 0; //empty list, return 0
	T retvalue = *li.First();//get first element
	cout << retvalue;
	while (li.NextNotNull()) //make sure that next element exists
	{
		retvalue = *li.Next();
		cout << " <- " << retvalue;
	}
	return retvalue;
}
template <class T>
int sum(const CircularChain<T>& l) {
	CircularChainIterator<T> li(l);    //li is associated with list l
	if (!li.NotNull()) return 0; //empty list, return 0
	T retvalue = *li.First();    //get first element
	while (li.NextNotNull())  //make sure that next element exists
		retvalue += *li.Next();
	return retvalue;
}
