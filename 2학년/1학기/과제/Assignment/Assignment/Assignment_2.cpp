#include "pch.h"
#include <iostream>
#pragma warning(disable: 4996)

int main()
{
	int size;
	scanf("%d", &size);
	int* arr = (int*)malloc(size * size * sizeof(int));
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			arr[i*size + j] = 0;
			if (i == j) {
				arr[i*size + j] = 1;
			}
		}
	}

	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			printf("%d ", arr[i*size + j]);
		}
		printf("\n");
	}
	free(arr);
}