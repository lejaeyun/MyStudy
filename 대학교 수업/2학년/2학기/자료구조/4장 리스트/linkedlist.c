#include <stdio.h>
#include <stdlib.h>

typedef struct node_st {
    int element;
    struct node_st* next;
} node;

void Push(node* head, int new_element);
void deleteNode(node* head, int position);

void Push(node* head, int new_element) {
    node* new_node = (node*) malloc(sizeof(node));

    new_node->element = new_element;
    new_node->next = head->next;
    head->next = new_node;
}

void deleteNode(node* head, int position){
	int dpos = 0;
	node* free_node = NULL;
	node* bef_node = NULL;
	for (node* del_node = head; dpos <= position + 1; dpos++,del_node = del_node->next){
		if (dpos == position - 1) {
			bef_node = del_node;
		}
		else if (dpos == position) {
			if (del_node->next == NULL){
				bef_node->next = NULL;
				free_node = del_node;
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
        printf(" %d ", list->element); 
        list = list->next; 
    } 
    printf("\n");
} 

int main() {
    int pos;

    node* head = (node*)malloc(sizeof(node));
    head->next = NULL;

    for(int i = 1; i <= 20; i++){
	Push(head, i);	
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

    return 0;
}
