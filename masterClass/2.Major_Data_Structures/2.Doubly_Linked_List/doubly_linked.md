---

### 2. Doubly Linked List - `README.md`

```markdown
# Doubly Linked List Implementation in Python

## Table of Contents
1. [Introduction](#introduction)
2. [How Doubly Linked Lists Work](#how-doubly-linked-lists-work)
3. [Key Operations](#key-operations)
4. [Example Code](#example-code)
5. [Use Cases](#use-cases)
6. [Time Complexity](#time-complexity)

---

## Introduction

A **doubly linked list** is a linear data structure similar to a singly linked list, but each node contains an additional pointer called **prev**, which points to the previous node.

## How Doubly Linked Lists Work

- Each node has three components: `value`, `next`, and `prev`.
- Allows for traversal in both directions (forward and backward).
- The first node is called the **head**, and the last node is called the **tail**.

## Key Operations

1. **Insertion**: Add a new node at the beginning, middle, or end of the list, updating both `next` and `prev` pointers.
2. **Deletion**: Remove a node by updating both the `next` and `prev` pointers of adjacent nodes.
3. **Traversal**: Move forward or backward through the list.
4. **Search**: Find a node with a specific value.

## Example Code

```python
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next
```

## Use Cases

- Implementation of browser history (backward and forward navigation).
- Undo and redo operations in applications.

## Memory management.

- Time Complexity
  - Insertion/Deletion: O(1).
  - Traversal/Search: O(n).
