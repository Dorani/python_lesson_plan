## LL: Find Kth Node From End (\*\*Interview Question)

### Problem:

Implement the `find_kth_from_end` function, which takes the `LinkedList` (`ll`) and an integer `k` as input, and returns the k-th node from the end of the linked list **without using the length**.

### Example:

Given this LinkedList:

- If `k=1`, then return the first node from the end (the last node), which contains the value `4`.
- If `k=2`, then return the second node from the end, which contains the value `3`, etc.

If the index is out of bounds, the program should return `None`.

### Requirements:

- The function should utilize **two pointers**, `slow` and `fast`, initialized to the head of the linked list.
- The **fast pointer** should move `k` nodes ahead in the list.
- If the **fast pointer** becomes `None` before moving `k` nodes, the function should return `None`, as the list is shorter than `k` nodes.

- The `slow` and `fast` pointers should then move forward in the list at the same time until the **fast pointer** reaches the end of the list.
- The function should return the **slow pointer**, which will be at the k-th position from the end of the list.

### Important:

This is a **separate function** that is not a method within the `LinkedList` class. This means you need to indent the function all the way to the **left**.
