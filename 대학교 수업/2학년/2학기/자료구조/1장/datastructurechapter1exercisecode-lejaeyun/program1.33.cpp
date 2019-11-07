//Program 1.33: Matrix transpose
void Transpose(int** a, int n)
{
	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n; j++)
			swap(a[i][j], a[j][i]);
}
