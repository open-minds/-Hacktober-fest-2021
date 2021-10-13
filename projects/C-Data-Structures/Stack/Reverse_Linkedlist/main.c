#include <stdlib.h>
#include <stdio.h>
typedef struct node node;
struct node {
    int value;
    node *next;
};
void push(node **root, int value)
{
    node *temp = malloc(sizeof(node));
    temp->value = value;
    if(*root == NULL)
    {
        *root = temp;
        return;        
    }
    temp->next = *root;
    *root = temp;
}
void insert_node(node **root, int value)
{
    node *temp = malloc(sizeof(node));
    temp->value = value;
    temp->next = NULL;
    if(*root == NULL)
    {
        *root = temp;
        return;
    }
    node *curr = *root;
    for(; curr->next != NULL ; curr = curr->next);
    curr->next = temp;
    return;
    
}
void print(node *root)
{
    for(node *temp = root ; temp != NULL ; temp = temp->next)
    {
        printf("%d ", temp->value);
    }
    printf("\n");
}
int pop(node **root)
{
    node *temp = *root;
    int popped_number = temp->value;
    *root = temp->next;
    return popped_number;
}

int main(int argc, char const *argv[])
{
    node *root = NULL;
    node *stack = NULL;
    insert_node(&root, 1);
    insert_node(&root, 2);
    insert_node(&root, 3);
    // pushing elements into the stack
    for(node *temp = root ; temp != NULL ; temp = temp->next)
    {
        push(&stack, temp->value);
    }
    // Stack == last in , first out ; so we pop again into the linked-list
    for(node *temp = root ; temp != NULL ; temp = temp->next)
    {
        temp->value = pop(&stack);
    }
    print(root);
    return 0;
}
