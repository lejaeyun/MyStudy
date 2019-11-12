/* knightwalk.cpp - knight walk simulation
학번:
이름:
github id:
*/
#include "knightWalk.h"
int WalkKnight(Chessboard g, const struct Offsets startPosition);
void MarkNth(Chessboard g, const struct Offsets startPosition);

int Chessboard::Mark(const Offsets a, const Offsets b) {
	if (*(Term + a.a * cols + a.b) == 0 && *(Term + b.a * cols + b.b) != 0) {
		*(Term + a.a * cols + a.b) = *(Term + b.a * cols + b.b) + 1;
		return 1;
	}
	return 0;
}

void Chessboard::SimpleMark(const Offsets a) {
	*(Term + a.a * cols + a.b) += 1;
}

//확인
int Chessboard::CheckComplete() {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (*(Term + cols * i + j) == 0) {
				return 0;
			}
		}
	}
	return 1;
}
// 초기화
void Chessboard::initialize() {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			*(Term + cols * i + j) = 0;
		}
	}
}

// 초기화
void Chessboard::Final() {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			*(Term + cols * i + j) -= 1;
		}
	}
}

//(0 <= a <= 7 && 0 <= b <= 7)이면 return 1
int Chessboard::CheckBoundary(Offsets nextPosition) {
	if (nextPosition.a >= 0 && nextPosition.a <= 7) {
		if (nextPosition.b >= 0 && nextPosition.b <= 7) {
			return 1;
		}
	}
	return 0;
}

int WalkKnight(Chessboard g, const struct Offsets startPosition);
int main(void) {
Chessboard g;
	int xStart, yStart;
	cout << endl << "시작할 위치(x, y) 입력: ";
	cin >> xStart >> yStart;
	struct Offsets startPosition;
	startPosition.a = xStart; 	startPosition.b = yStart;
	WalkKnight(g, startPosition);
	cout << endl << "Work path::" << endl;
	cout << g << endl;
	MarkNth(g, startPosition);
	cout << endl << "Mark nth visiting path::" << endl;
	cout << g;
	system("pause");
	return 1;
}

int WalkKnight(Chessboard g, const struct Offsets startPosition) {
	//start from position
	directions knightMove;;//knight number
	struct Offsets currentPosition;
	currentPosition = startPosition;
	g.initialize();
	g.SimpleMark(currentPosition);
	while (!g.CheckComplete()) {
		knightMove = (directions)(rand() % 8);
		struct Offsets newPosition;
		newPosition.a = currentPosition.a + Move[knightMove].a;
		newPosition.b = currentPosition.b + Move[knightMove].b;
		if (!g.CheckBoundary(newPosition)) continue;
		else {
			g.SimpleMark(newPosition);
			currentPosition = newPosition;
		}
	}
	cout << g << endl;;
	return 0;
}

void MarkNth(Chessboard g, const struct Offsets startPosition) {
	Stack knightStack;
	Stack tmpstack;
	directions knightMove;;//knight number
	int nthLevel = 0;//1차 이동, 2차 이동을 표시하는 level
	struct Offsets currentPosition;
	currentPosition = startPosition;
	knightStack.Push(currentPosition);
	g.initialize();
	g.SimpleMark(currentPosition);
	while (!g.CheckComplete()) {
		currentPosition = knightStack.Pop();
		struct Offsets newPosition;
		knightMove = (directions)(rand() % 8);
		newPosition.a = currentPosition.a + Move[knightMove].a;
		newPosition.b = currentPosition.b + Move[knightMove].b;
		if (!g.CheckBoundary(newPosition)) continue;
		else {
			int chk = g.Mark(newPosition, currentPosition);
			knightStack.Push(newPosition);
			}
		/*
		while (!knightStack.Empty()) {
			currentPosition = knightStack.Pop();
			struct Offsets newPosition;
			for (int knightMove = 0; knightMove < 8; knightMove++) {
				newPosition.a = currentPosition.a + Move[knightMove].a;
				newPosition.b = currentPosition.b + Move[knightMove].b;
				if (!g.CheckBoundary(newPosition)) continue;
				else {
					int chk = g.Mark(newPosition, currentPosition);
					if (chk == 1)
						tmpstack.Push(newPosition);
				}
			}
		}

		while (!tmpstack.Empty()) {
			knightStack.Push(tmpstack.Pop());
		}
		*/
	}
	cout << g;
}