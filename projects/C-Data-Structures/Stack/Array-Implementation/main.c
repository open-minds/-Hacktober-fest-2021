#include <stdlib.h>
#include <stdio.h>
int n = 0;
typedef struct stack stack;
struct stack{
    int top;
    int capacity;
    int *array; 
};
stack *create(int capacity)
{
    stack *new = malloc(capacity * sizeof(stack));
    new->capacity = capacity;
    new->top = -1;
    new->array = malloc(sizeof(int) * capacity);
    return new;
};
int *resize(int *array)
{
    int new_size = n * 2, i = 0;
    int *new_array = malloc(sizeof(int) * new_size);
    for(; i < new_size ; i++)
    {
        *(new_array+i) = *(array+i);
    }
    return new_array;
}
int push(stack *new, int number)
{
    (new->top)++;
    if(new->top > new->capacity)
    {
        printf("Overflowed\n");
        // we copy the actual array , and put it in a new array
        // the new_array.size = actual_array.size * 2
        // so if the actual_array has n elements
        // to copy the elements , it took us O(n).
        // Here we understand the benefits of linked-lists
        new->array = resize(new->array);
        *(new->array + new->top) = number;
        return 1;
    }

    *(new->array + new->top) = number;
    return 0;
}
void print(stack *new)
{
    for(int i = 0 ; i <= new->top ; i++)
    {
        printf("Element %d : %d\n", i, *(new->array+i));
    }
}
void is_full(stack *new)
{
    if(new->top == new->capacity - 1)
    {
        printf("Stack is full\n");
        return;
    }
    else
        printf("Stack isn't full , it remains %d elements to be full\n", (new->capacity - new->top - 1));
}
int main(void)
{
    printf("How many elements in the stack : ");
    do
    {
        scanf("%d", &n);
    } while(n > 10 || n <= 0);
    stack *first = create(n);
    push(first, 5);
    push(first, 3);
    push(first, 5);
    print(first);
    is_full(first);

    return 0;
}