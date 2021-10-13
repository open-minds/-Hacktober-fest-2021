// A program to implement Doubly linked list
// A doubly linked list is a typically a linked list with an 
// additional data type , which is a pointer to the previous node
#include "main.h"

int main(int argc, char const *argv[])
{
    node *head = malloc(sizeof(node));
    head->value = 0;
    head->previous = NULL;
    head->next = NULL;
    int n,x;
    printf("How many numbers in the list : ");
    scanf("%d", &n);
    for(int i = 0 ; i < n ; i++)
    {
        printf("Enter the %d-Number: ", i+1);
        scanf("%d", &x);
        insert_end(&head,x);
    }
    print(head);
    return 0;
}
void insert_end(node **root, int value)
{
    node *new = malloc(sizeof(node));
    new->value = value;
    new->next = NULL;
    node *curr = *root;
    for( ; curr->next != NULL ; curr = curr->next);
    curr->next = new;
    new->previous = curr;
}
void print(node *root)
{
    node *curr = root;
    for(; curr != NULL ; curr = curr->next)
    {
        printf("%d ", curr->value);
    }
    printf("\n");
}