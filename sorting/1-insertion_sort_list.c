#include "sort.h"

/**
 * swap_nodes - Swap two nodes in a listint_t doubly-linked list.
 * @a: A pointer to the first node to swap.
 * @b: The second node to swap.
 */

void swap_nodes(listint_t **h, listint_t *n1, listint_t *n2)
{
	if (n1->prev != NULL)
		n1->prev->next = n2;
	else
		*h = n2;

	if (n2->next != NULL)
		n2->next->prev = n1;

	n1->next = n2->next;
	n2->prev = n1->prev;
	n1->prev = n2;
	n2->next = n1;
}

/**
 * insertion_sort_list - Sorts a doubly linked list of integers
 *                       using the insertion sort algorithm.
 * @list: A pointer to the head of a doubly-linked list of integers.
 *
 * Description: Prints the list after each swap.
 */



void insertion_sort_list(listint_t **list)
{
	listint_t *current, *prev, *temp;

	if (list == NULL || *list == NULL || (*list)->next == NULL)
		return;
	for (current = (*list)->next; current != NULL; current = temp)
	{
		temp = current->next;

		prev = current->prev;
		while (prev != NULL && prev->n > current->n)
		{
			swap_nodes(list, prev, current);
			print_list(*list);
			prev = current->prev;
		}
	}
}

