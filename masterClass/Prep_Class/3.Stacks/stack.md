---

### 3. Stack - `README.md`

```markdown
# Stack Implementation in Python

## Table of Contents
1. [Introduction](#introduction)
2. [How Stacks Work](#how-stacks-work)
3. [Key Operations](#key-operations)
4. [Example Code](#example-code)
5. [Use Cases](#use-cases)
6. [Time Complexity](#time-complexity)

---

## Introduction

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The last element added is the first one to be removed.

## How Stacks Work

- Elements are added and removed from the **top**.
- Supports operations such as **push**, **pop**, **peek**, and **isEmpty**.

## Key Operations

1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove the element from the top.
3. **Peek**: View the element at the top without removing it.
4. **IsEmpty**: Check if the stack is empty.

## Example Code

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
```

## Use Cases

- Function call stack.
- Undo and redo operations in text editors.
- Evaluating expressions (e.g., balancing parentheses).

## Time Complexity

- Push/Pop/Peek: O(1).
