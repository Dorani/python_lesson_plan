# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

def getRow(rowIndex: int):
        previous = [1]

        for i in range(1, rowIndex + 1):
            current = [1] * (i + 1)
            for j in range(1, i):
                current[j] = previous[j - 1] + previous[j]
            previous = current 
        return previous
print(getRow(3)) # [1,3,3,1]
print(getRow(0)) # [1]
print(getRow(1)) # [1,1]
print(getRow(2)) # [1,2,1]