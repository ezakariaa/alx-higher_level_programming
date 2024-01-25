#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
* print_dlistint - function that prints all the elements of a dlistint_t list.
* @h: The dlistint_t list to prints
*
* Return: the number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
	int leng = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		++leng;
		h = h->next;
	}

	return (leng);
}
