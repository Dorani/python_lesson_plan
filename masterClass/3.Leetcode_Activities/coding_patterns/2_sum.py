# Problem: Two Sum

# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

# You may assume that each input has exactly one solution, and you may not use the same element twice.

# Example 1
# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(nums, target):
    lookup = {}
    
    for i, num in enumerate(nums):
        compliment = target - num
        
        if compliment in lookup:
            return [lookup[num], i]
        else:
           lookup[num] = i 
        
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))