## LL: Partition List (\*\*Interview Question)

⚠️ **CAUTION: Advanced Challenge Ahead!**

This Linked List problem is significantly more challenging than the ones we've tackled so far. It's common for students at this stage to find this exercise demanding, so don't worry if you're not ready to tackle it yet. It's perfectly okay to set it aside and revisit it later when you feel more confident.

If you decide to take on this challenge, I strongly advise using a hands-on approach: grab a piece of paper and visually map out each step.

This problem requires a clear understanding of how elements in a Linked List interact and move. By now, you've observed numerous Linked List animations in the course, which have prepared you for this moment.

This exercise will be a true test of your ability to apply those concepts practically. Remember, patience and persistence are key here!

### Exercise:

Implement the `partition_list` member function for the `LinkedList` class, which partitions the list such that all nodes with values less than `x` come before nodes with values greater than or equal to `x`.

- **Note**: This linked list class does NOT have a tail, which will make this method easier to implement.
- The original relative order of the nodes should be preserved.

### Details:

The function `partition_list` takes an integer `x` as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.

### Example 1:

**Input**:

- Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
  **Process**:

- Values less than 5: 3, 2, 1
- Values greater than or equal to 5: 8, 5, 10

**Output**:

- Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

### Tips:

- While traversing the linked list, maintain **two separate chains**: one for values less than `x` and one for values greater than or equal to `x`.
- Use **dummy nodes** to simplify the handling of the heads of these chains.
- After processing the entire list, connect the two chains to get the desired arrangement.

### Notes:

- The solution must **maintain the relative order** of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 as their relative order remains unchanged.
- You must solve the problem **without modifying the values** in the list's nodes (i.e., only the nodes' next pointers may be changed).
