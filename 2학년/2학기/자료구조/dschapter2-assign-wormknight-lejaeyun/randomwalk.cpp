/* randomwalk.cpp - random walk simulation 
학번:
이름:
github id:
*/
#include "randomwalk.h"
void Walk(Goboard g, const struct Offsets position);

void Goboard::Mark(const Offsets a) {
	*(Term + a.a * cols + a.b) += 1;
}
//확인
int Goboard::CheckComplete() {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if ( *(Term + cols * i + j) == 0) {
				return 0;
			}
		}
	}
	return 1;
}
// 초기화
void Goboard::initialize() {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			*(Term + cols * i + j) = 0;
		}
	}
}

//(0 <= a <= 18 && 0 <= b <= 18)이면 return 1
int Goboard::CheckBoundary(Offsets nextPosition) {
	if (nextPosition.a >= 0 && nextPosition.a <= 18) {
		if (nextPosition.b >= 0 && nextPosition.b <= 18){
			return 1;
		}
	}
	return 0;
}
// constructor, initialize,CheckComplete, CheckBoundary, Mark, operator<<를 구현
int main(void) {
	Goboard g;
	int xStart, yStart;
	cout << endl<<"시작할 위치(x, y) 입력: ";
	cin >> xStart >> yStart;
	struct Offsets startPosition;
	startPosition.a = xStart; 	startPosition.b = yStart;
	Walk(g, startPosition);
	cout << endl<< "Work path::"<<endl;
	cout << g;
	system("pause");
	return 1;
}

void Walk(Goboard g, const struct Offsets position) {
	//start from position
	directions randomMove;;//random number
	struct Offsets currentPosition;
	currentPosition = position;
	g.initialize();
	g.Mark(position);
	int i = 0;
	while (!g.CheckComplete()) {
		i++;
		randomMove = (directions)(rand() % 8);//난수를 사용하여 8가지 중에서 선택
		struct Offsets newPosition;
		newPosition.a = currentPosition.a + Move[randomMove].a;
		newPosition.b = currentPosition.b + Move[randomMove].b;
		if (!g.CheckBoundary(newPosition)) continue;
		else {
			g.Mark(newPosition);
			currentPosition = newPosition;
		}
	}
	cout << g;
}