#ifdef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct listint_s: for a singly linked list
 * @n: the integer
 * @next: this points to the next node
 *
 * Desc: singly linked list node structure
 */

size_t print_listint(const listint_t *h);
listint_t *addnodeint(listint_t **head, const int n);
void free_listint(listint_s *h);
int check_cycle(listint_t *list);

#endif /* LIST_H */
