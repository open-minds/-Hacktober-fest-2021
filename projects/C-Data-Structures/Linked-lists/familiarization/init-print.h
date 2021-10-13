#include <stdlib.h>
#include <stdio.h>
int i = 1;
typedef struct node node;
struct node
{
    int value;
    node *next; 
};
void node_value(node *n);
void print_list(node *n);