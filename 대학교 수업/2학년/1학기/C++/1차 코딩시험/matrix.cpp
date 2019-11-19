// 학번 : 201624548
// 이름 : 이재윤
// 깃허브 계정 : lejaeyun

// matrix - 2장 코딩 시험 19.3.21
// 소스코드 가장 윗 줄에 학번, 이름, 깃허브 계정을 반드시 작성할 것.
// 
// 제시된 5가지의 함수는 프로토타입만 작성되어 있으며, 해당 함수를 주석에서 설명하는 바와 같이 구현하여야 함.
// 함수를 호출하는 부분의 매개변수 중 '…'은 해당 함수에 알맞은 매개변수들로 바꿀 것.
#pragma warning(disable: 4996)
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>

#define ROWS 11 // 행
#define COLS 12 // 열

using namespace std;

void initializeMatrix(int (*a)[COLS], int rows); 
void randomWalk(int (*a)[COLS], int rows);
int findMAX(int(*a)[COLS], int rows);
float getAverage(int(*a)[COLS], int rows);
void showMatrix(int (*a)[COLS], int rows);

int main(void)
{
	srand((unsigned int)time(NULL));
	int A[ROWS][COLS];
	int select;
	while (1)
	{
		int n = 0;
		float average = 0;
		//1번 초기화 5번 출력, 2번 실행후 5번 출력으로 검사할 예정임
		cout << "\nSelect command 1: 행렬 초기화, 2: random walk,  3: find MAX, 4: get Average, 5. Display, 6: Quit => ";
		scanf("%d", &select);
		switch (select) {
		case 1:
			initializeMatrix(A, ROWS);
			break;

		case 2:
			randomWalk(A, ROWS);
			break;

		case 3:
			n = findMAX(A, ROWS);
			printf("MAX = %d\n", n);
			break;
		case 4:
			average = getAverage(A, ROWS);
			printf("avergae = %.2f\n", average);//소수점 두자리까지 출력, %f 사용
			break;
		case 5:
			showMatrix(A, ROWS);
			break;
		default:
			exit(0);
			break;
		}
	}
	system("pause");
	return 0;
}

// 변수 b를 사용하여 모든 원소를 0으로 초기화하는 함수를 작성.
// 넘겨받은 배열 a는, 아래에 제시된 코드와 같이 *b에 연결하여 사용해야 함.
void initializeMatrix(int(*a)[COLS], int rows)
{
	int *current;
	int *endArray;
	int index = 0;
	for (current = &a[0][0], endArray = current + COLS * rows ; current < endArray; current++,index++)
	{
		//함수 구현
		*current = 0;
	}
}

