class MaxHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def _left_child(self, index):
        # Calculate the index of the left child
        return 2 * index + 1

    def _right_child(self, index):
        # Calculate the index of the right child
        return 2 * index + 2

    def _parent(self, index):
        # Calculate the index of the parent node
        return (index - 1) // 2

    def _swap(self, index1, index2):
        # Swap the values at the two given indices
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)
        # Get the index of the newly added value
        current = len(self.heap) - 1

        # Bubble up the value to maintain the max heap property
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            # If the current value is larger than its parent, swap them
            self._swap(current, self._parent(current))
            # Move up to the parent's index and continue checking
            current = self._parent(current)

    def _sink_down(self, index):
        # Sinks the value at the given index down to its correct position to maintain the heap property
        max_index = index
        while True:
            # Get the indices of the left and right children
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Check if the left child exists and is larger than the current node
            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            # Check if the right child exists and is larger than the current largest node
            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            # If the largest value is not the current node, swap it with the larger child
            if max_index != index:
                self._swap(index, max_index)
                # Continue sinking down at the new index
                index = max_index
            else:
                # If the current node is larger than its children, stop sinking down
                return

    def remove(self):
        # Removes and returns the maximum value (root) from the heap
        if len(self.heap) == 0:
            # If the heap is empty, return None
            return None

        if len(self.heap) == 1:
            # If the heap has only one element, remove and return it
            return self.heap.pop()

        # Save the maximum value to return later
        max_value = self.heap[0]
        # Move the last element to the root position
        self.heap[0] = self.heap.pop()
        # Sink the new root down to its correct position to maintain the heap property
        self._sink_down(0)

        # Return the original maximum value
        return max_value

# Example usage
myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

# Print the heap after all insertions
print(myheap.heap)  # Output should be: [95, 75, 80, 55, 60, 50, 65]

# Remove the maximum value (95) and print the heap
myheap.remove()
print(myheap.heap)  # Output should be: [80, 75, 65, 55, 60, 50]

# Remove the next maximum value (80) and print the heap
myheap.remove()
print(myheap.heap)  # Output should be: [75, 60, 65, 55, 50]

"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]
"""
