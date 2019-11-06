#include <iostream>
#include <stack>
using namespace std;

bool check(int a[][100], int i, int j){
	for (int row = 0; row < i; row++) {
		for (int col = 0; col < j; col++)
		{
			if (a[row][col] == 0) {
				return true;
			}
		}
	}
	return false;
}

int main(void) {
	// 1¹ø
	/*
	int arr[100][100] = { 0 };
	int i = 0, j = 0;
	int n = 0, m = 0;
	int r = rand() % 8;
	while (check(arr, i, j) != false) {
		if (r < 3) {
			if (i - 1 < 0)
				continue;
			else if (((j - 1 < 0) and r == 0) or (j + 1 > m and r == 2))
				continue;

			else {
				if (r == 0)
					arr[i - 1][j - 1] = arr[i - 1][j - 1] + 1;
				else if (r == 1)
					arr[i - 1][j] = arr[i - 1][j] + 1;
				else if (r == 2)
					arr[i - 1][j + 1] = arr[i - 1][j + 1] + 1;
			}
		}
		else if (r < 5)
		{
			if ((j - 1 < 0 and r == 3) or (j + 1 > m and r == 4))
				continue;

			if (r == 3)
				arr[i][j - 1] = arr[i][j - 1] + 1;
			else if (r == 4)
				arr[i][j + 1] = arr[i][j + 1] + 1;
		}
		else if (r < 8)
		{
			if (i + 1 > n)
				continue;
			else if (((j - 1 < 0) and r == 5) or (j + 1 > m and r == 7))
				continue;

			if (r == 5)
				arr[i + 1][j - 1] = arr[i + 1][j - 1] + 1;
			else if (r == 6)
				arr[i + 1][j] = arr[i + 1][j] + 1;
			else if (r == 7)
				arr[i + 1][j + 1] = arr[i + 1][j + 1] + 1;

		}
	}
	*/

	// 2¹ø
	int n = 8, m = 8;
	int tarr[n][m] = { 0 }, nxt;
	int x = 3, y = 5;
	int num = 1;
	stack <int> queue;
	stack <int> visit;
	queue.push(x * n + y);

	while (!queue.empty()) {
		while (!queue.empty()) {
			nxt = queue.top();
			queue.pop();
			x = nxt / n;
			y = nxt % n;
			if (tarr[x][y] == 0) {
				tarr[x][y] = num;
			}

			if (x - 2 >= 0)
			{
				if (y - 1 >= 0 and tarr[x - 2][y - 1] == 0)
					visit.push((x - 2) * n + y - 1);

				if (y + 1 < m and tarr[x - 2][y + 1] == 0)
					visit.push((x - 2) * n + y + 1);
			}

			if (x - 1 >= 0)
			{
				if (y - 2 >= 0 and tarr[x - 1][y - 2] == 0)
					visit.push((x - 1) * n + y - 2);

				if (y + 2 < m and tarr[x - 1][y + 2] == 0)
					visit.push((x - 1) * n + y + 2);
			}

			if (x + 1 < n) 
			{
				if (y - 2 >= 0 and tarr[x + 1][y - 2] == 0)
					visit.push((x + 1) * n + y - 2);

				if (y + 2 < m and tarr[x + 1][y + 2] == 0)
					visit.push((x + 1) * n + y + 2);
			}

			if (x + 2 < n)
			{
				if (y - 1 >= 0 and tarr[x + 2][y - 1] == 0)
					visit.push((x + 2) * n + y - 1);

				if (y + 1 < m and tarr[x + 2][y + 1] == 0)
					visit.push((x + 2) * n + y + 1);
			}

		}

		while (!visit.empty()) {
			queue.push(visit.top());
			visit.pop();
		}

		num++;
	}
	
	//showtext
	
	for (int ii = 0; ii < n; ii++) {
		for (int jj = 0; jj < m; jj++)
		{
			tarr[ii][jj] = tarr[ii][jj] - 1;
			cout << tarr[ii][jj] << " ";
		}
		cout << endl;
	}
	system("pause");

	return 0;
}