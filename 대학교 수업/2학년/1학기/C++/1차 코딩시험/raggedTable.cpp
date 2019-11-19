// 학번 : 201624548
// 이름 : 이재윤
// 깃허브 계정 : lejaeyun

// raggedTable - 2장 코딩 시험 19.3.21
// 소스코드 가장 윗 줄에 학번, 이름, 깃허브 계정을 반드시 작성할 것.
//
// 본 소스코드는 문법적 오류 또는 논리적 오류를 포함하고 있다. 전체 소스코드이 목표로 하는 동작을 예상하여,
// 수정이 필요한 부분을 재작성하여 프로그램이 본래 목적대로 동작할 수 있도록 하여야 함.

#pragma warning(disable: 4996)
#include <stdio.h>
#include <stdlib.h>

int main() {
	int **t;
	int row, col;
	int rowIndex;
	printf("행의 수를 입력하세요:");
	scanf_s("%d", &row);


	// 길이가 다른 배열(ragged array)를 동적 할당하는 부분
	t = (int **)calloc(row, sizeof(int*));
	for (rowIndex = 0; rowIndex < row; rowIndex++) {
		printf("%d행 열의 수를 입력하세요:", rowIndex);
		scanf("%d", &col);
		*(t + rowIndex) = (int *)calloc(col+1, sizeof(int));//수정해야 함
		//각 행의 첫 열에 열의 개수 저장
		*(*(t + rowIndex)) = col;//수정해야 함
	}

	// 각 row의 column마다 col--를 저장하는 반복문
	int cnt; // 각 row의 column 갯수
	for (int i = 0; i<  row; i++) {
		cnt = **(t + i);									// 수정 필요
		for (int j = 0; j<cnt; j++) {
			*(*(t + i) + j) = cnt - j;						// 수정 필요
		}
		cnt++;
	}

	// 각 row의 column의 값을 화면에 출력하는 반복문
	//int cnt; // 각 row의 column 갯수
	printf("T1[][]의 원소 값\n");
	for (int i = 0; i< row; i++) {
		cnt = **(t+i);									// 수정 필요
		for (int j = 0; j<cnt; j++) {
			printf("%d ", *(*(t + i) + j));						// 수정 필요
		}
		printf("\n");
		cnt++;
	}

	// 동적할당 받은 2차원 배열의 경우 1차원 배열을 먼저 해제한 후 더블포인터를 해제해야 함.
	for (rowIndex = 0; rowIndex < row; rowIndex++)
	{
		free(t[rowIndex]);
	}
	free(t);

	system("pause");
	return 0;
}
