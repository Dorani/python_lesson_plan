# Linked List Implementation in Python

## Table of Contents

1. [Introduction](#introduction)
2. [How Linked Lists Work](#how-linked-lists-work)
3. [Key Operations](#key-operations)
4. [Example Code](#example-code)
5. [Use Cases](#use-cases)
6. [Time Complexity](#time-complexity)

---

## Introduction

A **linked list** is a linear data structure where each element is a separate object called a node. Each node contains:

1. **Data**: The value stored in the node.
2. **Next**: A reference (or pointer) to the next node in the sequence.

## How Linked Lists Work

In a **singly linked list**, each node points to the next node, forming a chain. The first node is known as the **head**, and the last node points to `None`, indicating the end of the list.

## Key Operations

1. **Insertion**: Add a new node at the beginning, middle, or end of the list.
2. **Deletion**: Remove a node from the list.
3. **Traversal**: Access each node's data by iterating through the list.
4. **Search**: Find a node with a specific value.

## Example Code

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
```

## Use Cases

- Dynamic memory allocation.
- Implementation of stacks and queues.
- Navigation through web pages (back and forward).
- Undo functionality in applications.

## Time Complexity

Insertion: O(1) at the head, O(n) at the end.
Deletion: O(1) if at the head, O(n) otherwise.
Traversal/Search: O(n).
