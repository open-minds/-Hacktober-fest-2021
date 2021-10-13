#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct stack_node stack_node;
struct stack_node
{
    char car;
    stack_node *next;
};
void push(stack_node **root, char car)
{
    stack_node *temp = malloc(sizeof(stack_node));
    temp->car = car;
    if(root == NULL)
    {
        *root = temp;
        return;
    }
    temp->next = *root;

    *root = temp;
}
char pop(stack_node *root)
{
    char popped_char = root->car;
    root = root->next;
    return popped_char;
    
}
void print(stack_node *root)
{
    for(stack_node *temp = root ; temp != NULL ; temp = temp->next)
    {
        printf("%c", temp->car);
    }
    printf("\n");
}
int main(int argc, char const *argv[])
{
    stack_node *root = NULL;
    char string[20];
    printf("Enter the string you want to reverse\n");
    fgets(string ,20 ,stdin);
    for(int i = 0 ; i < strlen(string); i++)
    {
        push(&root, string[i]);
    }
    print(root);


    return 0;
}