// 난수 i, j를 생성, 배열 a[i][j]의 값을 1씩 증가시키는 것을 반복하는 함수를 작성.
// 반복의 종료 조건은 배열 a의 모든 원소가 한번 이상 증가했을 경우, 즉 모든 원소가 0이 아닐때 반복을 종료함.
// 배열 [][] 형식 사용 금지, 대신에 **, *[]와 같은 형식을 사용할 것.
//
// Tip. 난수 생성 방법 : rand() % n; , n은 최댓값 + 1
// ex) 0 <= i <= 10 을 생성하고 싶을 경우 => int i = rand() % 11;
void randomWalk(int (*a)[COLS], int rows)
{
	//함수 구현
	int result = 0, RandNum, checknum, check_con;
	int * NextPoint = &a[0][0];
	int * FirstPoint = &a[0][0];

	// 0 위 1 오 2 아 3 왼
	// 대각선 추가
	while (result == 0)
	{
		RandNum = rand() % 4;
		if (RandNum == 0)
		{
			checknum = 0, check_con = 0;
			for (int * CheckPoint = FirstPoint; checknum < ROWS; CheckPoint = CheckPoint + 1, checknum++)
			{
				if (NextPoint == CheckPoint)
				{
					check_con = 1;
					break;
				}
			}
			if (check_con == 1)
				continue;
			NextPoint = NextPoint - ROWS;
		}
		else if (RandNum == 1)
		{
			checknum = 0, check_con = 0;
			for (int * CheckPoint = FirstPoint + (ROWS-1); checknum < COLS; CheckPoint = CheckPoint + ROWS, checknum++)
			{
				if (NextPoint == CheckPoint)
				{
					check_con = 1;
					break;
				}
			}
			if (check_con == 1)
				continue;
			NextPoint = NextPoint + 1;
		}
		else if (RandNum == 2)
		{
			checknum = 0, check_con = 0;
			for (int * CheckPoint = FirstPoint + (ROWS * (COLS - 1)); checknum < ROWS; CheckPoint = CheckPoint + 1, checknum++)
			{
				if (NextPoint == CheckPoint)
				{
					check_con = 1;
					break;
				}
			}
			if (check_con == 1)
				continue;
			NextPoint = NextPoint + ROWS;
		}
		else if (RandNum == 3)
		{
			checknum = 0, check_con = 0;
			for (int * CheckPoint = FirstPoint; checknum < COLS; CheckPoint = CheckPoint + ROWS, checknum++)
			{
				if (NextPoint == CheckPoint)
				{
					check_con = 1;
					break;
				}
			}
			if (check_con == 1)
				continue;
			NextPoint = NextPoint - 1;
		}

		*NextPoint = *NextPoint + 1;

		for (int * endArray = FirstPoint + (COLS * rows), index = 0; FirstPoint + index < endArray; index++)
		{
			if (*(*a + index) == 0)
			{
				result = 0;
				break;
			}
			if (index + 1 == (COLS * rows))
			{
				result = 1;
				break;
			}
				
		}
	}


} 

// 배열에 있는 모든 원소 중 가장 큰 값을 리턴하는 함수를 작성.
// 넘겨받은 배열 a는, 새로운 배열 c에 연결하여 사용해야 함.
// 배열 [][] 형식 사용 금지, 대신에 *c와 같은 포인터 형식을 사용할 것.
int findMAX(int(*a)[COLS], int rows)
{
	int *c = &a[0][0];
	int index = 0, max = 0;

	for (int index_rows = 0; index_rows < rows; index_rows++)
	{
		for (int index_cols = 0; index_cols < COLS; index_cols++)
		{
			if (max < *(c + index_rows * index_cols))
				max = *(c + index_rows * index_cols);
		}
	}

	
	return max;
}

// 배열에 있는 모든 원소의 평균값을 계산하여 리턴하는 함수를 작성.
// 넘겨받은 배열 a는, 아래에 제시된 코드와 같이 *t 및 **p에 연결하여 사용해야 함.
// 배열 [][] 방식 사용 금지, 대신에 *p와 같은 포인터 형식을 사용할 것.
float getAverage(int(*a)[COLS], int rows)
{
	int *t = *a;
	int **p;
	p = &t;
	float avg = 0;
	for (int * endArray = *p + (COLS * rows); t < endArray; t++)
	{
		avg = avg + *t;
	}

	return (avg / (COLS*rows));
	//함수 구현

}

// 배열에 있는 모든 원소를 화면에 바둑판 행렬로 출력하는 함수를 작성.
// 넘겨받은 배열 a는, 아래에 제시된 코드와 같이 *pt 및 **p에 연결하여 사용해야 함.
// 배열 [][] 방식 사용 금지, 대신에 *p와 같은 포인터 형식을 사용할 것.
void showMatrix(int (*a)[COLS], int rows)
{
	int *pt;
	int **p;
	pt = &a[0][0];
	p = &pt;
	int Index = 0;
	printf("showMatrix:: 행렬 출력\n");
	// 함수 구현
	for (int * endArray = *p + (COLS * rows); pt < endArray; pt++)
	{
		printf("%2d ",*pt);
		Index++;
		if (Index % COLS == 0)
			printf("\n");
	}
	printf("\n\n");
}
