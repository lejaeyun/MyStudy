#include "pch.h"
#include <iostream>
#pragma warning(disable: 4996)

int main()
{
	int size;
	printf("Enter size of array : ");
	scanf("%d", &size);
	int* Arr1 = (int*)malloc(size * sizeof(int));
	int* Arr2 = (int*)malloc(size * sizeof(int));
	printf("Input First array : ");
	for (int i = 0; i < size; i++) {
		scanf("%d", &Arr1[i]);
	}
	printf("Input Second array : ");
	for (int i = 0; i < size; i++) {
		scanf("%d", &Arr2[i]);
	}

	int *temp = Arr1;
	Arr1 = Arr2;
	Arr2 = temp;

	printf("\nOutput First array after swapping : ");
	for (int i = 0; i < size; i++) {
		printf("%d ", Arr1[i]);
	}
	printf("\nOutput Second array after swapping : ");
	for (int i = 0; i < size; i++) {
		printf("%d ", Arr2[i]);
	}
}
