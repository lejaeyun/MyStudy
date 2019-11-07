/* mazeAssignment,cpp - finding a path through a maze
학번: 201624548
이름: 이재윤
github id: lejaeyun@naver.com
*/
#include <iostream>
#include <fstream>
#include "stack.h"
#include "maze.h"
using namespace std;


/*
maze[][], mark[][]를 class의 private data member로 선언
main()에서는 class의 public function의 호출로 미로 찾기
*/

void main() {
	Maze* m = new Maze();
	int result, count;
	struct offsets start, end;
	do {
		m->randomInitialize();
		cout << *m << endl;//난수를 사용하여 생성된 maze[][]을 출력
		count = 0;
		do {
			start = m->getNextStart();
			end = m->getNextEnd();
			result = m->findPath(start, end);
		} while (!result && count++ < 2 * ROWS);
	} while (!result);
	cout << "start : " << start.a << " " << start.b << "end : " << end.a << " " << end.b << endl;
	cout << m << endl;//미로 경로는 9로 출력
	system("pause");
}
