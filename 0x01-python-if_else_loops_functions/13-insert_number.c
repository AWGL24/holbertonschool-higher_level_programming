#include "lists.h"
/**
 * insert_node - function that inserts a node
 * @head: pointer to the head of the list
 * @number: value of data
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	tmp = *head;
	new->n = number;
	if (tmp == NULL)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}

	while (tmp && tmp->next && tmp->next->n < number)
	{
		tmp = tmp->next;
	}
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
