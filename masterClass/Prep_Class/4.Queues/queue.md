---

### 4. Queue - `README.md`

```markdown
# Queue Implementation in Python

## Table of Contents
1. [Introduction](#introduction)
2. [How Queues Work](#how-queues-work)
3. [Key Operations](#key-operations)
4. [Example Code](#example-code)
5. [Use Cases](#use-cases)
6. [Time Complexity](#time-complexity)

---

## Introduction

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. The first element added is the first one to be removed.

## How Queues Work

- Elements are added at the **rear** and removed from the **front**.
- Supports operations such as **enqueue**, **dequeue**, **peek**, and **isEmpty**.

## Key Operations

1. **Enqueue**: Add an element to the rear of the queue.
2. **Dequeue**: Remove the element from the front.
3. **Peek**: View the element at the front without removing it.
4. **IsEmpty**: Check if the queue is empty.

## Example Code

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
```

## Use Cases

- Task scheduling (e.g., CPU scheduling).
- Handling requests in web servers.
- Print queue management.

## Time Complexity

- Enqueue/Dequeue/Peek: O(1).
