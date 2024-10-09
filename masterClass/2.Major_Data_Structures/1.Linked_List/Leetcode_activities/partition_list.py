class Node:
    # Constructor for creating a new node
    def __init__(self, value):
        self.value = value  # The value/data contained in the node
        self.next = None  # Pointer to the next node in the list (None by default)

class LinkedList:
    # Constructor for initializing a linked list
    def __init__(self):
        self.head = None  # The head of the list is initially set to None (empty list)
    
    # Method to append a node to the end of the linked list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Traverse the list to find the last node
                temp = temp.next
            temp.next = new_node  # Set the next of the last node to the new node

    # Method to print the linked list
    def print_list(self):
        temp = self.head  # Start from the head node
        while temp:
            print(temp.value, end=" -> " if temp.next else "\n")  # Print each node's value
            temp = temp.next  # Move to the next node
    
    # Method to partition the linked list around a value x
    def partition_list(self, x):
        # 1. Handle edge case: If the list is empty (no head), return None
        if not self.head:
            return None
        
        # 2. Create two dummy nodes to start the two chains (for < x and >= x)
        dummy1 = Node(0)  # Dummy head for the chain of nodes with values less than x
        dummy2 = Node(0)  # Dummy head for the chain of nodes with values greater than or equal to x
        
        # 3. Create pointers to track the end of both chains
        prev1 = dummy1  # Pointer to track the end of the chain for nodes less than x
        prev2 = dummy2  # Pointer to track the end of the chain for nodes greater than or equal to x
        
        # 4. Iterate through the original list
        current = self.head  # Start from the head of the original linked list
        
        while current:
            if current.value < x:
                # 5. Add nodes with values less than x to the first chain
                prev1.next = current  # Link current node to the end of the "less than" chain
                prev1 = current  # Move prev1 forward to the current node
            else:
                # 6. Add nodes with values greater than or equal to x to the second chain
                prev2.next = current  # Link current node to the end of the "greater than or equal to" chain
                prev2 = current  # Move prev2 forward to the current node
            
            current = current.next  # Move to the next node in the original list
        
        # 7. End both chains (set the next pointer of the last node to None)
        prev1.next = None  # Ensure the last node of the "less than" chain points to None
        prev2.next = None  # Ensure the last node of the "greater than or equal to" chain points to None
        
        # 8. Combine the two chains by connecting the "less than" chain to the "greater than or equal to" chain
        prev1.next = dummy2.next  # Link the end of the "less than" chain to the start of the "greater than or equal to" chain
        
        # 9. Update the head of the linked list to the head of the "less than" chain
        self.head = dummy1.next  # The new head of the list is the start of the "less than" chain

# Example usage of the LinkedList and partition_list function
if __name__ == "__main__":
    ll = LinkedList()  # Create a new LinkedList object
    ll.append(3)  # Append nodes to the linked list
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    
    print("Original List:")
    ll.print_list()  # Print the original list
    
    # Partition the list around the value 5
    ll.partition_list(5)
    
    print("Partitioned List:")
    ll.print_list()  # Print the partitioned list
