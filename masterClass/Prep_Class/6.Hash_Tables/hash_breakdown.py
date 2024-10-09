class HashTable:
    # Initialize the HashTable with a fixed size. 
    # Default size is 7, but this can be changed by passing a different value.
    def __init__(self, size=7):
        # Create a list (array) with 'size' number of elements, all set to None initially.
        # This will hold the key-value pairs using separate chaining (linked lists).
        self.data_map = [None] * size
    
    # Private method to create a hash for a given key.
    # It converts each character in the key to its ASCII value and computes a hash using modulo.
    def __hash(self, key):
        my_hash = 0
        # Loop through each character in the key
        for letter in key:
            # Update the hash value based on the character's ASCII value, a multiplier (23),
            # and the size of the data_map to ensure it stays within the list's index range.
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        # Return the calculated hash value (index)
        return my_hash  

    # Method to print the entire hash table for debugging/visualization purposes
    def print_table(self):
        # Enumerate through the data_map and print each index and its corresponding value
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    # Method to add a key-value pair to the hash table
    def set_item(self, key, value):
        # Get the index by hashing the key
        index = self.__hash(key)
        # If there's no linked list at this index, create an empty list (to handle collisions)
        if self.data_map[index] is None:
            self.data_map[index] = []
        # Append the key-value pair to the list at the calculated index
        # This handles collisions using separate chaining
        self.data_map[index].append([key, value])
    
    # Method to retrieve the value associated with a given key
    def get_item(self, key):
        # Get the index by hashing the key
        index = self.__hash(key)
        # If there's a list at this index, search through the list for the key
        if self.data_map[index] is not None:
            # Loop through the list to find the key
            for i in range(len(self.data_map[index])):
                # If the key matches, return the associated value
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        # If the key is not found, or there's no list at this index, return None
        return None

    # Method to retrieve all the keys stored in the hash table
    def keys(self):
        # Create a list to store all the keys
        all_keys = []
        # Loop through the entire data_map
        for i in range(len(self.data_map)):
            # If there's a list at the current index, go through each key-value pair
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    # Append each key to the all_keys list
                    all_keys.append(self.data_map[i][j][0])
        # Return the list of all keys
        return all_keys
        

# Example usage of the HashTable class

my_hash_table = HashTable()

# Add some items to the hash table
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

# Print all the keys stored in the hash table
print(my_hash_table.keys())

"""
    EXPECTED OUTPUT:
    ----------------
    ['bolts', 'washers', 'lumber']
"""
