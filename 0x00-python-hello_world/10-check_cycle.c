#include "lists.h"
/**
 * check_cycle - check if theres a cycle in list.
 * @list: Head node
 * Return: 1 if theres a cycle and 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *forward;

	current = list;
	forward = list;

	while (current != NULL && forward != NULL && forward->next != NULL)
	{
		current = current->next;
		forward = forward->next->next;
		if (current == forward)
			return (1);
	}
	return (0);
}
