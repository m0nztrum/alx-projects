#include "main.h"
#include <stdio.h>
/**
 * swap_int - swaps the value of 2 integers
 * @a: pointer to 1st value
 * @b: pointer to 2nd value
 */
void swap_int(int *a, int *b)
{
	int c;

	c = *a;
	*a = *b;
	*b = c;
}
