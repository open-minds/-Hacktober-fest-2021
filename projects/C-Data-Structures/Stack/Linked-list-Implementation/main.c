#include "main.h"

int main(int argc, char const *argv[])
{
    node *head = NULL;
    int n, x;
    printf("How many elements in the stack : ");
    do
    {
        scanf("%d", &n);
    } while(n > 10 || n <= 0);
    for(int i = 0 ; i < n ; i++)
    {
        printf("Enter the element : ");
        scanf("%d", &x);
        push(&head, x);
    }
    print(head);
    printf("Poped element : %d\n", pop(&head));
    deallocate(&head);
    push(&head, 20);
    print(head);
    return 0;
}
void print(node *root)
{
    for(node *curr = root ; curr != NULL ; curr = curr->next)
    {
        printf("%d ", curr->value);
    }
    printf("\n");
}
void push(node **root, int x)
{
    node *temp = malloc(sizeof(node));
    temp->value = x;
    if(*root == NULL)
    {
        *root = temp;
        return;
    }
    temp->next = *root;
    *root = temp;
}
int pop(node **root)
{
    if(*root == NULL)
    {
        printf("Empty stack\n");
    }
    node *temp = *root;
    int poped_number = temp->value;
    *root = (*root)->next;
    free(temp);
    return poped_number;

}
void deallocate(node **root)
{
    if(*root == NULL)
    {
        return;
    }
    node *temp = NULL;
    while(*root != NULL)
    {
        temp = *root;
        *root = (*root)->next;
        free(temp);
    }
}