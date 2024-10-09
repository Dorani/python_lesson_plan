# LL: Remove Duplicates (**Interview Question**)

You are given a singly linked list that contains integer values, where some of these values may be duplicated.

**Note:** This linked list class does **NOT** have a tail, which will make this method easier to implement.

Your task is to implement a method called `remove_duplicates()` within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the `remove_duplicates()` method in two different ways:

1. **Using a Set** - This approach will have a time complexity of O(n), where _n_ is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

2. **Without using a Set** - This approach will have a time complexity of O(n²), where _n_ is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.

### Method Signature

```python
def remove_duplicates(self):
```
