// A program to reverse a doubly linked list 
// it can be a good approach to reverse a singly linked list
// by addign a new pointer in the struct to the previous node
// But ! It costs you memory 
// so it's mainly the iterative way to reverse a doubly linked list
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
    reverse_dll(&head);
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
void reverse_dll(node **root)
{
    if(*root == NULL)
    {
        return;
    }
    node *curr = *root, *temp = NULL;
    for(; curr != NULL ; curr = curr->previous)
    {
        temp = curr->previous;
        curr->previous = curr->next;
        curr->next = temp;
    }
    *root = temp->previous;

}