//12.Doubly Linked List Implementation with Pointers C++
//circular doubly lists with head node 구현- 이코드를 수정하여 사용, 두개의 list를 만들고 list node에 정수 값이 sorted된 상태로 입력되게 하고, 두개의 list를 merge하여 합친 결과도 sorted list되게 한다. 
#include <iostream>
using namespace std;
template<class T> class CircularDoublyList;
template<class T> class CircularDoublyListIterator;
template<class T>
class DoublyListNode {
	friend class CircularDoublyList<T>;
private:
	T data;
	DoublyListNode<T>* llink, * rlink;
};
template<class T>
class CircularDoublyList {
	friend class CircularDoublyListIterator<T>;
public:
	CircularDoublyList() { first = new DoublyListNode<T>; first->rlink = last; last->llink = first; first->data = -1; }
	CircularDoublyList(const CircularDoublyList<T>&);
	~CircularDoublyList();
	int Size()const;
	bool Empty()const;
	void Attach(T);
	void Delete(DoublyListNode<T>*);
	void Insert(DoublyListNode<T>*, DoublyListNode<T>*);
	void Insert(T);
	void Merge(CircularDoublyList<T>&); // 머지 -> operator +
	bool Delete(T);
	template<class T>
	friend ostream& operator<<(ostream&, CircularDoublyList<T>&);
	//void Concatenate(CircularDoublyList<T>) // 한번 해보기
private:
	int n; //number of items
	DoublyListNode<T>* first;
	DoublyListNode<T>* last;
	static DoublyListNode<T>* av;
};
template<class T>
class CircularDoublyListIterator {
public:
	CircularDoublyListIterator(const CircularDoublyList<T>& l) : list(l) { current = l.first->link; }
	T* Next();
	T* First();
	bool NotNull();
	bool NextNotNull();
private:
	const CircularDoublyList<T>& list;
	DoublyListNode<T>* current;
};

template<class T>
DoublyListNode<T>* CircularDoublyList<T>::av = 0;
template<class T>
void CircularDoublyList<T>::Insert(T x) {
	DoublyListNode<T>* p, * temp = new DoublyListNode<T>;
	temp->data = x;
	p = first;

	while (true) {
		if (x < p->rlink->data)
		{
			temp->llink = p; temp->rlink = p->rlink;
			p->rlink->llink = temp; p->rlink = temp;
			break;
		}
		else if (p->rlink->data != -1)
			p = p->rlink;
		else {
			temp->llink = p; temp->rlink = p->rlink;
			p->rlink->llink = temp; p->rlink = temp;
			break;
		}
	}
	// Increase the number of nodes
	n++;
}
template<class T>
void CircularDoublyList<T>::Merge(CircularDoublyList<T>& b)
{
	auto current = b.first->rlink;
	while (current != b.first)
	{
		this->Insert(current->data);
		current = current->rlink;

		if (current->llink != b.first)
			b.Delete(current->llink);
	}
}
template<class T>
bool CircularDoublyList<T>::Delete(T _data)
{
	for (auto current = first; first != last; first++)
	{
		if (current->data == _data)
		{
			Delete(current);
			return true;
		}
	}
	return false;
}
template<class T>
void CircularDoublyList<T>::Delete(DoublyListNode<T>* x)
{
	if (x == first) cerr << "Deletion of head node not permitted" << endl;
	else {
		x->llink->rlink = x->rlink;
		x->rlink->llink = x->llink;
		delete x;
	}
}
template<class T>
void CircularDoublyList<T>::Insert(DoublyListNode<T>* p, DoublyListNode<T>* x)
//insert node p to the right of node x
{
	p->llink = x;
	p->rlink = x->rlink;
	x->rlink->llink = p;
	x->rlink = p;
}
template<class T>
void CircularDoublyList<T>::Insert(T x) {
	DoublyListNode<T> *p, *temp = new DoublyListNode<T>;
	temp->data = x;
	p = first;
	while (p->data != -1) {
		if (x < p->rlink->data)
		{
			temp->llink = p; temp->rlink = p->rlink;
			p->rlink->llink = temp; p->rlink = temp;
			n++;
			break;
		}
		else if (p->rlink->data != -1)
			p = p->rlink;
		else {
			temp->llink = p; temp->rlink = p->rlink;
			p->rlink->llink = temp; p->rlink = temp;
			n++;
		}
	}
}
template<class T>
int CircularDoublyList<T>::Size() const {
	return((first->data == -1) ? 0 : n);
}
template<class T>
bool CircularDoublyList<T>::Empty() const {
	return((first->data == -1) ? 1 : 0);
}

