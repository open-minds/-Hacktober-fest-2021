#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
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
int pop(node **root)
{
    node *temp = *root;
    int popped_number = temp->value;
    *root = temp->next;
    free(temp);
    return popped_number;
}
bool is_balanced(node *root, char *string)
{
    bool test = true;
    for(int i = 0 ; i < strlen(string); i++)
    {
        switch(string[i])
        {
            case ')':
                if(pop(&root) == '(')
                {
                    printf("found\n");
                    return test;
                }
                else
                    test = false;
            break;

            case ']':
                if(pop(&root) == '[')
                {
                    return test;                
                }
                else
                    test = false;
            break;

            case '}':
                if(pop(&root) == '{')
                {
                    return test;
                }
                else
                    test = false;
            break;
            default:
                test = false;
            break;
        }
    }
    return test;
}
int main(int argc, char const *argv[])
{
    char *string = malloc(sizeof(char) * 20);
    printf("Enter a string : "); // (name : [wassim]) 
    fgets(string,20, stdin);
    node *root = NULL;
    for(int i = 0, test = 0; i < strlen(string) ; i++)
    {
        if(string[i] == '(' || string[i] == '[' || string[i] == '{')
        {
            push(&root,string[i]);
            test++;
        }
        if(test == 0)
        {
            printf("Un-balanced\n");
            return 1;
        }
    }
    
    if(!is_balanced(root,string))
    {
        printf("un-balanced\n");
        return 0;
    }
    else
        printf("balanced\n");
    return 0;
}
