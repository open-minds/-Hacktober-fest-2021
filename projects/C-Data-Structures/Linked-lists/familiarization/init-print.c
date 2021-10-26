#include "init-print.h"
int main(int argc, char const *argv[])
{
    node *head = (node *)malloc(sizeof(node));
    node *second  = (node *)malloc(sizeof(node));
    node *third = (node *)malloc(sizeof(node));       
    node_value(head);
    head->next = second;
    node_value(second);
    second->next = third;
    node_value(third);
    third->next = NULL;
    print_list(head);

    free(head);
    free(second);
    free(third);
    return 0;
}
void node_value(node *n)
{
    printf("Enter the value of the node : ");
    scanf("%d", &(n->value));
    i++;
}
void print_list(node *n)
{
    for(int i = 1 ; n != NULL ; i++, n = n->next)
    {
        printf("Node-%d value : %d\n", i, n->value);
    }
}