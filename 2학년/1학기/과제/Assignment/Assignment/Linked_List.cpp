#include "pch.h"
#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable: 4996)

typedef struct node_st {
	int element;
	struct node_st* next;
} node;

void HPush(node* head, int new_element);
void deleteNode(node* head, int position);

void HPush(node* head, int new_element) {
	node* new_node = (node*)malloc(sizeof(node));

	new_node->element = new_element;
	new_node->next = head->next;
	head->next = new_node;
}


void deleteNode(node* head, int position) {
	int dpos = 0;
	node* free_node = nullptr;
	node* bef_node = nullptr;
	for (node* del_node = head; dpos <= position + 1; dpos++, del_node = del_node->next) {
		if (dpos == position - 1) {
			bef_node = del_node;
		}
		else if (dpos == position) {
			if (del_node->next == NULL) {
				bef_node->next = NULL;
				break;
			}
			else {
				free_node = del_node;
			}
		}
		else if (dpos == position + 1) {
			bef_node->next = del_node;
		}
	}
	free(free_node);
}

void printList(node* head)
{
	node* list = head->next;
	while (list != NULL)
	{
		printf(" %d ", (int*)list->element);
		list = list->next;
	}
	printf("\n");
}

void FreeNode(node* head)
{
	node* list = head->next;
	node* beflist = NULL;
	while (list != NULL)
	{
		beflist = list;
		list = list->next;
		free(beflist);
	}
}

int main() {
	int pos, size;

	node* head = (node*)malloc(sizeof(node));
	head->next = NULL;
	printf("Enter the size : ");
	scanf("%d", &size);
	for (int i = 0; i < size; i++) {
		HPush(head, i+1);
	}
	
	printf("Linked List: ");
	printList(head);

	printf("Select position: ");
	scanf("%d", &pos);
	printf("Linked List after deletion at position %d: ", pos);

	/* deleteNode */
	deleteNode(head, pos);
	printf("Linked List: ");
	printList(head);

	FreeNode(head);
	free(head);

	return 0;
}
