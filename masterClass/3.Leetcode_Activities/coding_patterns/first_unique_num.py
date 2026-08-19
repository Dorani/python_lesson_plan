# Problem #6 — First Unique Number

# Given a list of integers nums, return the first number that appears exactly once.

# If every number appears more than once, return -1.

# Examples
# Input:  nums = [4, 5, 1, 2, 1, 4]
# Output: 5


def first_unique_num(nums):
    lookup = {}
    
    for num in nums:
        if num in lookup:
            lookup[num] += 1
        else:
            lookup[num] = 1
            
    for num in nums:
        if lookup[num] == 1:
            return num
    return -1

        
        
nums = [4, 5, 1, 2, 1, 4]
print(first_unique_num(nums))