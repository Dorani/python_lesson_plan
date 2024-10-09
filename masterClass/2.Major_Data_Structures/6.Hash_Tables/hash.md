# Hash Table Implementation in Python

## Table of Contents

1. [Introduction to Hash Tables](#introduction-to-hash-tables)
2. [Hashing Explained](#hashing-explained)
3. [How Hash Tables Work](#how-hash-tables-work)
4. [Collision Handling](#collision-handling)
5. [Explanation of the Code](#explanation-of-the-code)
6. [Usage](#usage)
7. [Methods Overview](#methods-overview)

---

## Introduction to Hash Tables

A **hash table** is a data structure that stores key-value pairs. It allows for fast data retrieval, insertion, and deletion based on the key. The main advantage of a hash table is its efficiency; operations can be performed in constant time, on average, regardless of the number of elements stored.

## Hashing Explained

**Hashing** is the process of converting a given key (often a string) into a specific index within a fixed-size array (hash table). This index is calculated using a hash function. The hash function aims to distribute keys uniformly across the table to minimize collisions.

## How Hash Tables Work

1. **Hash Function:** Converts a key into a numerical index.
2. **Storage:** The key-value pair is stored at the index calculated by the hash function.
3. **Retrieval:** The same hash function is used to find the index associated with a key, allowing quick access to the corresponding value.

## Collision Handling

Since multiple keys may produce the same hash (index), collisions are inevitable in hash tables. There are several ways to handle collisions:

- **Separate Chaining:** Uses linked lists to store multiple key-value pairs at the same index.
- **Open Addressing:** Finds another open spot in the hash table when a collision occurs.

In this code, we use **separate chaining**, where each index in the array can store a list of key-value pairs.

---

## Explanation of the Code

The code provides a simple implementation of a hash table in Python using separate chaining for collision handling.

### Code Structure

The code consists of a `HashTable` class with the following key methods:

- `__init__`: Initializes the hash table with a specified size.
- `__hash`: A private method that generates a hash index for a given key.
- `set_item`: Adds a key-value pair to the hash table.
- `get_item`: Retrieves the value associated with a given key.
- `keys`: Returns a list of all keys stored in the hash table.
- `print_table`: Prints the contents of the hash table for debugging.

---

## Usage

To use the hash table, create an instance of the `HashTable` class and perform operations like adding, retrieving, and listing keys.

```python
# Example usage of the HashTable class

my_hash_table = HashTable()

# Add some items to the hash table
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

# Print all the keys stored in the hash table
print(my_hash_table.keys())

# Output:
# ['bolts', 'washers', 'lumber']
```

## Understanding Hash Tables

Hash tables are an essential data structure that balances speed and efficiency. They are used in many applications like databases, caching, and implementing associative arrays. This example demonstrates a simple implementation using separate chaining to handle collisions effectively.