template<class T>
T* CircularDoublyListIterator<T>::First() {
	if (current != list.first) return &current->data;
	else return 0;
}

template<class T>
T* CircularDoublyListIterator<T>::Next() {
	current = current->link;
	if (current != list.first) return &current->data;
	else return 0;
}

template<class T>
bool CircularDoublyListIterator<T>::NotNull()
{
	if (current != list.first) return TRUE;
	else return FALSE;
}

template<class T>
bool CircularDoublyListIterator<T>::NextNotNull()
{
	if (current->link != list.first) return TRUE;
	else return FALSE;
}


template<class T>
CircularDoublyList<T>::CircularDoublyList(const CircularDoublyList<T>& l)
{
	if (l.first == 0) { first = 0; return; }
	first = new DoublyListNode<T>(l.first->data);
	DoubltListNode<T>* newnode = first;
	for (DoublyListNode<T>* current = l.first->link; current != l.first; current = current->link)
	{
		newnode->link = new DoublyListNode<T>(current->data);
		newnode = newnode->link;
	}
	newnode->link = first;
}


template<class T>
CircularDoublyList<T> ::~CircularDoublyList()
{
	if (first)
	{
		DoublyListNode<T>* second = first->link;
		first->link = av;
		av = second;
		first = 0;
	}
}

template<class T>
ostream& operator<<(ostream& os, CircularDoublyList<T>& l)
{
	CircularDoublyListIterator<T> li(l);
	if (!li.NotNull()) return os;
	os << *li.First();
	while (li.NextNotNull())
		os << " + " << *li.Next();
	os << endl;
	return os;
}


template<class T>
void CircularDoublyList<T>::Attach(T k)
{
	DoublyListNode<T>* newnode = new DoublyListNode<T>(k);
	if (first == 0) first = last = newnode;
	else {
		newnode->link = last->link;
		last->link = newnode;
		last = newnode;
	}
}

int main()
{
	char select;

	//*Term<int> *tempTerm;
	DoublyListNode<float> nd;
	CircularDoublyList<float> a, b;
	CircularDoublyListIterator<float> iter(a);
	int c, e;
	float weight;
	cout << endl << "Select command: a: Add to List a, b: Add to List b, d: Delete, m: Merge, p: PrintAll, q: exit" << endl;
	cin >> select;
	while (select != 'q')
	{
		switch (select)
		{
		case 'a':
			cout << "List a - 입력값: " << endl;
			cin >> weight;
			a.Insert(weight);
			break;
		case 'b':
			cout << "List b - 입력값: " << endl;
			cin >> weight;
			b.Insert(weight);
			break;
		case 'd':
			cout << "List a와 b에서 삭제값: " << endl;
			cin >> weight;
			if (a.Delete(weight))
				cout<<"List a에서" <<weight<<"값이 삭제되었다"<<endl;
			else
				cout << "List a에" << weight << "값이 없다" << endl;
			if (b.Delete(weight))
				cout << "List b에서" << weight << "값이 삭제되었다" << endl;
			else
				cout << "List b에" << weight << "값이 없다" << endl;
			break;
		case 'm': //a+b
			a.Merge(b);
			break;
		case 'p':
			cout << "List a의 출력: " << endl;
			cout << a << endl;
			cout << "List b의 출력: " << endl;
			cout << b << endl;

			break;
		default:
			cout << "WRONG INPUT  " << endl;
			cout << "Re-Enter" << endl;
		}

		cin >> select;
	}
	system("pause");
	return 0;
}


