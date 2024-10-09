# Heaps in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Heap Terminology](#heap-terminology)
3. [Types of Heaps](#types-of-heaps)
4. [Heap Operations](#heap-operations)
5. [Heap Implementation](#heap-implementation)
6. [Use Cases](#use-cases)
7. [Time Complexity](#time-complexity)

---

## Introduction

A **heap** is a special tree-based data structure that satisfies the **heap property**, where the parent node is either greater than or equal to (max heap) or less than or equal to (min heap) its child nodes. Heaps are commonly used in priority queues, sorting algorithms, and graph algorithms like Dijkstra's shortest path.

## Heap Terminology

- **Heap Property**: The requirement that each parent node's value is greater than or equal to (max heap) or less than or equal to (min heap) its children.
- **Complete Binary Tree**: A tree in which all levels are completely filled except possibly the last, which is filled from left to right.
- **Root**: The topmost node in the heap, either the maximum (max heap) or minimum (min heap) element.

## Types of Heaps

1. **Max Heap**:

   - The value of each parent node is greater than or equal to the values of its children.
   - The root contains the largest value.

2. **Min Heap**:
   - The value of each parent node is less than or equal to the values of its children.
   - The root contains the smallest value.

## Heap Operations

1. **Insert**: Add a new element to the heap while maintaining the heap property.
2. **Delete (Extract)**: Remove the root element from the heap and restructure it to maintain the heap property.
3. **Peek**: View the root element without removing it.
4. **Heapify**: Rearrange the elements to satisfy the heap property.

## Heap Implementation

Heaps can be efficiently implemented using an array, where:

- The parent node at index `i` has children at indices `2*i + 1` (left child) and `2*i + 2` (right child).
- The child node at index `i` has a parent at index `(i-1) // 2`.

## Example Code

Here's a basic implementation of a min heap in Python:

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)
        # Move the new value to its correct position to maintain the heap property
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # While not at the root and the current node is smaller than its parent
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                # Swap if the current node is smaller than the parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        # Swap the root with the last element
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Move the new root to its correct position to maintain the heap property
        self._heapify_down(0)
        return min_value

    def _heapify_down(self, index):
        while (index * 2) + 1 < len(self.heap):
            # Get the indices of the left and right children
            left_child_index = (index * 2) + 1
            right_child_index = (index * 2) + 2
            # Find the smallest child
            smaller_child_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[left_child_index]:
                smaller_child_index = right_child_index
            # Swap if the current node is larger than the smaller child
            if self.heap[index] > self.heap[smaller_child_index]:
                self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
                index = smaller_child_index
            else:
                break

    def peek(self):
        # Return the root value (minimum) without removing it
        if len(self.heap) > 0:
            return self.heap[0]
        return None
```

## Use Cases

Heaps are widely used in various applications:

- **Priority Queues**: Efficiently implement priority queues where elements are dequeued based on priority.
- **Heapsort**: A comparison-based sorting technique that uses a heap.
- **Graph Algorithms**: Used in algorithms like Dijkstra's and Prim's for finding the shortest path and minimum spanning tree.
- **Task Scheduling**: Managing tasks with different priorities.

## Time Complexity

| Operation      | Time Complexity |
| -------------- | --------------- |
| Insert         | O(log n)        |
| Delete/Extract | O(log n)        |
| Peek           | O(1)            |
| Heapify        | O(n)            |

Where **n** is the number of elements in the heap.

Heaps provide efficient ways to manage dynamic sets of data, making them crucial in algorithms that require frequent access to the minimum or maximum element.
