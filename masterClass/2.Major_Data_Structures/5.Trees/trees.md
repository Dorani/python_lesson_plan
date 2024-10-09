# Binary Search Tree (BST) Implementation in Python

## Table of Contents

1. [Introduction to Binary Search Trees](#introduction-to-binary-search-trees)
2. [How BSTs Work](#how-bsts-work)
3. [Key Operations](#key-operations)
4. [Explanation of the Code](#explanation-of-the-code)
5. [Usage](#usage)
6. [Methods Overview](#methods-overview)

---

## Introduction to Binary Search Trees

A **binary search tree (BST)** is a tree data structure where each node has at most two children, referred to as the left and right child. For each node:

- The left subtree contains values less than the node’s value.
- The right subtree contains values greater than the node’s value.

This property enables efficient searching, insertion, and deletion of nodes.

## How BSTs Work

### Structure

- Each node contains a value, a reference to the left child, and a reference to the right child.
- The **root** node is the topmost node, where all operations start.
- **Leaf nodes** have no children.

### Properties

- Left children are always smaller than their parent node.
- Right children are always greater than their parent node.
- Duplicate values are not allowed in this implementation.

## Key Operations

1. **Insertion:** Adding a new value to the tree while maintaining the BST properties.
2. **Searching (Contains):** Checking if a value exists in the tree.
3. **Traversal (Optional):** Methods like in-order, pre-order, and post-order traversal can be implemented for different use cases.

---

## Explanation of the Code

The code provides a simple implementation of a binary search tree (BST) in Python.

### Code Structure

The code consists of two classes:

1. `Node`: Represents a node in the tree, with a `value`, `left`, and `right` attributes.
2. `BinarySearchTree`: Implements the operations for a binary search tree.

The `BinarySearchTree` class has the following methods:

- `insert`: Inserts a value into the tree.
- `contains`: Checks if a value exists in the tree.
- `print_tree` (optional): For debugging, can be used to visualize the structure of the tree.

---

## Usage

To use the binary search tree, create an instance of the `BinarySearchTree` class and perform operations like insertion and searching.

```python
# Example usage of the BinarySearchTree class

# Create a new instance of the BinarySearchTree
my_tree = BinarySearchTree()

# Insert some values into the tree
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# Check if certain values are in the tree
print('BST Contains 27:')
print(my_tree.contains(27))  # Output: True

print('\nBST Contains 17:')
print(my_tree.contains(17))  # Output: False
```

## Understanding Binary Search Trees

Binary search trees provide an efficient way to store and access data. With average time complexity of O(log n) for insertion and search operations, they are widely used in situations where quick lookups, additions, or deletions are required. The code provided here demonstrates a basic implementation, but more advanced features such as tree balancing (e.g., AVL trees, Red-Black trees) can improve performance in scenarios where the tree becomes unbalanced.
