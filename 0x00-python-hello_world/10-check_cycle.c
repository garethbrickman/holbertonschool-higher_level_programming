#include "lists.h"

/**
 * check_cycle - function checks if linked list has a cycle in it
 *
 *@list: listint_t linked list to be checked
 *
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	struct listint_s *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}
