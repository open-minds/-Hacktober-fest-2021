#include <stdlib.h>
#include <stdio.h>
int n, top = -1; // top starting at -1
void init(int *array);
void print(int *array);
void push(int *array, int x);
int *resize(int *array);
void pop();