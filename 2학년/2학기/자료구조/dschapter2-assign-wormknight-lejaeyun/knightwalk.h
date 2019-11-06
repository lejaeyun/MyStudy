/* knightwalk.h - knightm Walk에 필요한 header file 
학번:
이름:
github id:
knight(기사)가 현 위치에서 8가지 방향으로 random하게 이동한다.
*/

#include <iostream>
using namespace std;
struct Offsets {
	int a, b;
};
enum directions { NE, EN, ES, SE, SW, WS, WN, NW };
Offsets Move[8] = { {1,-2},{2,-1},{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2} };
//[g,h] <= [i,j], g = i + move[NE].a; h = j + move[NE].b;

class Stack {
	Offsets data[50];
	int nElements;
public:
	Stack() :
		nElements(0)
	{}
	void Push(Offsets elem);
	Offsets Pop();
	int Number();
	int Empty();
};
void Stack::Push(Offsets elem) {
	data[nElements] = elem;
	nElements++;
}

Offsets Stack::Pop() {
	nElements--;
	return data[nElements];
}

int Stack::Number() {
	return nElements;
}

int Stack::Empty() {
	return (nElements == 0);
}

class Chessboard {
public:
	Chessboard() { };//체스판 배열을 생성자로 호출
	void initialize();//체스판 배열의 각 cell = 0으로 초기화
	int CheckComplete();//모든 cell이 nonzero면 return 1
	void Chessboard::Final();
	int CheckBoundary(Offsets nextPosition);//(0<= a <= 7 && 0 <= b <= 7)이면 return 1
	void SimpleMark(const Offsets chess);//(*Term)++; 한번 방문시마다 1 증가
	int Chessboard::Mark(const Offsets a, const Offsets b);//(*Term)++; 한번 방문시마다 1 증가
	friend ostream& operator << (ostream& stream, Chessboard& s) {
		for (int i = 0; i < s.rows; i++) {
			for (int j = 0; j < s.cols; j++) {
				stream << *(s.Term + s.cols * i + j) << " ";
			}
			stream << endl;
		}
		return stream;
	}
private:
	int rows = 8, cols = 8;
	int* Term = new int[64];//1차원 배열을 pointer를 사용하여 저장
};