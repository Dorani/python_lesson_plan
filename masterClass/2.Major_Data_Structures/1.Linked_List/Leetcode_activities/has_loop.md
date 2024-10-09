## Linked List: Detect Loop (**Interview Question**)

Write a method called `has_loop` that is part of the LinkedList class.

The method should be able to detect if there is a cycle or loop present in the linked list.

You are required to use **Floyd's cycle-finding algorithm** (also known as the "tortoise and the hare" algorithm) to detect the loop.

### Algorithm Overview:

- The algorithm uses two pointers:
  - A **slow pointer** that moves one step at a time.
  - A **fast pointer** that moves two steps at a time.
- If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

### Method Guidelines:

1. **Initialize two pointers**: `slow` and `fast`, both pointing to the head of the linked list.

2. **Traverse the list**:

   - The slow pointer moves one step at a time.
   - The fast pointer moves two steps at a time.

3. **Detect loop**:
   - If there is a loop, the fast pointer will eventually meet the slow pointer. If this happens, return `True`.
4. **No loop**:
   - If the fast pointer reaches the end of the list or encounters a `None` value, it means there is no loop in the list. In this case, return `False`.

### Important Note:

If your linked list contains a loop, it indicates a flaw in its implementation. This situation can manifest in several ways and should be addressed during debugging or testing.
