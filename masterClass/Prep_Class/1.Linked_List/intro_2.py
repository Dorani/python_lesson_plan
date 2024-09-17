# Define a class for the nodes of the linked list
class Node:
    # Initialize the node with a value and no next node
    def __init__(self, value):
        self.value = value
        self.next = None

# Define a class for the linked list itself
class LinkedList:
    # Initialize the linked list with a single node (head and tail point to the same node)
    def __init__(self, value):
        new_node = Node(value)  # Create a new node with the given value
        self.head = new_node    # Set the head of the linked list to this new node
        self.tail = new_node    # Set the tail of the linked list to this new node
        self.length = 1         # Initialize the length of the list to 1
    
    # Method to print all the values in the linked list
    def print_list(self):
        temp = self.head        # Start from the head of the list
        while temp is not None: # Traverse the list until you reach the end
            print(temp.value)   # Print the value of the current node
            temp = temp.next    # Move to the next node
    
    # Method to add a node to the end of the list (append operation)
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty, make the new node both head and tail
            self.head = new_node
            self.tail = new_node
        else:                   # Otherwise, append the new node to the end and update the tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1        # Increment the length of the list
        return True
    
    # Method to remove the last node from the list (pop operation)
    def pop(self):
        if self.head is None:   # If the list is empty, return None
            return None
        temp = self.head        # Start from the head
        pre = self.head         # Track the node before the current one
        while temp.next:        # Traverse the list to find the last node
            pre = temp
            temp = temp.next
            
        self.tail = pre         # Set the tail to the second-to-last node
        self.tail.next = None   # Remove the reference to the last node
        self.length -= 1        # Decrease the length of the list
        if self.length == 0:    # If the list is now empty, reset head and tail
            self.head = None
            self.tail = None
        return temp.value       # Return the value of the removed node
    
    # Method to add a node to the beginning of the list (prepend operation)
    def prepend(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty, make the new node both head and tail
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head # Point the new node's next to the current head
        self.head = new_node    # Update the head to the new node
        self.length += 1        # Increment the length of the list
        return True
    
    # Method to remove the first node from the list (pop_first operation)
    def pop_first(self):
        if self.length == 0:    # If the list is empty, return None
            return None
        temp = self.head        # Temporarily store the current head
        self.head = self.head.next # Move the head to the next node
        temp.next = None        # Disconnect the old head from the list
        self.length -= 1        # Decrease the length of the list
        if self.length == 0:    # If the list is now empty, reset the tail
            self.tail = None
        return temp.value       # Return the value of the removed node
    
    # Method to get a node at a specific index
    def get(self, index):
        if index < 0 or index >= self.length:  # Return None if the index is out of bounds
            return None
        temp = self.head        # Start from the head of the list
        for _ in range(index):  # Traverse the list up to the given index
            temp = temp.next
        return temp             # Return the node at the specified index
    
    # Method to update the value of a node at a specific index
    def set_value(self, index, value):
        temp = self.get(index)  # Get the node at the given index
        if temp:                # If the node exists, update its value
            temp.value = value
            return True
        return False            # Return False if the node doesn't exist
    
    # Method to insert a node at a specific index
    def insert(self, index, value):
        if index < 0 or index >= self.length:  # Return False if the index is out of bounds
            return False
        if index == 0:          # If inserting at the beginning, prepend the value
            return self.prepend(value)
        if index == self.length: # If inserting at the end, append the value
            return self.append(value)
        new_node = Node(value)   # Create a new node
        temp = self.get(index-1) # Get the node just before the insertion point
        new_node.next = temp.next # Link the new node to the following node
        temp.next = new_node     # Link the previous node to the new node
        self.length += 1         # Increment the length of the list
        return True
    
    # Method to remove a node at a specific index
    def remove(self, index):
        if index < 0 or index >= self.length:  # Return None if the index is out of bounds
            return None
        if index == 0:          # If removing the first node, use pop_first
            return self.pop_first()
        if index == self.length - 1: # If removing the last node, use pop
            return self.pop()
        pre = self.get(index - 1)  # Get the node just before the one to be removed
        temp = pre.next         # Get the node to be removed
        pre.next = temp.next    # Link the previous node to the one after the removed node
        temp.next = None        # Disconnect the removed node from the list
        self.length -= 1        # Decrease the length of the list
        return temp
    
    # Method to reverse the entire linked list
    def reverser(self):
        temp = self.head        # Start from the head of the list
        self.head = self.tail   # Swap the head and the tail
        self.tail = temp
        after = temp.next       # Keep track of the next node in the list
        before = None           # Initialize a pointer for the previous node (none at first)
        for _ in range(self.length):  # Traverse the list
            after = temp.next   # Move to the next node
            temp.next = before  # Reverse the link of the current node
            before = temp       # Move the before pointer forward
            temp = after        # Move the temp pointer forward to the next node


# Instantiate the LinkedList class with a starting value
my_linked_list = LinkedList(10)  # Linked list: 10

# Print the list
print("Initial list:")
my_linked_list.print_list()  # Output: 10

# Append elements to the list
my_linked_list.append(20)  # Linked list: 10 -> 20
my_linked_list.append(30)  # Linked list: 10 -> 20 -> 30
print("\nList after appending 20 and 30:")
my_linked_list.print_list()  # Output: 10 -> 20 -> 30

# Pop the last element (removing 30)
popped_value = my_linked_list.pop()  # Linked list: 10 -> 20
print(f"\nPopped value: {popped_value}")  # Output: Popped value: 30
print("List after popping:")
my_linked_list.print_list()  # Output: 10 -> 20

# Prepend an element to the beginning of the list
my_linked_list.prepend(5)  # Linked list: 5 -> 10 -> 20
print("\nList after prepending 5:")
my_linked_list.print_list()  # Output: 5 -> 10 -> 20

# Pop the first element (removing 5)
first_popped_value = my_linked_list.pop_first()  # Linked list: 10 -> 20
print(f"\nPopped first value: {first_popped_value}")  # Output: Popped first value: 5
print("List after popping first:")
my_linked_list.print_list()  # Output: 10 -> 20

# Get a node at index 1
node_at_index_1 = my_linked_list.get(1)  # Should return the node with value 20
print(f"\nNode at index 1: {node_at_index_1.value}")  # Output: Node at index 1: 20

# Set a new value at index 0
my_linked_list.set_value(0, 15)  # Linked list: 15 -> 20
print("\nList after setting value 15 at index 0:")
my_linked_list.print_list()  # Output: 15 -> 20

# Insert a value at index 1
my_linked_list.insert(1, 17)  # Linked list: 15 -> 17 -> 20
print("\nList after inserting 17 at index 1:")
my_linked_list.print_list()  # Output: 15 -> 17 -> 20

# Remove a node at index 1 (removes 17)
removed_node = my_linked_list.remove(1)  # Linked list: 15 -> 20
print(f"\nRemoved node value: {removed_node.value}")  # Output: Removed node value: 17
print("List after removing node at index 1:")
my_linked_list.print_list()  # Output: 15 -> 20

# Reverse the linked list
my_linked_list.reverser()  # Linked list: 20 -> 15
print("\nList after reversing:")
my_linked_list.print_list()  # Output: 20 -> 15
