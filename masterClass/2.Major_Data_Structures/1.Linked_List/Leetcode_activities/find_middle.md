## Implement the `find_middle_node` Method for the `LinkedList` Class

**Note**: This `LinkedList` implementation does not have a `length` member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

### Requirements:

- The method should use a **two-pointer approach**, where one pointer (`slow`) moves one node at a time and the other pointer (`fast`) moves two nodes at a time.
- When the `fast` pointer reaches the end of the list or has no next node, the `slow` pointer should be at the middle node of the list.

- The method should return:

  - The middle node if the number of nodes is odd.
  - The **first node of the second half** of the list if the list has an even number of nodes.

- The method should **only traverse the linked list once**. In other words, you can only use one loop.
