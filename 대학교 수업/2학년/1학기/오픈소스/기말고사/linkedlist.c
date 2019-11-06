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

void printList(node* head) 
{ 
    node* list = head->next;
    while (list != NULL) 
    { 
        printf(" %d ", (int*) list->element); 
        list = list->next; 
    } 
    printf("\n");
} 

int main() {
    int pos;

    node* head = (node*)malloc(sizeof(node));
    head->next = NULL;

    Push(head, 1);
    Push(head, 2);
    Push(head, 3);
    Push(head, 4);
    Push(head, 5);
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
