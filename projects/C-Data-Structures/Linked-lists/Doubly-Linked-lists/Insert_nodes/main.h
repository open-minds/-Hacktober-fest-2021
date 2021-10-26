#include <stdlib.h>
#include <stdio.h>

typedef struct node node;
struct node {
    int value;
    node *next;
    node *previous;
};
void print(node *root);
void insert_end(node **root, int value);