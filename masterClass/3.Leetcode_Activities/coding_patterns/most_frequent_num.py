# Problem #7 — Most Frequent Element

# Given a list of integers nums, return the number that appears most frequently.

# If there is a tie, return the number that appears first in the original list.

# Examples
# Input:  nums = [1, 3, 2, 3, 1, 3]
# Output: 3


nums = [1, 3, 2, 3, 1, 3]

def most_frequent(nums):
    lookup = {}
    
    for num in nums:
        if num in lookup:
            lookup[num] += 1
        else:
            lookup[num] = 1
    
    best_num = nums[0]
    best_count = lookup[nums[0]]
    
    for num in nums:
        if lookup[num] > best_count:
            best_num = num
            best_count = lookup[num]
    return best_num


print(most_frequent(nums))